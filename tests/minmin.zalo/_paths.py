"""Paths for the code-pack tests of minmin.zalo, and server/ of MinMin OS on sys.path.

The plugins in this pack run INSIDE a MinMin OS server and import its modules (`zalo_cli`, `image_gen`,
`image_vision`, `conversations`), so their tests need a MinMin OS checkout next to this repo. CI clones it;
locally point MINMIN_OS_DIR at yours (default: ../minmin-os next to this repo).

    MINMIN_OS_DIR=/path/to/minmin-os python tests/minmin.zalo/test_zalo_read_images.py
"""
import os
import sys
from pathlib import Path

STORE = Path(__file__).resolve().parents[2]
PACK = STORE / "packs" / "minmin.zalo"
ROOT = Path(os.environ.get("MINMIN_OS_DIR") or (STORE.parent / "minmin-os")).resolve()
SERVER = ROOT / "server"
if not (SERVER / "zalo_cli.py").is_file():
    raise SystemExit(f"MinMin OS checkout not found at {ROOT} (set MINMIN_OS_DIR)")
if str(SERVER) not in sys.path:
    sys.path.insert(0, str(SERVER))
