"""Screenshot every SVG in docs/svg into one contact sheet PNG (for eyeballing)."""
import sys, glob, os
from playwright.sync_api import sync_playwright

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pat = sys.argv[1] if len(sys.argv) > 1 else "*"
out = sys.argv[2] if len(sys.argv) > 2 else "/tmp/claude-0/sheet.png"
files = sorted(glob.glob(os.path.join(root, "docs/svg", pat + ".svg")))
html = "<html><body style='background:#ddd;font:12px sans-serif;display:flex;flex-wrap:wrap;gap:10px;width:1500px'>"
for f in files:
    html += f"<div><div>{os.path.basename(f)}</div><img src='file://{f}'></div>"
html += "</body></html>"
tmp = "/tmp/claude-0/sheet.html"
open(tmp, "w").write(html)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1520, "height": 800})
    pg.goto("file://" + tmp)
    pg.wait_for_timeout(300)
    pg.screenshot(path=out, full_page=True)
    b.close()
print(out, len(files))
