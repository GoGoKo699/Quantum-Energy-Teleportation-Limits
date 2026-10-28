#!/usr/bin/env python3
"""Run the finite scientific checks and optionally save their JSON report."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import platform
import subprocess
import sys

SCRIPTS = ("check_energy_information.py", "check_critical_ising.py")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write the actual run report here.")
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    reports = {}
    ok = True
    for name in SCRIPTS:
        process = subprocess.run(
            [sys.executable, str(folder / name)],
            cwd=folder.parent, capture_output=True, text=True, check=False
        )
        try:
            report = json.loads(process.stdout)
        except json.JSONDecodeError:
            report = {"ok": False, "error": "Check did not return valid JSON.",
                      "stdout": process.stdout, "stderr": process.stderr}
        if process.returncode != 0:
            report["ok"] = False
            report["exit_code"] = process.returncode
            if process.stderr:
                report["stderr"] = process.stderr
        ok = ok and report.get("ok") is True
        reports[name] = report
    result = {"ok": ok, "python_version": platform.python_version(),
              "checks": reports}
    rendered = json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
