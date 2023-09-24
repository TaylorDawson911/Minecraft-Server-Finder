import socket
import random
from tqdm import tqdm
import requests
import json

def is_minecraft_server(ip):
    url = f"https://api.mcsrvstat.us/2/{ip}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            server_info = response.json()
            if 'online' in server_info and server_info['online']:
                return server_info  # Return the server information
            else:
                return None
        else:
            print(f"Failed to retrieve server info. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def generate_similar_ips(base_ip, server_amount):
    similar_ips = []
    for i in range(server_amount):
        ip_parts = base_ip.split('.')
        ip_parts[-1] = str(int(ip_parts[-1]) + i)
        similar_ips.append('.'.join(ip_parts))
    return similar_ips

def meets_filter_criteria(server_info, version):
    return server_info['version'] == version

def search_similar_minecraft_servers(base_ip, server_amount, version):
    similar_ips = generate_similar_ips(base_ip, server_amount)
    minecraft_servers = {}  # Dictionary to store Minecraft server information

    with tqdm(total=len(similar_ips)) as pbar:
        for ip in similar_ips:
            server_info = is_minecraft_server(ip)
            if server_info and meets_filter_criteria(server_info, version):
                minecraft_servers[ip] = {
                    'version': server_info.get('version', 'N/A'),
                    'motd': server_info.get('motd', {}).get('clean', 'N/A'),
                    'players': f"{server_info.get('players', {}).get('online', 'N/A')}/{server_info.get('players', {}).get('max', 'N/A')}",
                    'software': server_info.get('software', 'N/A')
                }
                
            pbar.update(1)

    return minecraft_servers

def export_to_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def similar_ip_main():
    ip = input("Enter an IP address: ")
    server_amount = 25
    version = "1.20.1"
    
    minecraft_servers = search_similar_minecraft_servers(ip, server_amount, version)

    print("Filtered Minecraft Servers Found:")
    for ip, server_info in minecraft_servers.items():
        print(f"IP: {ip}")
        print(f"Version: {server_info['version']}")
        print(f"MOTD: {server_info['motd']}")
        print(f"Players: {server_info['players']}")
        print(f"Software: {server_info['software']}")
        print("---")
    
    export_to_json(minecraft_servers, 'minecraft_servers.json')
    print("Server data exported to minecraft_servers.json")

    return