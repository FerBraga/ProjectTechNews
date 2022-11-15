from tech_news.database import db
from datetime import datetime


def search_by_title(title):

    response = db.news.find({"title": {"$regex": title, "$options": "i"}})

    title_found = [(item["title"], item["url"]) for item in response]

    return title_found


# Requisito 7
def search_by_date(date):

    try:
        new_format_date = (
            datetime.strptime(date, "%Y-%m-%d").date().strftime("%d/%m/%Y")
        )
        response = db.news.find({"timestamp": new_format_date})

        titles_found = [(item["title"], item["url"]) for item in response]

        return titles_found
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):

    response = db.news.find(
        {"tags": {"$regex": tag, "$options": "i"}}
    )

    titles_found = [(item["title"], item["url"]) for item in response]

    return titles_found


# Requisito 9
def search_by_category(category):

    response = db.news.find(
        {"category": {"$regex": category, "$options": "i"}}
    )

    titles_found = [(item["title"], item["url"]) for item in response]

    return titles_found
