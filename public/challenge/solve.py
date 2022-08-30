import pathlib
import json

path = pathlib.Path("content/challenge/puzzle-03/message.json")
data = json.loads(path.read_text())

max_j = max([d['j'] for d in data]) + 1
max_i = max([d['i'] for d in data]) + 1

msg = [[" " for i in range(max_j)] for j in range(max_i)]
for d in data:
    msg[d['i']][d['j']] = d['value']

print("\n".join(["".join(r) for r in msg]))
