import requests
import sys

def query_passive_dns(domain):
    # You might need an API key for some services
    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
    headers = {"apikey": "YOUR_API_KEY"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['subdomains']

if __name__ == "__main__":
    print(query_passive_dns(sys.argv[1]))