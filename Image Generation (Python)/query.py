from random import shuffle, randint, choice

# Methyl/Ethyl/Other Attachments
def subs(adds = []) -> list:
    subs = ["(C)"] * randint(1, 3) + ["(CC)"] * randint(0, 2)
    for i in adds:
        subs.extend([i] * choice([1, 1, 1, 2]) if len(adds) == 1
                    else [i] * choice([0, 0, 0, 0, 1, 1, 1, 2]))
    return subs

# Alkanes
def alkane():
    chain = ["C"] * randint(6, 10)
    substitutes = subs()
    shuffle(substitutes)

    for i in substitutes:
        atts = i
        for i in range(20):
            index = randint(1, len(chain) - 1)
            if chain[index] == chain[index - 1] == "C":
                chain.insert(index, atts); break

    return "".join(chain)

# Alkenes
def alkene():
    chain = ["C"] * randint(6, 10)
    substitutes = subs(["="])
    shuffle(substitutes)

    for i in substitutes:
        atts = i
        for i in range(20):
            index = randint(1, len(chain) - 1)
            if chain[index] == chain[index - 1] == "C":
                chain.insert(index, atts); break

    return "".join(chain)

# Alcohols
def alcohol():
    chain = ["C"] * randint(6, 10)
    substitutes = subs(["(O)"])
    shuffle(substitutes)

    for i in substitutes:
        atts = i
        for i in range(20):
            index = randint(1, len(chain) - 1)
            if chain[index] == chain[index - 1] == "C":
                chain.insert(index, atts); break

    return "".join(chain)

# Ketones
def ketone():
    chain = ["C"] * randint(4, 7)
    substitutes = subs(["(=O)"])
    shuffle(substitutes)

    for i in substitutes:
        atts = i
        for i in range(20):
            index = randint(1, len(chain) - 1)
            if chain[index] == chain[index - 1] == "C":
                chain.insert(index, atts); break

    return "".join(chain)

# Halides
def halide():
    chain = ["C"] * randint(6, 8)
    substitutes = subs(["(Cl)", "(Br)", "(I)", "(F)"])
    shuffle(substitutes)

    for i in substitutes:
        atts = i
        for i in range(10):
            index = randint(1, len(chain) - 1)
            if chain[index] == chain[index - 1] == "C":
                chain.insert(index, atts); break

    return "".join(chain)

# Esters
def ester():
    chain = ["C"] * randint(6, 10)
    substitutes = subs(["(=O)O"])
    shuffle(substitutes)

    for i in substitutes:
        atts = i
        for i in range(20):
            index = randint(1, len(chain) - 1)
            if chain[index] == chain[index - 1] == "C":
                chain.insert(index, atts); break

    return "".join(chain)

# Carboxylic acids
def carboxyl_acid():
    chain = ["C"] * randint(6, 10)
    substitutes = subs()
    shuffle(substitutes)

    for i in substitutes:
        atts = i
        for i in range(20):
            index = randint(1, len(chain) - 1)
            if chain[index] == chain[index - 1] == "C":
                chain.insert(index, atts); break

    return "".join(chain) + "(=O)O"

# Sulfonic acids
def sulphonic_acid():
    chain = ["C"] * randint(6, 10)
    substitutes = subs()
    shuffle(substitutes)

    for i in substitutes:
        atts = i
        for i in range(20):
            index = randint(1, len(chain))
            if chain[index] == chain[index - 1] == "C":
                chain.insert(index, atts); break

    return "".join(chain) + "S(=O)(=O)O"

# Aldehydes
def aldehyde():
    chain = ["C"] * randint(6, 10)
    substitutes = subs()
    shuffle(substitutes)

    for i in substitutes:
        atts = i
        for i in range(20):
            index = randint(1, len(chain))
            if chain[index] == chain[index - 1] == "C":
                chain.insert(index, atts); break

    return "".join(chain) + "(=O)"

# Amides
def amide():
    chain = ["C"] * randint(6, 10)
    substitutes = subs()
    shuffle(substitutes)

    for i in substitutes:
        atts = i
        for i in range(20):
            index = randint(1, len(chain))
            if chain[index] == chain[index - 1] == "C":
                chain.insert(index, atts); break

    return "".join(chain) + "(=O)N"

# Mixed
def mixed():
    chain = ["C"] * randint(7, 9)
    attrs = ["(N)", "(C#N)", "(O)", "(=O)", "(=O)O", "S(=O)(=O)O", "(Br)", "(Cl)", "(I)", "(F)"]
    shuffle(attrs)
    substitutes = subs(attrs[:5])
    shuffle(substitutes)

    for i in substitutes:
        atts = i
        for i in range(20):
            index = randint(1, len(chain) - 1)
            if chain[index] == chain[index - 1] == "C":
                chain.insert(index, atts); break

    return "".join(chain) + choice(["(=O)O", "S(=O)(=O)O", "(=O)"])

# Benzene and Aralkanes
def phenyl():
    chain = ["C"] * randint(6, 10)
    substitutes = subs(["(C1=CC=CC=C1)"])
    shuffle(substitutes)

    for i in substitutes:
        atts = i
        for i in range(20):
            index = randint(1, len(chain) - 1)
            if chain[index] == chain[index - 1] == "C":
                chain.insert(index, atts);
                break

    return "".join(chain)

# Cycloalkanes
def cyclo():
    chain = ["C"] * randint(6, 10)
    substitutes = subs()
    shuffle(substitutes)

    for i in substitutes:
        atts = i
        for i in range(20):
            index = randint(1, len(chain) - 1)
            if chain[index] == chain[index - 1] == "C":
                chain.insert(index, atts); break

    return "".join(chain) + "C1" + "C" * randint(3, 6) + "C1"

