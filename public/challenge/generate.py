import json
import pathlib

txt = """
.___________. __    __   _______     _______.  ______    __    __  .______        ______  _______
|           ||  |  |  | |   ____|   /       | /  __  \  |  |  |  | |   _  \      /      ||   ____|
`---|  |----`|  |__|  | |  |__     |   (----`|  |  |  | |  |  |  | |  |_)  |    |  ,----'|  |__
    |  |     |   __   | |   __|     \   \    |  |  |  | |  |  |  | |      /     |  |     |   __|
    |  |     |  |  |  | |  |____.----)   |   |  `--'  | |  `--'  | |  |\  \----.|  `----.|  |____
    |__|     |__|  |__| |_______|_______/     \______/   \______/  | _| `._____| \______||_______|"""

data = []
for i, line in enumerate(txt.split("\n")):
    for j, char in enumerate(line):
        if ord(char) != 32:
            data.append({"i": i, "j": j, "value": char})

pathlib.Path("content/challenge/puzzle-03/message.json").write_text(json.dumps(data))
