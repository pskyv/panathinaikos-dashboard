"""Builds public/index.html from src/ and data/.
Usage: python3 build.py "<ημερομηνία ενημέρωσης>"
"""
import json, sys, pathlib
root = pathlib.Path(__file__).parent
upd = sys.argv[1] if len(sys.argv) > 1 else ''
shell = (root / 'src/shell.html').read_text()
page = (root / 'src/page.html').read_text().replace(' Η ημερομηνία κάθε ενημέρωσης φαίνεται στις Πηγές.', '')
data = {k: json.loads((root / f'data/{k}.json').read_text()) for k in ['standings', 'matches', 'players', 'conference']}
d3 = (root / 'src/d3.min.js').read_text()
html = (shell.replace('%%DATA%%', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'), 1)
             .replace('%%UPDATED%%', upd, 1)
             .replace('%%PAGE%%', page, 1)
             .replace('%%D3%%', d3, 1))
(root / 'public/index.html').write_text(html)
print('public/index.html', len(html))
