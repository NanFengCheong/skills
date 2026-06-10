---
name: defensive-programming
description: Write code that anticipates and contains failures at trust boundaries. Covers input validation, fail-fast with preconditions, assertions for invariants, defensive copies, null/undefined discipline, type narrowing, and guard clauses. Use when writing public APIs, parsers, user input handlers, deserialization boundaries, or any code receiving data from an untrusted source.
---

# Defensive Programming

## Philosophy

Assume every external input, dependency response, and concurrent state is hostile or broken. Validate early, fail fast, fail cleanly. Push complexity to boundaries — keep internals safe.

## Rules

### 1. Validate at Trust Boundaries

Validate all data the moment it enters your system — API handler, file read, deserialization, env var, user input. After validation, internals operate on guaranteed types.

```ts
// bad — validation deferred or partial
function process(req: Request) {
  const id = req.body.id // could be anything
  db.query(`SELECT * FROM users WHERE id = ${id}`)
}

// good — validate at the boundary
function process(req: Request) {
  const id = parseUserId(req.body.id)
  db.query('SELECT * FROM users WHERE id = $1', [id])
}
```

### 2. Fail Fast with Preconditions

Check preconditions at the start of every public function. Use a consistent pattern (guard clauses, `assert`, or a validation lib). Fail immediately, not 10 calls deep.

```ts
function withdraw(account: Account, amount: number): void {
  assert(amount > 0, 'amount must be positive')
  assert(amount <= account.balance, 'insufficient funds')
  // safe to proceed
}
```

**Which to use:**
- `assert` / invariant checks — for programming errors (should never happen)
- `throw` / `Result.Err` — for expected failure modes (validation errors, not-found)
- Return types (`Option`, `Result`) — when callers should handle absence/failure

### 3. Never Trust Mutable Input

Defensively copy mutable data from external sources. Your internals should own their data.

```ts
class OrderStore {
  #items: Item[]

  constructor(items: Item[]) {
    this.#items = items.map(i => ({ ...i })) // defensive copy
  }

  getItems(): readonly Item[] {
    return Object.freeze([...this.#items])
  }
}
```

### 4. Exhaustive Conditionals

Every branch of a union/switch/enum must be handled. If a new variant is added, the compiler or a default handler catches it.

```ts
type Status = 'active' | 'inactive' | 'pending'

function handleStatus(s: Status): string {
  switch (s) {
    case 'active':   return 'Active'
    case 'inactive': return 'Inactive'
    case 'pending':  return 'Pending'
    default:
      const _exhaustive: never = s
      throw new Error(`unhandled status: ${s}`)
  }
}
```

### 5. Null/Undefined Discipline

Use the type system to make null/undefined impossible when it should be. `T | null` is a contract, not an accident.

```ts
// bad — hides the null case
function findUser(id: string): User

// good — type signals absence
function findUser(id: string): User | null
```

Never pass `null` to a function that doesn't declare it. Prefer `Option<T>` / `Maybe<T>` / `T | undefined` based on language convention.

### 6. Fail-Safe Defaults

Every config, flag, and feature gate must have a safe default. Safe = least privilege, least access, least risk.

```ts
const config = {
  maxRetries: 3,       // safe: bounded
  timeoutMs: 5000,     // safe: no infinite wait
}
```

### 7. Never Swallow Errors

Every caught exception must be logged, wrapped, or explicitly handled. Silent `catch {}` is forbidden.

```ts
// bad
try { risky() } catch {}

// good
try { risky() } catch (err) {
  logger.error('risky failed', { err })
  throw // or return fallback
}
```

### 8. Principle of Least Privilege

Expose the minimum surface area. Mark internal functions private. Accept only what you need, not entire objects.

```ts
// bad — accepts everything
function save(user: FullUser) { ... }

// good — accepts only what it uses
function save(id: string, email: Email) { ... }
```

## Checklist

```
[ ] Every input validated at the trust boundary
[ ] Preconditions checked on every public function
[ ] No silent catch blocks
[ ] Defensive copies on mutable external data
[ ] Null/undefined impossible where it shouldn't exist
[ ] Every branch of a union/enum handled
[ ] Config has safe defaults
[ ] Each function accepts minimum required data
[ ] Exceptions are never ignored
```

## Related Skills

- **[resilient-programming](../resilient-programming/SKILL.md)** — system-level fault tolerance (retries, circuit breakers, timeouts). Use alongside when the code at the boundary talks to a network service.
- **[tdd](../tdd/SKILL.md)** — use during the RED phase to write tests that probe edge cases and invariants the defensive check protects.
- **[diagnose](../diagnose/SKILL.md)** — when a bug is caused by missing validation or an unguarded code path, run diagnose to isolate the gap, then apply the defensive pattern from this skill.
