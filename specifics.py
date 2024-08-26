import re
def break_references(text):

    # Adjusted regex to split by periods that are not followed by a word boundary after "eg."
    split_text = re.split(r'(?<!\beg)\.(?!\s)', text)

    # Remove any leading or trailing whitespace from the results
    split_text = [s.strip() for s in split_text if s]
    return split_text

