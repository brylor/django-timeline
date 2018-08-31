#!/usr/bin/env python
from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string
from lxml import html
import sqlite3
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()


def starting_url():
    url = "https://en.wikipedia.org/wiki/Timeline_of_United_States_history"
    return url


#pageContent=requests.get('https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_judo')
#tree = html.fromstring(pageContent.content)

#goldWinners=tree.xpath('//*[@id="mw-content-text"]/table/tr/td[2]/a[1]/text()')

def get_events():
    resp = requests.get(starting_url())
    #soup = bs.BeautifulSoup(resp.text,'lxml')
    #tree = html.fromstring(resp.content)
    # year xpath
    # /html/body/div[3]/div[3]/div[4]/div/table[2]/tbody/tr[2]/td[1]
    #year = tree.xpath('//html/body/div/div/div/div/table/tbody/tr[position()>1]/td[1]/text()')
    #event = tree.xpath('///html/body/div/div/div/div/table/tbody/tr[position()>1]/td[3]/text()')
    soup = bs.BeautifulSoup(resp.text, "lxml")

    tables = soup.find_all('table', {'class':'wikitable'})
    for table in tables[1:]:
        tmp = table.find_all('tr')

        first = tmp[0]
        allRows = tmp[1:-1]
        #table.find_all('tr')[1:-1]


        #headers = [header.get_text() for header in first.find_all('th')]

        #results = [[data.get_text() for data in row.find_all('td')] for row in allRows]
        results =[]
        #<td rowspan="2">2=</td>
        # list of tuple (Level of tr, Level of td, total Count, Text Value)
        #e.g.
        #[(1, 0, 2, u'2=')]
        # (<tr> is 1 , td sequence in tr is 0, reapted 2 times , value is 2=)
        rowspan = []

        for no, tr in enumerate(allRows):
            tmp = []
            #print(no,tr)
            for td_no, data in enumerate(tr.find_all('td')):
                 #print(data.has_key("rowspan"))
                 if data.has_attr("rowspan"):
                     rowspan.append((no, td_no, int(data["rowspan"]), data.get_text()))
        print(rowspan)

        # if rowspan:
        #     for i in rowspan:
        #         # tr value of rowspan in present in 1th place in results
        #         for j in xrange(1, i[2]):
        #             #- Add value in next tr.
        #             results[i[0]+j].insert(i[1], i[3])
        # print(results)
    # The first tr contains the field names. (List comprehension)
    #headings = [th.get_text() for th in table.find("tr").find_all("th")]
    #print(table.find("tr"))
    #datasets = []
    #for row in table.find_all("tr")[1:]:

        #dataset = zip(headings, (td.get_text() for td in row.find_all("td")))

    #print(datasets)
    #print(list(events))

get_events()
#print(get_events())
