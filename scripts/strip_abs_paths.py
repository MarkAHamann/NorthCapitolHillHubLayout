from pathlib import Path
from re import sub
map = Path(".") / "map.dxf"

dxf = map.read_text()

# Find C:/ ... /./ and replace with ./
dxf = sub("C:/.*/\.", ".", dxf)

map.write_text(dxf)
