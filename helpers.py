import os
import argparse

def load_arguments():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Process input and output filenames.")

    # Add input and output filename arguments
    parser.add_argument('-i', '--input', required=True, help='Input filename')
    parser.add_argument('-o', '--output', required=True, help='Output filename')

    # Parse the arguments
    args = parser.parse_args()

    # Access the input and output filenames
    input_filename = args.input
    output_filename = args.output
    return(input_filename, output_filename)
    # # Print the filenames (for demonstration purposes)
    # print(f"Input filename: {input_filename}")
    # print(f"Output filename: {output_filename}")

def read_file(file_path):

    if not os.path.exists(file_path):
        return "File not found."

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except IOError:
        return "Error reading file."

def write_to_file(content, file_name):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"Content successfully written to {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# content = "Hello, this is a sample text."
# filename = "sample.txt"
# write_to_file(content, filename)


if __name__ == "__main__":
    input_filename, output_filename = load_arguments()
    content=read_file(input_filename)
    print(content)
