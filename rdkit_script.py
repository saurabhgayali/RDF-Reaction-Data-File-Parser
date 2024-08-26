import rdkit as rdkit

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
    out=extract_rdf_elements(sample_data,FILE_PATH)
    print(out)
    