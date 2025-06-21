import requests
from bs4 import BeautifulSoup
import csv
import time

URL = "https://www.olx.in/items/q-car-cover"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_html(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()  
        return response.text
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch page: {e}")
        return None

def parse_listings(html):
    soup = BeautifulSoup(html, "html.parser")
    listings = []

    for item in soup.find_all("li", class_="EIR5N"):
        try:
            title = item.find("span", class_="_2tW1I")
            price = item.find("span", class_="_89yzn")
            location = item.find("span", class_="tjgMj")
            link_tag = item.find("a")

            if not (title and price and link_tag):
                continue 

            link = "https://www.olx.in" + link_tag.get("href")

            listings.append({
                "Title": title.text.strip(),
                "Price": price.text.strip(),
                "Location": location.text.strip() if location else "Not Available",
                "Link": link
            })
        except Exception as e:
            print(f"[WARNING] Skipping one listing due to parsing error: {e}")
            continue

    return listings

def save_to_csv(listings, filename="car_covers.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Title", "Price", "Location", "Link"])
        writer.writeheader()
        writer.writerows(listings)

def main():
    print("[INFO] Starting scraper for OLX Car Covers...")
    html = fetch_html(URL)

    if not html:
        print("[ERROR] Exiting due to fetch failure.")
        return

    listings = parse_listings(html)
    if listings:
        save_to_csv(listings)
        print(f"[INFO] {len(listings)} listings saved to car_covers.csv")
    else:
        print("[INFO] No listings found.")

if __name__ == "__main__":
    main()
