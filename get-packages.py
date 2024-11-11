import requests
import sys
from pathlib import Path

OUTPUT_PATH="packages"

s = requests.Session()

releases = s.get(f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/releases").json()

Path(OUTPUT_PATH).mkdir(parents=True, exist_ok=True)

for release in releases:
    # release['name']
    for asset in release['assets']:
        if str(asset['name']).endswith(".deb"):
            file = s.get(asset['browser_download_url'], allow_redirects=True)
            open(f"{OUTPUT_PATH}/{asset['name']}", "wb").write(file.content)
            print(f"Downloaded {asset['name']}")