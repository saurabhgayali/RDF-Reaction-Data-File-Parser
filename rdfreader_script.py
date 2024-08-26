from rdfreader import RDFParser

rdf_file_name = "sample.rdf"

with open(rdf_file_name, "r") as rdf_file:

    # create a RDFParser object, this is a generator that yields Reaction objects
    rdfreader = RDFParser(
        rdf_file,
        # will return None instead of raising an exception if a molecule is invalid
        except_on_invalid_molecule=False,
        # will return None instead of raising an exception if a reaction is invalid
        except_on_invalid_reaction=False,
    )
rdf_json = []
for rxn in rdfreader:
    rxn_json = {}
    rxn_json["smiles"] = rxn.smiles
    # print(rxn.properties) # a dictionary of properties extracted from the RXN record
    rxn_json["properties"] = rxn.properties
    # reactants = rxn.reactants # a list of Molecule objects
    rxn_json["reactants"] = rxn.reactants
    # products = rxn.products
    rxn_json["products"] = rxn.products
    # solvents = rxn.solvents
    rxn_json["solvents"] = rxn.solvents
    # catalysts = rxn.catalysts
    rxn_json["catalysts"] = rxn.catalysts

    # Molecule objects have several attributes, including:
    # print(reactants[0].smiles)
    # print(reactants[0].properties) # a dictionary of properties extracted from the MOL record (often empty)
    # reactants[0].rd_mol # an RDKit molecule object
    rdf_json.append(rxn_json)
    print(rxn_json)
print(rdf_json)
