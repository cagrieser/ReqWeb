import argparse
import requests
from termcolor import colored

def fetch_content(url, payload):
    response = requests.get(url)
    if response.status_code == 200:
        print(colored("Website Headers:", "red"))
        headers = response.headers
        for header, value in headers.items():
            print(f"{header}: {value}")
        print("\n")
        content = response.text
        print(colored("Payload:", "blue"), colored(payload, "red"))
        print("\n")
        return content
    else:
        return None

def main():
    parser = argparse.ArgumentParser(description='Fetch content from URLs')
    parser.add_argument('--wordlist', required=True, help='Path to the wordlist file containing payloads')
    parser.add_argument('--url', required=True, help='URLs to fetch content from')
    args = parser.parse_args()

    with open(args.wordlist, 'r') as file:
        payloads = file.read().splitlines()

    if payloads:
        for payload in payloads:
            url = args.url + payload
            content = fetch_content(url, payload)
            if content:
                print(f"URL: {url}\nContent: {content}\n")
            else:
                print(f"Failed to fetch content from URL: {url}\n")
    else:
        print("No payloads found in the wordlist file.")

if __name__ == "__main__":
    main()
