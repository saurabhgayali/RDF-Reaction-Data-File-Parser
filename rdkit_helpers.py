from rdkit import Chem

def smiles_to_mol(smiles_str):
    """
    Convert a SMILES string to an RDKit molecule object.
    """
    mol = Chem.MolFromSmiles(smiles_str)
    
    # Print more detailed mol data
    if mol is not None:
        print("MOL block representation:")
        print(Chem.MolToMolBlock(mol))  # MOL block representation
        print("Number of atoms in the molecule:", mol.GetNumAtoms())  # Number of atoms
    else:
        print("Invalid SMILES string")
    
    return mol

def mol_to_smiles(mol):
    """
    Convert an RDKit molecule object to a SMILES string.
    """
    if mol is not None:
        smiles = Chem.MolToSmiles(mol)
        return smiles
    else:
        return None

# Example usage
smiles_string = 'Cc1ccccc1C'
mol = smiles_to_mol(smiles_string)
print("Converted SMILES:", mol_to_smiles(mol))
