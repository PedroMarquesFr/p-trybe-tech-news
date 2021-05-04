from tech_news import database


def search_by_title(title):
    """Seu código deve vir aqui"""
    news = database.find_news_by_title(title)
    result = []
    for single_news in news:
        result.append((single_news["title"], single_news["url"]))
    return result


print(search_by_title("Vamos"))


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
