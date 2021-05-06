from tech_news import database


def return_title_url(news):
    result = []
    for single_news in news:
        result.append((single_news["title"], single_news["url"]))
    return result


def top_5_news():
    """Seu código deve vir aqui"""
    news = database.aggregate_most_engage()
    return return_title_url(news)
    # news_with_sum = [
    #     {*el, el["shares_count"] + el["comments_count"]} for el in news
    # ]
    # print(news_with_sum)

    # if len(news) < 5:
    #     return return_title_url(news)


def top_5_categories():
    """Seu código deve vir aqui"""
    news = database.top_5_categories()
    if len(news) == 0:
        return []
    print(news)
    print([obj["categories"] for obj in news])
    return [obj["categories"] for obj in news]

