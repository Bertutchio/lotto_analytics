# coding: utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch

years = [
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
]

es = Elasticsearch()

for year in years:
    # specify the url
    quote_page = 'http://www.tirage-euromillions.net/euromillions/annees/annee-'+ str(year) +'/'

    # query the website and return the html to the variable ‘page’
    # TODO: check query is OK
    page = urlopen(quote_page)

    soup = BeautifulSoup(page, 'html.parser')

    for tr in soup.select('tr'):
        i = 1
        for td in tr.select('td'):
            # TODO: make a switch
            doc = {}
            value = td.string
            if i == 1:
                date = value.split()
                doc['date'] = date
            if i == 2:
                doc['number_1'] = int(value)
            if i == 3:
                doc['number_2'] = int(value)
            if i == 4:
                doc['number_3'] = int(value)
            if i == 5:
                doc['number_4'] = int(value)
            if i == 6:
                doc['number_5'] = int(value)
            if i == 7:
                doc['star_1'] = int(value)
            if i == 8:
                doc['star_2'] = int(value)
            elif i == 9:
                doc['number_of_winners'] = int(value)
            elif i == 10:
                doc['amount'] = int(value.strip('EUR').replace(' ', ''))
            i = i + 1
