import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Set Kaggle API credentials as environment variables
os.environ['KAGGLE_USERNAME'] = 'rahulkumar0014'
os.environ['KAGGLE_KEY'] = 'dec36072807110b131d09174266dcd47'

def authenticate_kaggle():
    try:
        api = KaggleApi()
        api.authenticate()
        return api
    except Exception as e:
        print(f"Failed to authenticate with Kaggle: {e}")
        raise

def kaggle_login_and_download(dataset_url, download_path):
    try:
        api = authenticate_kaggle()
        dataset = dataset_url.split('/')[-1]
        api.dataset_download_files(dataset, path=download_path, unzip=True)
        print(f"Downloaded {dataset} to {download_path}")
    except Exception as e:
        print(f"Failed to download from Kaggle: {e}")

# Example usage
dataset_url = "kaggle/dataset/url"  # Replace with actual dataset URL
download_path = "E:/Hackatone Project/NetTrafficGuard/data/raw"
kaggle_login_and_download(dataset_url, download_path)
