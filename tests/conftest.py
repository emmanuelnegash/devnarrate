import sys
from pathlib import Path

# Make the repo root importable so `from src.main import app` works in tests
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))