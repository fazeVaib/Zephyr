import requests
from pprint import pprint
from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


def get_articles():
    url = "https://medium.com/search?q=air%20pollution"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html5lib')
    posts = soup.findAll('div', attrs={'class': 'postArticle-content'})
    return posts
