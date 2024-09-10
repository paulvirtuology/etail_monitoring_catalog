import requests
from bs4 import BeautifulSoup

def scrape_with_free(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return {"provider": "Free", "data": {"title": soup.title.string}}
