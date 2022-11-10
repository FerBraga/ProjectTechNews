import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):

    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):

    selector = Selector(html_content)

    try:
        selected = selector.css(".cs-overlay-link::attr(href)").getall()
        return selected
    except Exception:
        return []


# Requisito 3
def scrape_next_page_link(html_content):

    link_page = Selector(html_content)

    while link_page:
        link_page = link_page.css("a.next::attr(href)").get()
        return link_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
