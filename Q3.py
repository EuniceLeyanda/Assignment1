import configparser
import json
from flask import Flask, jsonify

app = Flask(__name__)

def read_config_file(file_path):
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        return config
    except FileNotFoundError:
        print("Error: Configuration file not found.")
        return None

def extract_key_value_pairs(config):
    extracted_info = {}
    for section in config.sections():
        extracted_info[section] = dict(config.items(section))
    return extracted_info

@app.route('/get_config', methods=['GET'])
def get_config():
    config_data = read_config_file('sample_config.json')
    if config_data:
        return jsonify(config_data)
    else:
        return jsonify({'error': 'Configuration file not found'}), 404


if __name__ == "__main__":
    config_file_path = "config.ini"
    config = read_config_file(config_file_path)

    if config:
        extracted_info = extract_key_value_pairs(config)
        
        if extracted_info:
            # Convert the dictionary to JSON
            json_data = json.dumps(extracted_info, indent=2)

            # write json data into JSON file
            with open('sample_config.json', 'w') as f:
                json.dump(json_data,f)
    
    app.run(debug=True)