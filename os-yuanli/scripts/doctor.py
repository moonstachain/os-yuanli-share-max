#!/usr/bin/env python3
"""Static consistency checks for the os-yuanli skill."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "skills"
SKILL_MD = ROOT / "SKILL.md"
OPENAI_YAML = ROOT / "agents/openai.yaml"
REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / ".gitignore",
    OPENAI_YAML,
    ROOT / "references/constitution.md",
    ROOT / "references/task-family-map.md",
    ROOT / "references/routing-bridges.md",
    ROOT / "references/output-contract.md",
    ROOT / "references/integration-boundaries.md",
    ROOT / "references/audit-rubric.md",
    ROOT / "references/system-audit-playbook.md",
    ROOT / "references/system-audit-feishu-loop.md",
    ROOT / "scripts/doctor.py",
]
REQUIRED_SUBSKILLS = [
    "intent-grounding",
    "skill-router",
    "jiyao-youyao-haiyao-zaiyao",
    "evidence-gate",
    "closure-evolution",
    "wechat-style-profiler",
    "wechat-topic-outline-planner",
    "wechat-draft-writer",
    "wechat-title-generator",
    "wechat-article-writer",
]
REQUIRED_SKILL_TOKENS = [
    "OS-原力",
    "原力OS",
    "治理OS",
    "工作OS",
    "主题层",
    "策略层",
    "执行层",
    "full mode",
    "light mode",
    "system audits",
]
REQUIRED_FAMILIES = [
    "内容生产",
    "研究审计",
    "工作流自动化",
    "接线部署",
    "治理协作",
    "未知或混合任务",
]
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def check_exists(path: Path, errors: list[str]) -> None:
    if not path.exists():
        errors.append(f"missing: {path}")


def resolve_link(source: Path, target: str) -> Path | None:
    if target.startswith("http://") or target.startswith("https://"):
        return None
    if target.startswith("#"):
        return None
    if target.startswith("/"):
        return Path(target)
    return (source.parent / target).resolve()


def check_markdown_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for target in MARKDOWN_LINK_RE.findall(text):
        resolved = resolve_link(path, target)
        if resolved is None:
            continue
        if not resolved.exists():
            errors.append(f"broken link in {path}: {target} -> {resolved}")


def check_required_tokens(path: Path, tokens: list[str], errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for token in tokens:
        if token not in text:
            errors.append(f"missing token in {path}: {token}")


def check_openai_yaml(path: Path, errors: list[str]) -> None:
    if not path.exists():
        return
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        errors.append(f"invalid yaml object: {path}")
        return
    interface = data.get("interface")
    if not isinstance(interface, dict):
        errors.append(f"missing interface block: {path}")
        return
    if interface.get("display_name") != "OS-原力":
        errors.append(f"display_name mismatch in {path}")
    if "default_prompt" not in interface:
        errors.append(f"missing default_prompt in {path}")
    short_description = interface.get("short_description", "")
    if not isinstance(short_description, str) or not (25 <= len(short_description) <= 64):
        errors.append(f"invalid short_description length in {path}")
    policy = data.get("policy")
    if not isinstance(policy, dict) or policy.get("allow_implicit_invocation") is not False:
        errors.append(f"allow_implicit_invocation must be false in {path}")


def main() -> int:
    errors: list[str] = []

    check_exists(ROOT, errors)
    check_exists(SKILL_MD, errors)
    for item in REQUIRED_FILES:
        check_exists(item, errors)

    for name in REQUIRED_SUBSKILLS:
        check_exists(SKILLS_ROOT / name / "SKILL.md", errors)

    if SKILL_MD.exists():
        check_markdown_links(SKILL_MD, errors)
        check_required_tokens(SKILL_MD, REQUIRED_SKILL_TOKENS, errors)

    for item in REQUIRED_FILES:
        if item.suffix == ".md" and item.exists():
            check_markdown_links(item, errors)

    family_map = ROOT / "references/task-family-map.md"
    if family_map.exists():
        check_required_tokens(family_map, REQUIRED_FAMILIES, errors)

    check_openai_yaml(OPENAI_YAML, errors)

    if errors:
        print("FAILED")
        for item in errors:
            print(f"- {item}")
        return 1

    print("OK")
    print(f"root: {ROOT}")
    print(f"skills_root: {SKILLS_ROOT}")
    print(f"required_subskills: {len(REQUIRED_SUBSKILLS)}")
    print(f"required_families: {len(REQUIRED_FAMILIES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
