from tech_news import database
import datetime


def search_by_title(title):
    """Seu código deve vir aqui"""
    news = database.find_news_by_title(title)
    result = []
    for single_news in news:
        result.append((single_news["title"], single_news["url"]))
    return result


def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        assert datetime.datetime.strptime(date, "%Y-%m-%d")
        news = database.search_news({"timestamp": {"$regex": date}})
        result = []
        for single_news in news:
            result.append((single_news["title"], single_news["url"]))
        return result
    except ValueError:
        raise ValueError("Data inválida")


print(search_by_date("2020-11-23"))


def search_by_source(source):
    """Seu código deve vir aqui"""
    news = database.search_news(
        {"sources": {"$elemMatch": {"$regex": source, "$options": "i"}}},
    )
    result = []
    for single_news in news:
        result.append((single_news["title"], single_news["url"]))
    return result


def search_by_category(category):
    """Seu código deve vir aqui"""
