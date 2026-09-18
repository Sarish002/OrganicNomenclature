import os

# Accessing files
files = os.listdir("../Images")
print(files)

# List of images
mols = [i.strip(".png") for i in files]

# The FGs
cycle = 0
benzene = 0
alcohol = 0 #
alkane = 0
alkene = 0
amides = 0 #
aldehyde = 0 #
ketone = 0 #
ester = 0 #
sulphs = 0
carboxyls = 0

# Increment the FGs
for mol in mols:
    if mol.endswith("ol"):
        alcohol += 1
    if mol.endswith("ane"):
        alkane += 1
    if mol.endswith("ene"):
        alkene += 1
    if mol.endswith("amide"):
        amides += 1
    if mol.endswith("al"):
        aldehyde += 1
    if mol.endswith("one"):
        ketone += 1
    if mol.endswith("oate"):
        ester += 1
    if mol.endswith("sulfonic acid"):
        sulphs += 1
    if mol.endswith("anoic acid"):
        carboxyls += 1
    if mol.endswith("benzene"):
        benzene += 1
    if "cyclo" in mol:
        cycle += 1

# Display
if __name__ == "__main__":
    print(len(ketone))
