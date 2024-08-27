import json
import helpers as helpers
import common as common
import specifics as specifics

# input_filename, output_filename = helpers.load_arguments()
INPUT_FILENAME = "sample.rdf"
OUTPUT_FILENAME = "sample.json"
max_reaction_per_file = 15
# key is name in rdf file while value will be key in json
datum_variables = {"Name": "reaction_name", "Reference": "references",
                   "Reaction_Conditions": "reaction_conditions",
                   "SMILES": "reaction_smile", "Protections": "protections",
                   "Inventory": "inventory"}


def main():
    rdf_content = helpers.read_file(INPUT_FILENAME)
    rdf_content_parsed = common.extract_rdf_elements(
        rdf_content, INPUT_FILENAME)

    reaction_elements = common.extract_repeat_elements(
        rdf_content, "$RXN", "header", 1, max_reaction_per_file)

    reaction_parameters = []
    for single_reaction in reaction_elements:
        reactant_product_info = single_reaction.split('\n')[3]
        no_of_reactants, no_of_products = common.capture_digits(
            reactant_product_info)

        # Creating a dictionary with reaction numbers
        reaction_numbers = {
            "number_of_reactants": no_of_reactants,
            "number_of_products": no_of_products
        }

        # Parsing additional reaction data
        reaction_datum_data = common.parse_datum_data(
            single_reaction, datum_variables)
        # Breaking the references
        reaction_datum_data["reaction_conditions"] = specifics.break_reaction_conditions(
            reaction_datum_data["reaction_conditions"])
        reaction_datum_data["references"] = specifics.parse_doi_links(
            reaction_datum_data["references"])
        # Parsing reactants and products from reaction smile
        reaction_level2_data = {}
        reaction_level2_data["reactants"] = {}
        reaction_level2_data["products"] = {}
        reaction_level2_data["reactants"]["smiles"], reaction_level2_data["products"]["smiles"] = specifics.parse_reaction_smiles(reaction_datum_data["reaction_smile"])
        # Merging the dictionaries into a single dictionary
        combined_reaction_data = {**reaction_numbers,
                                  **reaction_datum_data, **reaction_level2_data}

        # Appending the combined dictionary to the reaction parameters list
        reaction_parameters.append(combined_reaction_data)

    # Adding the reaction data to the main parsed content
    rdf_content_parsed["reactions"] = reaction_parameters

    # Writing the parsed content to the output file
    print(helpers.write_to_file(json.dumps(
        rdf_content_parsed, indent=4), OUTPUT_FILENAME))


if __name__ == '__main__':
    INPUT_FILENAME = "sample.rdf"
    OUTPUT_FILENAME = "sample.json"
    main()
