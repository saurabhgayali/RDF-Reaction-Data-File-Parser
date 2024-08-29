import os
import json
from flask import Flask, jsonify, abort


app = Flask(__name__)

JSON_DIRECTORY = 'json'


def load_json_data(json_filename):
    """
    Load JSON data from the specified file.
    """
    json_file_path = os.path.join(JSON_DIRECTORY, f"{json_filename}.json")
    if not os.path.exists(json_file_path):
        return None
    try:
        with open(json_file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        return None


def get_nested_data(data, keys):
    """
    Recursively retrieve data from nested JSON structure based on keys.
    """
    for key in keys:
        if isinstance(data, list):
            try:
                key = int(key)
            except ValueError:
                abort(404, description="Invalid key for list index")
        try:
            data = data[key]
        except (KeyError, IndexError, TypeError):
            abort(404, description="Key not found")
    return data


@app.route('/<json_filename>/', defaults={'path': ''}, methods=['GET'])
@app.route('/<json_filename>/<path:path>', methods=['GET'])
def load_json_route(json_filename, path):
    """
    Load the specified JSON file and return the requested data based on the path.
    """
    data = load_json_data(json_filename)
    if data is None:
        abort(404, description="JSON file not found")

    if path:
        keys = path.split('/')
        data = get_nested_data(data, keys)

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
