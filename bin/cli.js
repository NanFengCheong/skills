#!/usr/bin/env node
const { execSync } = require("child_process");
const path = require("path");
const fs = require("fs");

const REPO = path.resolve(__dirname, "..");

function exec(cmd, cwd = REPO) {
  try {
    execSync(cmd, { cwd, stdio: "inherit" });
  } catch {
    process.exit(1);
  }
}

function findSkills() {
  const { execSync } = require("child_process");
  const out = execSync(
    `find "${REPO}/skills" -name SKILL.md -not -path '*/node_modules/*'`,
    { encoding: "utf8" }
  );
  return out
    .trim()
    .split("\n")
    .filter(Boolean)
    .map((p) => path.relative(REPO, path.dirname(p)));
}

const help = `
Usage: npx @nanfengcheong/skills <command>

Commands:
  list                List all available skills
  link                Link skills to ~/.claude/skills
  help                Show this help message
`.trim();

const cmd = process.argv[2];

if (!cmd || cmd === "help") {
  console.log(help);
  console.log(`\n${findSkills().length} skills available.`);
  process.exit(0);
}

switch (cmd) {
  case "list":
    console.log(findSkills().join("\n"));
    break;
  case "link":
    exec(`"${REPO}/scripts/link-skills.sh"`);
    break;
  default:
    console.error(`Unknown command: ${cmd}\n`);
    console.error(help);
    process.exit(1);
}
