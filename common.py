import os


def read_file(file_path):

    if not os.path.exists(file_path):
        return "File not found."

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except IOError:
        return "Error reading file."


def extract_rdf_elements(content, file_path):

    if content == "File not found.":
        return "File not found."

    if content == "Error reading file.":
        return "Error reading file."

    content = content.split('\n')
    date_time = content[1].split(',')[1].strip()
    output = {}
    output["date"] = f"Date: {date_time}"
    output["time"] = f"Time: {date_time}"
    output["filename"] = file_path
    return output


def extract_reaction_elements(reaction_data):
    content = reaction_data.split('\n')
    reactant_products_data = content[4]
    out = {}
    out["number_of_reactants"] = capture_digits(reactant_products_data)[0]
    out["number_of_products"] = capture_digits(reactant_products_data)[1]
    return out


def capture_digits(text_with_strings):
    # Strip any leading/trailing whitespace and split the data string by any whitespace
    digits = text_with_strings.strip().split()

    # Convert the split string elements to integers
    first_number = int(digits[0])
    second_number = int(digits[1])

    return first_number, second_number


def extract_repeat_elements(text, break_string, type_of_break, start, number_of_elemnts):
    data = text.split(break_string)[start:start+number_of_elemnts]
    data = [x.strip() for x in data]
    if type_of_break == "header":
        data = [break_string+"\n"+x for x in data]
    if type_of_break == "footer":
        data = [x+"\n"+break_string for x in data]

    return data


if __name__ == '__main__':
    FILE_PATH = "sample.rdf"
    sample_data = read_file(FILE_PATH)
    extract_rdf_elements(sample_data,FILE_PATH)
