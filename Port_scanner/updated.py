import socket
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style

urls = []
with open('site.txt', 'r') as file:
    urls = file.read().splitlines()

with open('wordlist.txt', 'r') as ports_file:
    ports = [int(port) for port in ports_file.read().splitlines()]

def check_site_reachability(url):
    try:
        socket.gethostbyname(url)
        return True
    except socket.error:
        return False

def check_port(url, port):
    try:
        with socket.create_connection((url, port), timeout=1) as sock:  # Adjust timeout as needed
            print(f"{Fore.GREEN}Port {port} is open on {url}{Style.RESET_ALL}")
    except socket.error:
        pass

def scan_ports_for_url(url):
    if check_site_reachability(url):
        print(f"Scanning ports for {url}")
        with ThreadPoolExecutor(max_workers=10) as executor:  # Set the number of threads as needed
            executor.map(check_port, [url] * len(ports), ports)
    else:
        print(f"{Fore.RED}Site {url} is unreachable{Style.RESET_ALL}")

with ThreadPoolExecutor() as executor:
    executor.map(scan_ports_for_url, urls)

