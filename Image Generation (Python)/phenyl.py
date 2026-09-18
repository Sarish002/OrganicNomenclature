import pubchempy
import query
from rdkit.Chem import MolFromSmiles, Draw


class Molecule:
    def __init__(self, smile: str):
        self.smile = smile # SMILES notation
        compound = pubchempy.get_compounds(smile, namespace="smiles")
        match = compound[0]
        self.iupac_name = match.iupac_name # IUPAC notation

    def create_img(self):
        mol_img = MolFromSmiles(self.smile) # Creating image
        Draw.MolToFile(mol_img, f"Images/{self.iupac_name}.png")

if __name__ == "__main__":
    counter = 0

    # Cyclocompounds
    while counter < 100:
        try:
            cyclo = query.cyclo()
            print(cyclo)
            if Molecule(cyclo).iupac_name is not None:
                print(Molecule(cyclo).iupac_name)
                Molecule(cyclo).create_img()
                counter += 1
            else:
                pass
        except:
            pass