import os
import requests
import re
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

BASE_URL = "https://www.mytween.io/"
OUTPUT_DIR = "."

def download_file(url, local_path):
    if os.path.exists(local_path):
        return
    try:
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            with open(local_path, 'wb') as f:
                f.write(r.content)
            print(f"Downloaded: {url}")
        else:
            print(f"Failed to download {url}: {r.status_code}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def scrape_site():
    print(f"Scraping {BASE_URL}...")
    r = requests.get(BASE_URL, headers={'User-Agent': 'Mozilla/5.0'})
    html = r.text
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    soup = BeautifulSoup(html, 'html.parser')
    
    assets = set()
    for tag in soup.find_all(['script', 'link', 'img']):
        url = tag.get('src') or tag.get('href')
        if url:
            if url.startswith('/'):
                assets.add(url)
            elif url.startswith('http') and BASE_URL in url:
                path = urlparse(url).path
                assets.add(path)

    # Specific extra files
    assets.update(['/manifest.webmanifest', '/icon.png?e6a62d6534c77576', '/apple-icon.png?c53c68c11c533036'])

    for asset in assets:
        clean_path = asset.split('?')[0] # remove query string for saving
        if clean_path == '/':
            continue
            
        full_url = urljoin(BASE_URL, asset)
        local_path = os.path.join(OUTPUT_DIR, clean_path.lstrip('/'))
        download_file(full_url, local_path)
        
    print("Scraping completed.")

if __name__ == "__main__":
    scrape_site()
