import requests
def is_valid_subdomain(subdomain):
    url = f"http://{subdomain}"  
    try:
        response = requests.get(url)
        return response.status_code in [200]  
    except requests.RequestException:
        return False
def filter_valid_subdomains(filename):
    valid_subdomains = []
    with open(filename, 'r') as file:
        for line in file:
            subdomain = line.strip()
            if is_valid_subdomain(subdomain):
                valid_subdomains.append(subdomain)
    return valid_subdomains
# Usage
filename = input("enter the textFile name:")
valid_subdomains = filter_valid_subdomains(filename)
for subdomain in valid_subdomains:
    print(subdomain)
