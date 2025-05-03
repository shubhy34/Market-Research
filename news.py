import requests
import os
from dotenv import load_dotenv

load_dotenv()
SERP_API_KEY = os.getenv('SERP_API_KEY')

def fetch_company_news(query):
    url = f"https://serpapi.com/search.json?q={query}&tbm=nws&api_key={SERP_API_KEY}"
    res = requests.get(url)
    if res.status_code == 200:
        articles = res.json().get("news_results", [])
        return [{'title': a['title'], 'link': a['link']} for a in articles]
    return []
