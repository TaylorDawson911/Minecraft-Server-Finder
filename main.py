import argparse
import configparser

from modules import shodansearch, whitelistchecker

config = configparser.ConfigParser()
config.read('config.ini')


def shodan_search_main(output_filename, version, additional_search):
    result = shodansearch.shodan_search(config['shodan']['api_key'], output_filename, version, additional_search)
    if result == "Success":
        print("Shodan search completed successfully.")
    else:
        print("Shodan search failed.")
    
def whitelist_checker_main(filename):
    api = config['webhook']['url']
    email = config['bot']['email']
    whitelistchecker.whitelist_checker(api, filename,email)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple command line tool.")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Subparser for shodansearch
    shodan_parser = subparsers.add_parser('shodansearch', help='Perform Shodan search')
    shodan_parser.add_argument("-o", "--output", help="Output filename")
    shodan_parser.add_argument("-v", "--version", required=True, help="Version information")
    shodan_parser.add_argument("-s", "--additional-search", help="Additional search")

    whitelist_parser = subparsers.add_parser('whitelistchecker', help='Check whitelist status of servers')
    whitelist_parser.add_argument("-f", "--filename", required=True, help="Input filename")

    args = parser.parse_args()

    if args.command == "shodansearch":
        shodan_search_main(args.output, args.version, args.additional_search)
    elif args.command == "search":
        print("Performing search...")  # Replace with your search logic
    elif args.command == "whitelistchecker":
        whitelist_checker_main(args.filename)

    else:
        print("Invalid command. Use 'search' or 'shodansearch'.")
