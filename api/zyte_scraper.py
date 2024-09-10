import requests
from utils.config import ZYTEAPI

def scrape_with_zyte(url: str):
    headers = {'Authorization': f'Apikey {ZYTEAPI}'}
    response = requests.get(f'https://api.zyte.com/v1/url/{url}', headers=headers)
    return {"provider": "Zyte", "data": response.json()}
