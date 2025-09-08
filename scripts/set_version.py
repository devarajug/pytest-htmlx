import re
import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent 
if len(sys.argv) != 2:
    print("Usage: python scripts/set_version.py vX.Y.Z")
    sys.exit(1)

tag = sys.argv[1]  # e.g. v0.5.0
if not tag.startswith("v"):
    raise RuntimeError("Tag must start with 'v', e.g. v1.2.3")

new_version = tag.lstrip("v")

version_file = root_dir / "pytest_htmlx" / "__init__.py"
text = version_file.read_text()

new_text = re.sub(r'__version__ = ".+"', f'__version__ = "{new_version}"', text)
version_file.write_text(new_text)

print(f"Updated version to {new_version}")
