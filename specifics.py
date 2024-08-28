import re
import json
import rdkit as Chem
from rdkit.Chem import GraphDescriptors

def break_reaction_conditions(text):
    # Adjusted regex to split by periods that are not followed by a word boundary after "eg."
    split_text = re.split(r'(?<!\beg)\.(?!\s)', text)
    # Remove any leading or trailing whitespace from the results
    split_text = [s.strip() for s in split_text if s]
    return split_text
def parse_doi_links(complete_references):
    # Regex to match DOI and corresponding link
    pattern = r'\[(.*?)\]:\s(https://doi\.org/\S+)'
    # Find all matches
    reference_list = re.findall(pattern, complete_references)
    # Create the output list of dictionaries
    references = [{"doi": doi, "link": link} for doi, link in reference_list]
    return references
def parse_reaction_smiles(reaction_smile_string):
    # Split reactants and products using '>>'
    reactants_str, products_str = reaction_smile_string.split('>>')
    
    # Further split the reactants and products by '.'
    reactants = reactants_str.split('.')
    products = products_str.split('.')
    
    # Create the output dictionary
    # output = {
    #     "reactants": {
    #         "smiles": [r.strip() for r in reactants]  # Strip any leading/trailing spaces
    #     },
    #     "products": {
    #         "smiles": [p.strip() for p in products]  # Strip any leading/trailing spaces
    #     }
    # }
    
    return reactants,products
def check():
    bipycu = Chem.MolFromSmiles('c1cccn->2c1-c1n->3cccc1.[Cu]23(Cl)Cl')
    bipycu.GetBondBetweenAtoms(4,12).GetBondType()
    rdkit.Chem.rdchem.BondType.DATIVE
    Chem.MolToSmiles(bipycu)
    
check()