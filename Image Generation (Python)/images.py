import os
import pubchempy
import query
import bs4, requests
from rdkit import Chem
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

    # Alcohols
    while counter < 100:
        try:
            alcohol = question_maker.alcohol()
            print(alcohol)
            if Molecule(alcohol).iupac_name is not None:
                print(Molecule(alcohol).iupac_name)
                Molecule(alcohol).create_img()
                counter += 1
            else:
                pass
        except:
            pass
    counter = 0

    # Ketones
    while counter < 100:
        try:
            ketone = question_maker.ketone()
            print(ketone)
            if Molecule(ketone).iupac_name is not None:
                print(Molecule(ketone).iupac_name)
                Molecule(ketone).create_img()
                counter += 1
            else:
                pass
        except:
            pass
    counter = 0

    # Esters
    while counter < 100:
        try:
            ester = question_maker.ester()
            print(ester)
            if Molecule(ester).iupac_name is not None:
                print(Molecule(ester).iupac_name)
                Molecule(ester).create_img()
                counter += 1
            else:
                pass
        except:
            pass
    counter = 0

    # Carboxylic acids
    while counter < 100:
        try:
            carboxyl_acid = question_maker.carboxyl_acid()
            print(carboxyl_acid)
            if Molecule(carboxyl_acid).iupac_name is not None:
                print(Molecule(carboxyl_acid).iupac_name)
                Molecule(carboxyl_acid).create_img()
                counter += 1
            else:
                pass
        except:
            pass
    counter = 0

    # Aldehydes
    while counter < 100:
        try:
            aldehyde = question_maker.aldehyde()
            print(aldehyde)
            if Molecule(aldehyde).iupac_name is not None:
                print(Molecule(aldehyde).iupac_name)
                Molecule(aldehyde).create_img()
                counter += 1
            else:
                pass
        except:
            pass
    counter = 0

    # Alkanes
    while counter < 143:
        try:
            alkane = question_maker.alkane()
            print(alkane)
            if Molecule(alkane).iupac_name is not None:
                print(Molecule(alkane).iupac_name)
                Molecule(alkane).create_img()
                counter += 1
            else:
                pass
        except:
            pass
    counter =  0

    # Alkenes
    while counter < 100:
        try:
            alkene = question_maker.alkene()
            print(alkene)
            if Molecule(alkene).iupac_name is not None:
                print(Molecule(alkene).iupac_name)
                Molecule(alkene).create_img()
                counter += 1
            else:
                pass
        except:
            pass
    counter = 0

    # Halides
    while counter < 100:
        try:
            halide = question_maker.halide()
            print(halide)
            if Molecule(halide).iupac_name is not None:
                print(Molecule(halide).iupac_name)
                Molecule(halide).create_img()
                counter += 1
            else:
                pass
        except:
            pass