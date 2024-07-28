import requests
from bs4 import BeautifulSoup
import os
import zipfile


def scrape_dataset_urls(search_url):
    """Scrape dataset URLs from the UCI Machine Learning Repository."""
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all links to datasets
    dataset_links = soup.find_all('a', href=True)
    
    # Extract URLs
    dataset_urls = []
    for link in dataset_links:
        href = link['href']
        if href and 'datasets' in href.lower():
            dataset_urls.append('https://archive.ics.uci.edu' + href)
    
    # Debug output to check URLs
    print("Extracted dataset URLs:")
    for url in dataset_urls:
        print(url)
    
    return dataset_urls

def download_datasets(dataset_urls, download_path):
    for url in dataset_urls:
        print(f"Processing dataset URL: {url}")
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        download_link = soup.find('a', string='Data Folder')
        if download_link:
            download_url = 'https://archive.ics.uci.edu' + download_link['href']
            response = requests.get(download_url, stream=True)
            filename = os.path.basename(download_url)
            filepath = os.path.join(download_path, filename)
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            try:
                with zipfile.ZipFile(filepath, 'r') as zip_ref:
                    zip_ref.testzip()
                print(f"Downloaded dataset: {filename}")
            except zipfile.BadZipFile:
                print(f"Error: {filename} is a corrupt archive. Deleting file...")
                os.remove(filepath)

def main():
    search_url = 'https://archive.ics.uci.edu/ml/datasets.html?format=&task=&att=&area=net&numAtt=&numIns=&type=&sort=nameUp&view=table'
    dataset_urls = scrape_dataset_urls(search_url)
    
    if not dataset_urls:
        print("No datasets found.")
        return
    
    print(f"Found {len(dataset_urls)} datasets.")
    
    download_path = os.path.join('E:', 'Hackatone Project', 'NetTrafficGuard', 'data', 'raw')
    
    download_datasets(dataset_urls, download_path)

if __name__ == "__main__":
    main()