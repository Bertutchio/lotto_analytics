# coding: utf-8

from urllib.request import urlopen
from urllib.error import URLError
from datetime import datetime
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch


def parse_line(line):

    doc = {}
    col = 1

    for td in line:
        value = td.string
        if col == 1:
            date = value.split()
            date = date[1].split('/')
            parsed_date = datetime(
                int(date[2]),
                int(date[1]),
                int(date[0])
            )
            doc['date'] = parsed_date.isoformat()
        if col == 2:
            doc['number_1'] = int(value)
        if col == 3:
            doc['number_2'] = int(value)
        if col == 4:
            doc['number_3'] = int(value)
        if col == 5:
            doc['number_4'] = int(value)
        if col == 6:
            doc['number_5'] = int(value)
        if col == 7:
            doc['star_1'] = int(value)
        if col == 8:
            doc['star_2'] = int(value)
        elif col == 9:
            doc['number_of_winners'] = int(value)
        elif col == 10:
            doc['amount_won'] = int(value.strip('EUR').replace(' ', ''))
        col = col + 1

    return doc


years = (
    2004,
    2005,
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
)

es = Elasticsearch([
    {'host': 'lotto_analytics_elasticsearch', 'port': 9200}
])

for year in years:

    print('parsing year ' + str(year))

    quote_page = 'http://www.tirage-euromillions.net/euromillions/annees/annee-' + str(year) + '/'

    try: page = urlopen(quote_page).read()
    except URLError as e:
        print(e.reason)
    except URLError as e:
        print(e.reason)

    soup = BeautifulSoup(page, 'html.parser')

    line = 1

    for tr in soup.select('tr'):

        td_list = tr.select('td')

        if line > 1 and len(td_list) > 1:
            doc = parse_line(td_list)
            es.index(index='lotto', body=doc)

        line = line + 1
