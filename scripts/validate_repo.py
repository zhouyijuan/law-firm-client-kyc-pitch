#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
NAME = "law-firm-client-kyc-pitch"
PLUGIN = ROOT / "plugins" / NAME


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"ERROR: {message}")


marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
manifest = json.loads((PLUGIN / ".codex-plugin/plugin.json").read_text())
entry = marketplace["plugins"][0]

require(marketplace["name"] == NAME, "unexpected marketplace name")
require(entry["name"] == NAME, "unexpected marketplace entry")
require(entry["source"] == {"source": "local", "path": f"./plugins/{NAME}"}, "invalid source")
require(entry["policy"] == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "invalid policy")
require("products" not in entry["policy"], "policy.products must be omitted")
require(manifest["name"] == NAME, "unexpected plugin name")
require(bool(re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?", manifest["version"])), "invalid version")

skill = PLUGIN / "skills" / NAME / "SKILL.md"
match = re.match(r"^---\n(.*?)\n---\n", skill.read_text(), re.DOTALL)
require(match is not None, "missing skill frontmatter")
frontmatter = yaml.safe_load(match.group(1))
require(frontmatter.get("name") == NAME and frontmatter.get("description"), "invalid skill frontmatter")

for path in ROOT.rglob("*"):
    require(path.name not in {".DS_Store", ".env", "id_rsa", "id_ed25519"}, f"forbidden file: {path}")

print(f"OK: {NAME} {manifest['version']}")
