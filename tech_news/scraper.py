import requests
import re
from tech_news.database import create_news
from bs4 import BeautifulSoup
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

    page_infos = Selector(html_content)

    soup = BeautifulSoup(html_content)

    title = page_infos.css("h1::text").get()
    page_link = soup.select_one('link[rel="canonical"]')["href"]
    date_info = page_infos.css("li.meta-date::text").get()
    author = page_infos.css("span.author a::text").get()
    comments_count = len(page_infos.css("ol.comment-list").getall())
    summary = page_infos.css("div.entry-content p").get()
    tags = page_infos.css("section.post-tags ul li a::text").getall()
    category = page_infos.css("span.label::text").get()

    removing = re.compile("<.*?>")
    cleantext = re.sub(removing, "", summary).strip()

    return {
        "url": page_link,
        "title": title.replace('\xa0', ''),
        "writer": author,
        "summary": cleantext,
        "comments_count": comments_count,
        "timestamp": date_info,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    news = []
    counts = 0

    while counts < amount:
        fetch_result = fetch(url)
        news_returned = scrape_novidades(fetch_result)
        for new in news_returned:
            content = fetch(new)
            scraped_new = scrape_noticia(content)
            news.append(scraped_new)
            counts += 1
            if counts == amount:
                break

        url = scrape_next_page_link(fetch_result)

    create_news(news)
    return news
