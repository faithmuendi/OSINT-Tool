import requests
import whois
import socket
import json

# Function to get WHOIS information
def get_whois(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return f"Error fetching WHOIS data: {e}"

# Function to get IP address of domain
def get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except Exception as e:
        return f"Error resolving IP: {e}"

# Function to get Shodan data (Requires API key)
def get_shodan_info(ip, shodan_api_key):
    try:
        url = f"https://api.shodan.io/shodan/host/{ip}?key={shodan_api_key}"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return f"Error fetching Shodan data: {e}"

# User Input
domain = input("Enter the domain to investigate: ")
whois_info = get_whois(domain)
ip_address = get_ip(domain)

print("\n🔎 WHOIS Information:")
print(whois_info)

print("\n🌐 IP Address:")
print(ip_address)

# Shodan API Key (Replace with yours)
SHODAN_API_KEY = "your_api_key_here"

if SHODAN_API_KEY != "your_api_key_here":
    shodan_data = get_shodan_info(ip_address, SHODAN_API_KEY)
    print("\n🔍 Shodan Info:")
    print(json.dumps(shodan_data, indent=4))
else:
    print("\n⚠️ Shodan API key missing. Skipping Shodan lookup.")
