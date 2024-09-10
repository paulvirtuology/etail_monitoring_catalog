from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# API keys
SCRAPERAPI = os.getenv("SCRAPERAPI")
ZYTEAPI = os.getenv("ZYTEAPI")
OPENAIAPI = os.getenv("OPENAIAPI")
