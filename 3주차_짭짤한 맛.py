from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.spartadb

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
            }

response_data = requests.get("https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713", headers=headers)
soup = BeautifulSoup(response_data.text, 'html.parser')


my_list = soup.select("#body-content > div.newest-list > div > table > tbody > tr")

for num in my_list:
    rank = num.select_one("td.number").text[0:2].strip()
    title = num.select_one("td.info > a.title").text.strip()
    singer = num.select_one("td.info > a.artist").text
    print(rank, title, singer)

    doc = {
        'rank' : rank,
        'title' : title,
        'singer' : singer
    }

    db.task02.insert_one(doc)




