import os
from os import write

mols = os.listdir("Images")
with open("json.json", "w") as json:
    molstr = str(mols)
    molstrlist = molstr.split(", ")
    molslist = "".join([i + ",\n " for i in molstrlist]).strip(",")
    json.write(molslist)
