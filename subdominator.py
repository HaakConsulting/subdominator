import requests
import argparse
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup

INTERESTING_KEYWORDS = ['login', 'admin', 'dashboard', 'panel', 'api', '.env', '.git', 'config']
HEADERS = {'User-Agent': 'Mozilla/5.0 (HaakScanner)'}

def check_subdomain(subdomain):
    try:
        url = f"http://{subdomain}"
        response = requests.get(url, headers=HEADERS, timeout=5, allow_redirects=True)
        status = response.status_code

        if status in [200, 301, 302, 403, 401]:
            info = analyze_content(response.text)
            return {
                'subdomain': subdomain,
                'status': status,
                'keywords': info
            }
    except requests.RequestException:
        return None

def analyze_content(html):
    keywords_found = []
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text().lower()

    for keyword in INTERESTING_KEYWORDS:
        if keyword in text:
            keywords_found.append(keyword)

    if soup.find("form"):
        keywords_found.append("form_detected")

    return keywords_found

def load_subdomains(wordlist_path, domain):
    with open(wordlist_path, "r") as file:
        return [f"{line.strip()}.{domain}" for line in file if line.strip()]

def main(domain, wordlist, threads):
    subdomains = load_subdomains(wordlist, domain)
    print(f"[*] Checking {len(subdomains)} subdomains for activity and interesting content...")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(check_subdomain, subdomains)

    for result in results:
        if result:
            output = f"[+] {result['subdomain']} - Status: {result['status']}"
            if result['keywords']:
                output += f" | Found: {', '.join(result['keywords'])}"
            print(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Identifica subdominios activos e interesantes")
    parser.add_argument("-d", "--domain", required=True, help="Dominio objetivo (e.g. example.com)")
    parser.add_argument("-w", "--wordlist", required=True, help="Archivo con lista de subdominios")
    parser.add_argument("-t", "--threads", type=int, default=20, help="Número de hilos")

    args = parser.parse_args()
    main(args.domain, args.wordlist, args.threads)
