from tech_news.database import db


def search_by_title(title):

    response = db.news.find(
        {"title": {"$regex": title, "$options": "i"}}
    )

    title_found = [(item["title"], item["url"]) for item in response]

    return title_found


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    pass
