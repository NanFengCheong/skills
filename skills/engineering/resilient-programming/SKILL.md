---
name: resilient-programming
description: Design systems that survive and recover from failures. Covers retries with exponential backoff, circuit breakers, bulkheads, graceful degradation, fallbacks, timeouts, health checks, graceful shutdown, rate limiting, load shedding, and compensating transactions. Use when integrating with external services, designing async/background jobs, adding network calls, handling DB/queue failures, or architecting system-level reliability.
---

# Resilient Programming

## Philosophy

Failures are inevitable. Design so that when something fails, the system degrades gracefully, recovers automatically, and the blast radius is contained.

## Patterns

### 1. Timeouts Everywhere

Every external call must have a timeout. No infinite waits.

```ts
const result = await fetch(url, { signal: AbortSignal.timeout(5000) })
```

Default timeout: 5s for external HTTP, 10s for batch queries, 30s for long-running operations. Tune per dependency based on its p99.

### 2. Retries with Exponential Backoff + Jitter

Retry transient failures, but never without backoff and never without a cap.

```ts
async function fetchWithRetry(url: string, maxRetries = 3): Promise<Response> {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      return await fetch(url, { signal: AbortSignal.timeout(5000) })
    } catch (err) {
      if (attempt === maxRetries - 1) throw err
      const delay = Math.min(1000 * 2 ** attempt, 10000) // exponential
        + Math.random() * 100                            // jitter
      await sleep(delay)
    }
  }
}
```

**Rules:**
- Retry only on idempotent operations (GET, idempotent PUT/POST with idempotency keys)
- Cap total retry time (< 30s for user-facing, unbounded for background with a DLQ)
- Add jitter (±25%) to avoid thundering herd
- 4xx (except 429/503) are not retryable

### 3. Circuit Breaker

Stop calling a failing dependency to let it recover and prevent cascading failures.

```ts
const breaker = new CircuitBreaker({
  threshold: 5,              // failures before open
  resetTimeout: 30_000,      // wait 30s before half-open
  onOpen: () => alertOncall(),
})
```

**States:** Closed (normal) → Open (failing, fast-fail) → Half-Open (probing) → Closed or Open.

### 4. Bulkheads / Isolation

Isolate dependencies so one failure doesn't take down the whole system.

```ts
// Each external service gets its own connection pool / thread pool / rate limiter
const authPool = new ConnectionPool({ max: 5 })
const billingPool = new ConnectionPool({ max: 5 })
const analyticsPool = new ConnectionPool({ max: 2 }) // less critical
```

**Antipattern:** shared connection pool across all backends — one slow dependency starves the rest.

### 5. Graceful Degradation

When a dependency fails, respond with degraded data, not an error.

```ts
async function getUserProfile(id: string): Promise<Profile> {
  const [profile, recommendations, ads] = await Promise.allSettled([
    fetchProfile(id),
    fetchRecommendations(id),
    fetchAds(id),
  ])

  return {
    profile: profile.status === 'fulfilled' ? profile.value : null,
    recommendations: recommendations.status === 'fulfilled' ? recommendations.value : null,
    ads: ads.status === 'fulfilled' ? ads.value : null,
  }
}
```

**Skeleton pattern:** Serve core data from the primary source. Non-critical enrichments (ads, recommendations, social proof) can be empty/null without failing the request.

### 6. Fallbacks and Defaults

Every integration point needs a fallback behavior.

- **Config value fails to load** → use hardcoded safe default
- **Cache miss + DB down** → serve stale cache, not error
- **3rd-party API down** → use last-known-good data
- **Feature flag service unreachable** → treat flag as disabled (safe side)

### 7. Health Checks

Expose a health endpoint that checks all critical dependencies. Use for load balancer routing and Kubernetes probes.

```
GET /health → 200 OK
GET /health?check=ready → 200 OK (readiness: can serve traffic)
GET /health?check=live → 200 OK (liveness: process is alive)
```

### 8. Graceful Shutdown

Handle SIGTERM/SIGINT: stop accepting new work, finish in-flight work, then exit.

```ts
process.on('SIGTERM', async () => {
  logger.info('shutting down...')
  server.close()
  await queue.drain()
  await db.close()
  process.exit(0)
})
```

### 9. Rate Limiting

Protect your system from bursts and abusive clients.

```ts
// Per-user rate limit
const limiter = new RateLimiter({ windowMs: 60_000, max: 100, key: userId })
```

### 10. Load Shedding

When at capacity, drop low-priority work before degrading critical paths.

- Reject non-critical requests with 503
- Prioritize authenticated users over anonymous
- Queue background jobs, reject if queue is full

### 11. Compensating Transactions

Distributed operations that span multiple services must handle partial failure. When step 2 of 3 fails, execute a compensating action for step 1 (delete created resource, release lock, reverse payment).

## Observability for Resilience

Every failure mode must produce telemetry:

```
Metric: failed_calls_total{service="billing"} 7
Metric: circuit_breaker_state{service="auth"} open
Log:    POST /orders failed — DB timeout, circuit open
Alert:  billing error rate > 5% for 5 minutes
```

Without observability, resilience patterns hide problems instead of solving them.

## Checklist

```
[ ] Every external call has a timeout
[ ] Retry configured with exponential backoff + jitter + cap
[ ] Circuit breaker or at least a max-retry guard
[ ] Dependencies use separate connection pools
[ ] Non-critical failures degrade gracefully
[ ] Fallback values exist for every integration
[ ] Health endpoint checks critical deps
[ ] Graceful shutdown drains work before exit
[ ] Rate limiting on public endpoints
[ ] Load shedding at capacity
[ ] Compensating actions for multi-step operations
[ ] Failure metrics and alerts configured
```

## Related Skills

- **[defensive-programming](../defensive-programming/SKILL.md)** — code-level safeguards (validation, preconditions, defensive copies). Use at the trust boundary inside resilient wrappers.
- **[tdd](../tdd/SKILL.md)** — write integration tests that verify retry logic, circuit breaker state transitions, and graceful degradation paths.
- **[diagnose](../diagnose/SKILL.md)** — when a production incident involves timeout, cascading failure, or partial outage, use diagnose to trace the gap, then apply the resilience pattern.
