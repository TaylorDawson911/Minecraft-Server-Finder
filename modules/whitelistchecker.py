# get data from minecraft_servers.json

# Path: searchthing.py

import subprocess
import json
import os
from modules.webhook import create_webhook

debug = True


def whitelist_checker(webhook_url, filename, email):

    

    # check if filename has a .json extension
    if not filename.endswith(".json"):
        # try to add the extension
        filename = filename + ".json"


    try:
        script_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(script_directory)
        serverlists_directory = os.path.join(parent_directory, "serverlists")

        filename = serverlists_directory + "\\" + filename
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    


    def call_node_script(server_ip):
        try:
            # Run the Node.js script and capture its output
            output = subprocess.check_output(['node', 'bot.js', server_ip, email])
            # Decode the output from bytes to a string
            output_str = output.decode('utf-8').strip()
            return output_str
        except subprocess.CalledProcessError as e:
            print("Error: Node.js script returned non-zero exit code.")
            return None
        except FileNotFoundError:
            print("Error: Node.js executable 'node' not found. Make sure Node.js is installed.")
            return None
        

    debug = True

    json_data = open(filename)
    data = json.load(json_data)

    try:
        data = data['matches']
    except TypeError:
        pass



    for server in data:
        if debug:
            print(f"trying server {data.index(server) + 1} of {len(data)}")


        # get the information
        ip_str = server['ip_str']
        description = server['minecraft']['description']['text']
        players = server['minecraft']['players']['max']
        version = server['version']
        online = server['minecraft']['players']['online']
        last_pinged = server['timestamp']
        country_name = server['location']['country_name']
        try:
            favicon = server['minecraft']['favicon']
        except KeyError:
            favicon = None

        if debug:
            print(f"current ip: {ip_str}")
        # get the whitelist status
        whitelist = server['whitelist']
        # call the node.js script
        output_str = call_node_script(ip_str)
        if output_str is not None:
            if output_str == "success":
                if debug:
                    print("success")
                # change whitelist status to "no"
                server['whitelist'] = "no"
                # send a webhook
                serverPayload = {
                    'webhook_url': webhook_url,
                    'ip_str': ip_str,
                    'description': description,
                    'players': players,
                    'version': version,
                    'whitelist': whitelist,
                    'online': online,
                    'last_pinged': last_pinged,
                    'country_name': country_name,
                    'favicon': favicon
                }

                create_webhook(serverPayload)
                
            else:
                if debug:
                    print("fail")
                # change whitelist status to "yes"
                server['whitelist'] = "yes"
        else:
            if debug:
                print("fail")


    #update the json file
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)





