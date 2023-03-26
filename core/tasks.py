from datetime import datetime

import requests
from bs4 import BeautifulSoup
from celery import shared_task

from core.models import News


@shared_task(name="hackernews_rss")
def hackernews_rss():
    article_list = []
    print("Starting scraping")
    try:
        response = requests.get("https://news.ycombinator.com/rss")
        soup = BeautifulSoup(response.content, features="html.parser")
        articles = soup.findAll("item")

        for a in articles:
            title = a.find("title").text
            # link = a.find("link").text
            published_wrong = a.find("pubdate").text
            published = datetime.strptime(published_wrong, "%a, %d %b %Y %H:%M:%S %z")
            article = {
                "title": title,
                "link": "link",
                "published": published,
                "source": "HackerNews RSS",
            }
            article_list.append(article)

        print("Finished scraping the articles")
        print(article_list)

        save_function(article_list)

    except Exception as error:
        print("Scraping failed")
        print(error)


# @shared_task(name="save_function")
def save_function(article_list: list):
    print("starting saving articles")
    news_count = 0

    for article in article_list:
        News.objects.create(
            title=article.get("title"),
            link=article.get("link"),
            published=article.get("published"),
            source=article.get("source"),
        )
        news_count += 1
    print("finished saving articles")
    print(f"{news_count} articles saved")
    print(News.objects.all())
