#!/usr/bin/env python3
"""Validate the instruction registry and recipe dependencies; performs no business actions."""
import copy
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REFERENCES = ROOT / "cucuma-chief-of-staff" / "references"


def validate(registry, scenarios, root):
    errors = []
    if registry.get("contract_version") != 1 or scenarios.get("contract_version") != 1:
        errors.append("unsupported contract version")
    modules = registry.get("modules", {})
    for name, module in modules.items():
        target = (root / module["path"]).resolve()
        owner = (root / module["owner"]).resolve()
        if not target.is_relative_to(owner) or not target.is_file():
            errors.append(f"{name}: missing module or wrong owner")
        elif target.is_file():
            content = target.read_text()
            if f"- Module: `{name}`" not in content:
                errors.append(f"{name}: module header drift")
            if f"- Version: {module['revision']}\n" not in content:
                errors.append(f"{name}: revision header drift")
            for label, key in (("Required inputs", "inputs"), ("Outputs", "outputs")):
                line = re.search(rf"^- {label}: (.+)$", content, re.MULTILINE)
                keys = re.findall(r"`([^`]+)`", line.group(1)) if line else []
                if keys != module[key]:
                    errors.append(f"{name}: {key} header drift")
            if "decision_values" in module:
                line = re.search(r"^- Decision values: (.+)$", content, re.MULTILINE)
                values = re.findall(r"`([^`]+)`", line.group(1)) if line else []
                if values != module["decision_values"] or module["decision_field"] not in content:
                    errors.append(f"{name}: decision contract drift")
        if not (owner / "SKILL.md").is_file():
            errors.append(f"{name}: owner skill missing")
        if not isinstance(module.get("revision"), int) or module["revision"] < 1:
            errors.append(f"{name}: invalid revision")
        for key in ("inputs", "outputs"):
            values = module.get(key, [])
            if not values or len(values) != len(set(values)):
                errors.append(f"{name}: missing or duplicate {key}")
    for name, recipe in registry.get("recipes", {}).items():
        available = set(recipe["inputs"])
        if len(recipe["steps"]) != len(set(recipe["steps"])):
            errors.append(f"{name}: repeated step; resume from an explicit invocation")
        for step in recipe["steps"]:
            if step not in modules:
                errors.append(f"{name}: unknown step {step}")
                continue
            missing = set(modules[step]["inputs"]) - available
            if missing:
                errors.append(f"{name}/{step}: unavailable inputs {sorted(missing)}")
            available.update(modules[step]["outputs"])
        if set(recipe["outputs"]) - available:
            errors.append(f"{name}: unreachable outputs")
    cases = scenarios.get("scenarios", [])
    if len({case["id"] for case in cases}) != len(cases):
        errors.append("duplicate scenario IDs")
    covered = {case["module"] for case in cases if case.get("request") and case.get("expect")}
    if set(modules) != covered:
        errors.append("scenario coverage does not match module registry")
    return errors


if __name__ == "__main__":
    registry = json.loads((REFERENCES / "recipes.json").read_text())
    scenarios = json.loads((REFERENCES / "composition-scenarios.json").read_text())
    errors = validate(registry, scenarios, ROOT)
    # A recipe must not silently accept an unavailable upstream artifact.
    broken = copy.deepcopy(registry)
    broken["recipes"]["source-to-drafts"]["inputs"] = []
    if not any("unavailable inputs" in error for error in validate(broken, scenarios, ROOT)):
        errors.append("validator failed missing-input self-check")
    changed = copy.deepcopy(registry)
    changed["modules"]["source-intake"]["revision"] += 1
    if not any("revision header drift" in error for error in validate(changed, scenarios, ROOT)):
        errors.append("validator failed revision-drift self-check")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(registry['modules'])} modules, {len(registry['recipes'])} recipes, "
          f"{len(scenarios['scenarios'])} scenario definitions; dependency/revision self-checks passed.")
