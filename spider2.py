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

def pre_process_table(table):
    """
    INPUT:
        1. table - a bs4 element that contains the desired table: ie <table> ... </table>
    OUTPUT:
        a tuple of:
            1. rows - a list of table rows ie: list of <tr>...</tr> elements
            2. num_rows - number of rows in the table
            3. num_cols - number of columns in the table
    Options:
        include_td_head_count - whether to use only th or th and td to count number of columns (default: False)
    """
    for t in table:

        rows = [x for x in t:.find_all('tr')]

        num_rows = len(rows)

        # get an initial column count. Most often, this will be accurate
        num_cols = max([len(x.find_all(['th','td'])) for x in rows])

        # sometimes, the tables also contain multi-colspan headers. This accounts for that:
        header_rows_set = [x.find_all(['th', 'td']) for x in rows if len(x.find_all(['th', 'td']))>num_cols/2]

        num_cols_set = []

        for header_rows in header_rows_set:
            num_cols = 0
            for cell in header_rows:
                row_span, col_span = get_spans(cell)
                num_cols+=len([cell.getText()]*col_span)

            num_cols_set.append(num_cols)

        num_cols = max(num_cols_set)

        return (rows, num_rows, num_cols)


def get_spans(cell):
        """
        INPUT:
            1. cell - a <td>...</td> or <th>...</th> element that contains a table cell entry
        OUTPUT:
            1. a tuple with the cell's row and col spans
        """
        if cell.has_attr('rowspan'):
            rep_row = int(cell.attrs['rowspan'])
        else: # ~cell.has_attr('rowspan'):
            rep_row = 1
        if cell.has_attr('colspan'):
            rep_col = int(cell.attrs['colspan'])
        else: # ~cell.has_attr('colspan'):
            rep_col = 1

        return (rep_row, rep_col)

# def process_rows(rows, num_rows, num_cols):
#     """
#     INPUT:
#         1. rows - a list of table rows ie <tr>...</tr> elements
#     OUTPUT:
#         1. data - a Pandas dataframe with the html data in it
#     """
#     #data = pd.DataFrame(np.ones((num_rows, num_cols))*np.nan)
#     for i, row in enumerate(rows):
#         try:
#             col_stat = data.iloc[i,:][data.iloc[i,:].isnull()].index[0]
#         except IndexError:
#             print(i, row)
#
#         for j, cell in enumerate(row.find_all(['td', 'th'])):
#             rep_row, rep_col = get_spans(cell)
#
#             #print("cols {0} to {1} with rep_col={2}".format(col_stat, col_stat+rep_col, rep_col))
#             #print("\trows {0} to {1} with rep_row={2}".format(i, i+rep_row, rep_row))
#
#             #find first non-na col and fill that one
#             while any(data.iloc[i,col_stat:col_stat+rep_col].notnull()):
#                 col_stat+=1
#
#             data.iloc[i:i+rep_row,col_stat:col_stat+rep_col] = cell.getText()
#             if col_stat<data.shape[1]-1:
#                 col_stat+=rep_col

    #return data

def main(table):
    rows, num_rows, num_cols = pre_process_table(table)
    print(rows,num_rows,num_cols)
    #df = process_rows(rows, num_rows, num_cols)
    #return(df)

def starting_url():
    url = "https://en.wikipedia.org/wiki/Timeline_of_United_States_history"
    return url




resp = requests.get(starting_url())

soup = bs.BeautifulSoup(resp.text, "lxml")
tables = soup.findAll("table", class_='wikitable')

## I want table 3 or the one that contains years 2000-2018
#table = tables[3]

## run the above functions to extract the data
rows, num_rows, num_cols = pre_process_table(tables)
print (rows,num_rows,num_cols)
