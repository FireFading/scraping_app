import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import lxml

from .models import News

@shared_task
def hackernews_rss():
    article_list = []
    try:
        print('Starting scraping')
        r = requests.get('https://news.ycombinator.com/rss')
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')

        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            published_wrong = a.find('pubDate').text
            published = datetime.strptime(published_wrong, '%a, %d %b %Y %H:%M:%S %z')
            article = {
                'title': title,
                'link': link,
                'published': published,
                'source': 'HackerNews RSS'
            }
            article_list.append(article)
            print('Finished scraping the articles')
    
            return save_function(article_list)
        
    except Exception as e:
        print('Scraping failed')
        print(e)
        
        
@shared_task(serializer='json')
def save_function(article_list):
    print('starting')
    new_count = 0

    for article in article_list:
        try:
            News.objects.create(
                title = article['title'],
                link = article['link'],
                published = article['published'],
                source = article['source']
            )
            new_count += 1
        except Exception as e:
            print('failed at latest_article is none')
            print(e)
            break
    return print('finished')