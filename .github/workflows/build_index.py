#!/usr/bin/env python3
import json, subprocess, re
from pathlib import Path

def git_mtime(post_file) -> int:
    try:
        timestamp = subprocess.check_output(
            ["git","log","-1","--format=%ct","--", str(post_file)],
            stderr=subprocess.DEVNULL
        ).strip()
        return int(timestamp or 0)
    except subprocess.CalledProcessError:
        return 0

def build_index(cfg_file="config.json"):
    cfg = json.loads(Path(cfg_file).read_text())
    for col in cfg.get("postColumns", []):
        d = Path(col["dir"])
        if d.is_dir():
            (d / "index.json").write_text(
                json.dumps(
                    [p.name for p in sorted(d.glob("*.md"), key=git_mtime, reverse=True)],
                    indent=2
                )
            )

if __name__ == "__main__":
    build_index()
