import mechanize
from bs4 import BeautifulSoup
import datetime
from datetime import timedelta
import csv


start_date = datetime.date(2011, 01, 8)

news_file = open("news_1.csv", 'wb')
writer = csv.writer(news_file, delimiter=',')

def select_form(form):
  return form.attrs.get('action', None) == 'http://www.dailymirror.lk/archives'


br_url = mechanize.Browser()
br_news = mechanize.Browser()
br_url.open("http://www.dailymirror.lk/archives")
br_news.open("http://www.dailymirror.lk/archives")
response_url = br_url.response()
response_news = br_news.response()



