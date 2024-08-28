import json
import helpers as helper_tasks
import common as common_tasks
import specifics as specific_tasks

# input_filename, output_filename = helpers.load_arguments()
# INPUT_FILENAME = "sample.rdf"
# OUTPUT_FILENAME = "sample.json"
MAX_REACTION_PER_FILE = 15
# key is name in rdf file while value will be key in json
datum_variables = {"Name": "reaction_name", "Reference": "references",
                   "Reaction_Conditions": "reaction_conditions",
                   "SMILES": "reaction_smile", "Protections": "protections",
                   "Inventory": "inventory"}


def main(input_name,output_name):
    rdf_content = helper_tasks.read_file(input_name)
    rdf_content_parsed = common_tasks.extract_rdf_elements(
        rdf_content, input_name)

    reaction_elements = common_tasks.extract_repeat_elements(
        rdf_content, "$RXN", "header", 1, MAX_REACTION_PER_FILE)

    reaction_parameters = []
    reaction_id=1
    for single_reaction in reaction_elements:
        reactant_product_info = single_reaction.split('\n')[3]
        no_of_reactants, no_of_products = common_tasks.capture_digits(
            reactant_product_info)

        # Creating a dictionary with reaction numbers
        reaction_numbers = {
            'id': str(reaction_id),
            "number_of_reactants": no_of_reactants,
            "number_of_products": no_of_products
        }

        # Parsing additional reaction data
        reaction_datum_data = common_tasks.parse_datum_data(
            single_reaction, datum_variables)
        # Breaking the references
        reaction_datum_data["reaction_conditions"] = specific_tasks.break_reaction_conditions(
            reaction_datum_data["reaction_conditions"])
        reaction_datum_data["references"] = specific_tasks.parse_doi_links(
            reaction_datum_data["references"])
        # Parsing reactants and products from reaction smile
        reaction_level2_data = {}
        reaction_level2_data["reactants"] = {}
        reaction_level2_data["products"] = {}
        (
            reaction_level2_data["reactants"]["smiles"],
            reaction_level2_data["products"]["smiles"]
        ) = specific_tasks.parse_reaction_smiles(
            reaction_datum_data["reaction_smile"]
        )
        reaction_level2_data["reactants"]["s"]
        # Merging the dictionaries into a single dictionary
        combined_reaction_data = {**reaction_numbers,
                                  **reaction_datum_data, **reaction_level2_data}

        # Appending the combined dictionary to the reaction parameters list
        reaction_parameters.append(combined_reaction_data)
        
        reaction_id=reaction_id+1
    # Adding the reaction data to the main parsed content
    rdf_content_parsed["reactions"] = reaction_parameters

    # Writing the parsed content to the output file
    print(helper_tasks.write_to_file(json.dumps(
        rdf_content_parsed, indent=4), output_name))


if __name__ == '__main__':
    input_name = "sample.rdf"
    output_name = "sample.json"
    main(input_name, output_name)
