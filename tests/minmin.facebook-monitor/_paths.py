"""Paths for the code-pack tests of minmin.facebook-monitor, and server/ of MinMin OS on sys.path.

The plugin in this pack runs INSIDE a MinMin OS server and imports its modules (`mcp_store`), so its tests need a
MinMin OS checkout next to this repo. CI clones it; locally point MINMIN_OS_DIR at yours (default: ../minmin-os next
to this repo).

    MINMIN_OS_DIR=/path/to/minmin-os python tests/minmin.facebook-monitor/test_fb_monitor.py
"""
import os
import sys
from pathlib import Path

STORE = Path(__file__).resolve().parents[2]
PACK = STORE / "packs" / "minmin.facebook-monitor"
ROOT = Path(os.environ.get("MINMIN_OS_DIR") or (STORE.parent / "minmin-os")).resolve()
SERVER = ROOT / "server"
if not (SERVER / "mcp_store.py").is_file():
    raise SystemExit(f"MinMin OS checkout not found at {ROOT} (set MINMIN_OS_DIR)")
if str(SERVER) not in sys.path:
    sys.path.insert(0, str(SERVER))
