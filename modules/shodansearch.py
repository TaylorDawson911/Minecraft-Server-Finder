import shodan
import json
import os

def shodan_search(api_key, output_filename, version, additional_search):
    # Shodan API key (replace with your own API key)
    api = shodan.Shodan(api_key)

    if additional_search is None:
        additional_search = ""
        

    def export_to_json(data, file_path):
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    try:
        # Search Shodan
        results = api.search(f'product:minecraft version:{version} {additional_search}')

        # Add "whitelist": "n/a" to each server
        for server in results['matches']:
            server['whitelist'] = "n/a"

        # Construct the full path to the output file in the serverlists directory
        output_file_path = os.path.join("..", "serverlists", f"{output_filename}.json")

        script_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(script_directory)
        serverlists_directory = os.path.join(parent_directory, "serverlists")

        output_file_path = os.path.join(serverlists_directory, f"{output_filename}.json")



        # Save the result to a json file in the serverlists directory
        export_to_json(results, output_file_path)
    except shodan.APIError as e:
        print('Error: {}'.format(e))
        return "Shodan API error"

    return "Success"
