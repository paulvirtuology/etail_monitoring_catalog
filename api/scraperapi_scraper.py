import requests
from utils.config import SCRAPERAPI

def scrape_with_scraperapi(url: str):
    response = requests.get(f'http://api.scraperapi.com?api_key={SCRAPERAPI}&url={url}')
    return {"provider": "ScraperAPI", "data": response.content}
