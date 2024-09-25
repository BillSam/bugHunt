import dns.resolver
import sys

def brute_force_subdomains(domain, wordlist_file):
    with open(wordlist_file, 'r') as f:
        for line in f:
            subdomain = line.strip() + '.' + domain
            try:
                dns.resolver.resolve(subdomain, 'A')
                print(f"Found: {subdomain}")
            except dns.resolver.NXDOMAIN:
                pass

if __name__ == "__main__":
    brute_force_subdomains(sys.argv[1], sys.argv[2])