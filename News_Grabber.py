import mechanize
from bs4 import BeautifulSoup
import datetime
from datetime import timedelta
import csv

start_date = datetime.date(2009, 12, 9)

news_file = open("news.csv", 'wb')
writer = csv.writer(news_file, delimiter=',')


def select_form(form):
  return form.attrs.get('action', None) == 'http://www.dailymirror.lk/archives'


br_url = mechanize.Browser()
br_news = mechanize.Browser()
br_url.open("http://www.dailymirror.lk/archives")
br_news.open("http://www.dailymirror.lk/archives")
response_url = br_url.response()
response_news = br_news.response()

for date in (start_date + timedelta(n) for n in range(3058)):
  try:
    print date.strftime('%Y-%m-%d')

    br_url.select_form(predicate=select_form)
    br_url.form['datefield'] = date.strftime('%Y-%m-%d')
    br_url.submit()

    soup_url = BeautifulSoup(br_url.response().read(), 'html.parser')
    div_list = soup_url.find_all('div', class_='media-left')

    for div in div_list:
      try:
        current_url = div.find_all('a')[0].get('href')
        print current_url
        br_news.open(current_url)
        response_news = br_news.response()
        soup_news = BeautifulSoup(br_news.response().read(), 'html.parser')
        writer.writerow([date.strftime('%Y-%m-%d'), div.find_all('a')[0].get('href'),
                         unicode(soup_news.find_all('h1')[0].get_text())[2:-2].encode("utf-8"), unicode(
            soup_news.find_all('div', class_="row inner-text")[0].find_all('p')[0].get_text()).encode('utf-8').replace(
            '\r', '').replace('\n', '')])
      except Exception as er:
        print er
  except Exception as e:
    print e

news_file.close();

