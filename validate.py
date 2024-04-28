import requests

def is_valid_subdomain(subdomain):
    url = f"http://{subdomain}"
    try:
        response = requests.get(url)
        return response.status_code in [200, 403], response.status_code
    except requests.RequestException:
        return False, None

def filter_valid_subdomains(filename):
    valid_200_subdomains = []
    valid_403_subdomains = []
    with open(filename, 'r') as file:
        for line in file:
            subdomain = line.strip()
            is_valid, status_code = is_valid_subdomain(subdomain)
            if is_valid:
                if status_code == 200:
                    valid_200_subdomains.append(subdomain)
                elif status_code == 403:
                    valid_403_subdomains.append(subdomain)
    return valid_200_subdomains, valid_403_subdomains

# Usage
filename = input("Enter the text file name:")
valid_200_subdomains, valid_403_subdomains = filter_valid_subdomains(filename)

with open("valid_200_subdomains.txt", 'w') as file:
    for subdomain in valid_200_subdomains:
        file.write(subdomain + '\n')

with open("valid_403_subdomains.txt", 'w') as file:
    for subdomain in valid_403_subdomains:
        file.write(subdomain + '\n')
