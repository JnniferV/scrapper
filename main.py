
from scraper.scrape_assos import scrape_sites
from emailer.send_email import send_email
import csv

def run():
    scrape_sites()
    with open("data/contacts.csv", newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            send_email(row['Email'], row['Nom'])

if __name__ == "__main__":
    run()
