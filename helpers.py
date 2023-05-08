import re

def ts_to_json(file):
    txt = ""
    with open("dex.ts") as file:
        txt = file.read()

    txt = re.sub("//.*\n", "\n", txt)
    txt = re.split("=", txt)[1]
    txt = re.sub("(\s|{)(\w+):", "\g<1>\"\g<2>\":", txt)
    txt = re.sub(",(\s*)(]|})", "\g<1>\g<2>", txt)
    txt = re.sub(";", "", txt)

    with open("dex.json", "w") as file:
        file.write(txt)
