import json
import helpers as helper_tasks
import common as common_tasks
import specifics as specific_tasks
import rdkit_helpers as rdkit_tasks

MAX_REACTION_PER_FILE = 15
'''variables for parsing datum data. key is name in rdf file while value will be key in json'''
datum_variables = {"Name": "reaction_name", "Reference": "references",
                   "Reaction_Conditions": "reaction_conditions",
                   "SMILES": "reaction_smile", "Protections": "protections",
                   "Inventory": "inventory"}


def main(input_name, output_name):
    rdf_content = helper_tasks.read_file(input_name)
    rdf_content_parsed = common_tasks.extract_rdf_elements(
        rdf_content, input_name)

    reaction_elements = common_tasks.extract_repeat_elements(
        rdf_content, "$RXN", "header", 1, MAX_REACTION_PER_FILE)

    reaction_parameters = []
    reaction_id = 1
    for single_reaction in reaction_elements:
        reactant_product_info = single_reaction.split('\n')[3]
        no_of_reactants, no_of_products = common_tasks.capture_digits(
            reactant_product_info)

        reaction_numbers = {
            'id': str(reaction_id),
            "number_of_reactants": no_of_reactants,
            "number_of_products": no_of_products
        }

        reaction_datum_data = common_tasks.parse_datum_data(
            single_reaction, datum_variables)

        reaction_datum_data["reaction_conditions"] = specific_tasks.break_reaction_conditions(
            reaction_datum_data["reaction_conditions"])
        reaction_datum_data["references"] = specific_tasks.parse_doi_links(
            reaction_datum_data["references"])

        reaction_level2_data = {}
        reaction_level2_data["reactants"] = {}
        reaction_level2_data["products"] = {}
        (
            reaction_level2_data["reactants"]["smiles"],
            reaction_level2_data["products"]["smiles"],
        ) = specific_tasks.parse_reaction_smiles(
            reaction_datum_data["reaction_smile"]
        )
        reaction_level2_data["reactants"]["structure"] = []

        reaction_level2_data["products"]["structure"] = []

        for smile in reaction_level2_data["reactants"]["smiles"]:
            mol = rdkit_tasks.smiles_to_mol(smile)
            if mol:
                reaction_level2_data["reactants"]["structure"].append(
                    mol)
            else:

                print(f"Failed to convert SMILES: {smile}")

        for smile in reaction_level2_data["products"]["smiles"]:
            mol = rdkit_tasks.smiles_to_mol(smile)
            if mol:
                reaction_level2_data["products"]["structure"].append(
                    mol)
            else:

                print(f"Failed to convert SMILES: {smile}")

        combined_reaction_data = {**reaction_numbers,
                                  **reaction_datum_data, **reaction_level2_data}

        reaction_parameters.append(combined_reaction_data)

        reaction_id = reaction_id+1

    rdf_content_parsed["reactions"] = reaction_parameters

    print(helper_tasks.write_to_file(json.dumps(
        rdf_content_parsed, indent=4), output_name))


if __name__ == '__main__':
    input_name = "sample.rdf"
    output_name = "sample.json"
    main(input_name, output_name)
