import requests
import socket

def get_ip_info(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]

        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url)
        data = response.json()

        isp = data.get('org', 'N/A')
        reverse_dns = data.get('hostname', 'N/A')
        country = data.get('country', 'N/A')

        print(f"IP Address: {ip_address}")
        print(f"Hostname: {hostname}")
        print(f"ISP: {isp}")
        print(f"Reverse DNS: {reverse_dns}")
        print(f"Country: {country}")

    except socket.herror as e:
        print(f"Error performing reverse IP lookup: {e}")
    except requests.RequestException as e:
        print(f"Error accessing IP information: {e}")

if __name__ == '__main__':
    user_ip = input("Enter an IP address: ")

    get_ip_info(user_ip)
