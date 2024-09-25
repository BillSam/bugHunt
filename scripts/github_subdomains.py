import requests
import sys

def github_search(domain):
    url = f"https://api.github.com/search/code?q='{domain}'&per_page=100"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        for item in results['items']:
            # Process and extract potential subdomains
            pass

if __name__ == "__main__":
    github_search(sys.argv[1])