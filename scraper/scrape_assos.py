
import requests
from bs4 import BeautifulSoup
import re
import csv

def extract_emails_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        emails = list(set(re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)))
        return emails
    except Exception as e:
        print(f"[!] Erreur lors du scrap de {url}: {e}")
        return []

def save_to_csv(rows, path='data/contacts.csv'):
    with open(path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Nom', 'Email', 'Source'])
        writer.writerows(rows)

def scrape_sites():
    urls = [
        "https://exemple-association1.fr",
        "https://exemple-association2.fr"
    ]
    contacts = []
    for url in urls:
        emails = extract_emails_from_url(url)
        for email in emails:
            name = email.split("@")[0]
            contacts.append([name.capitalize(), email, url])
    save_to_csv(contacts)
    print(f"[✓] {len(contacts)} contacts sauvegardés.")
