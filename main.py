from fastapi import FastAPI
from api import zyte_scraper, scraperapi_scraper, free_scraper

app = FastAPI()

# Zyte scraping endpoint
@app.get("/api/use_zyte/scrape")
async def scrape_with_zyte(url: str):
    return zyte_scraper.scrape_with_zyte(url)

# ScraperAPI scraping endpoint
@app.get("/api/use_scraperapi/scrape")
async def scrape_with_scraperapi(url: str):
    return scraperapi_scraper.scrape_with_scraperapi(url)

# Free scraping solution endpoint
@app.get("/api/use_free/scrape")
async def scrape_with_free(url: str):
    return free_scraper.scrape_with_free(url)
