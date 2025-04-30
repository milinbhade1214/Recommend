import os
import zipfile
import urllib.request

url = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
dest = "data/ml-latest-small.zip"
extract_path = "../data"

os.makedirs("../data", exist_ok=True)

if not os.path.exists(dest):
    print("Downloading MovieLens data...")
    urllib.request.urlretrieve(url, dest)

with zipfile.ZipFile(dest, "r") as zip_ref:
    zip_ref.extractall(extract_path)

print("Dataset downloaded and extracted.")