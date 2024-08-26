import re
def break_references(text):
    #text = "This is an example sentence. It includes e.g., Python scripts. Let's split this."
    split_text = re.split(r'(?<!\b(?:e\.g|i\.e))\.', text)
    # Remove any leading or trailing whitespace from the results
    split_text = [s.strip() for s in split_text if s]
    # print(split_text)
    return split_text