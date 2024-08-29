import re


def break_reaction_conditions(text):
    '''break reaction conditions using '.' and ignoring eg. in string'''
    split_text = re.split(r'(?<!\beg)\.(?!\s)', text)
    split_text = [s.strip() for s in split_text if s]
    return split_text


def parse_doi_links(complete_references):
    '''parse doi links from reference string'''
    pattern = r'\[(.*?)\]:\s(https://doi\.org/\S+)'
    reference_list = re.findall(pattern, complete_references)
    references = [{"doi": doi, "link": link} for doi, link in reference_list]
    return references


def parse_reaction_smiles(reaction_smile_string):
    '''parse reactants and products from reaction smile string'''
    reactants_str, products_str = reaction_smile_string.split('>>')
    reactants = reactants_str.split('.')
    products = products_str.split('.')
    return reactants, products
