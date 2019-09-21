import json
import urllib.request, urllib.parse, urllib.error
import sqlite3

conn = sqlite3.connect('day3.db')
cur = conn.cursor()
sql = '''CREATE TABLE IF NOT EXISTS docs (
id VARCHAR PRIMARY_KEY NOT_NULL, 
journal VARCHAR(255), 
eissn VARCHAR(255), 
publication_date VARCHAR(255), 
article_type VARCHAR(255),
author_display VARCHAR(255),
abstract VARCHAR(255)
)'''
cur.execute(sql)

url = 'http://api.plos.org/search?q=title:KOREA'
soup = urllib.request.urlopen(url).read()
info = json.loads(soup)
jsonData = info['response']['docs']

sql = "INSERT INTO docs (id,journal,eissn,publication_date,article_type,author_display,abstract) VALUES (?,?,?,?,?,?,?)"

for val in jsonData:
    authorDisplay = ''.join(val['author_display'])
    abstract = ''.join(val['abstract'])
    infoList = [(val['id'], val['journal'], val['eissn'], val['publication_date'], val['article_type'], authorDisplay, abstract)]
    cur.executemany(sql, infoList)
    conn.commit()
