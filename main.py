import helpers as helpers
import common as common
import specifics as specifics
import json
# input_filename, output_filename = helpers.load_arguments()
input_filename = "sample.rdf"
output_filename = "sample.json"
max_reaction_per_file = 15
# key is name in rdf file while value will be key in json
datum_variables = {"Name": "reaction_name","Reference": "references","Reaction_Conditions": "reaction_conditions","SMILES": "reaction_smile","Protections": "protections","Inventory": "inventory"}



def main():
    rdf_content = helpers.read_file(input_filename)
    rdf_content_parsed = common.extract_rdf_elements(rdf_content, input_filename)
    
    reaction_elements = common.extract_repeat_elements(rdf_content, "$RXN", "header", 1, max_reaction_per_file)

    reaction_parameters = []
    for single_reaction in reaction_elements:
        reactant_product_info = single_reaction.split('\n')[3]
        no_of_reactants, no_of_products = common.capture_digits(reactant_product_info)

        # Creating a dictionary with reaction numbers
        reaction_numbers = {
            "number_of_reactants": no_of_reactants,
            "number_of_products": no_of_products
        }

        # Parsing additional reaction data
        reaction_datum_data = common.parse_datum_data(single_reaction, datum_variables)

        reaction_datum_data["reaction_conditions"] = specifics.break_references(reaction_datum_data["reaction_conditions"])

        # Merging the dictionaries into a single dictionary
        combined_reaction_data = {**reaction_numbers, **reaction_datum_data}

        # Appending the combined dictionary to the reaction parameters list
        reaction_parameters.append(combined_reaction_data)

    # Adding the reaction data to the main parsed content
    rdf_content_parsed["reactions"] = reaction_parameters

    # Writing the parsed content to the output file
    print(helpers.write_to_file(json.dumps(rdf_content_parsed, indent=4), output_filename))



if __name__ == '__main__':
    input_filename = "sample.rdf"
    output_filename = "sample.json"
    main()
