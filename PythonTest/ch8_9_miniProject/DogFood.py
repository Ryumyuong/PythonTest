import time
import bs4
import urllib.request
import ssl
import pymysql
from tkinter import *
import re

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
link,title,subject, company, pTime= "","","","", ""

null = None
## 함수 선언 부분
def insertData(link,title, subject, company, pTime) :
    con, cur = None, None
    data1, data2, data3, data4, data5= "", "", "", "", ""
    sql=""

    con = pymysql.connect(host='127.0.0.1', user='root', password='mysql', database='gameNews', charset='utf8')
    cur = con.cursor()
    data1 = link 
    data2 = title 
    data3 = subject
    data4 = company
    data5 = pTime
    
    try :
        print(data1)
        print(data2)
        print(data3)
        print(data4)
        print(data5)
        sql = "INSERT INTO gameTable (link,title, subject, company, pTime)  VALUES('"+ data1 + "','" + data2 + "','" + data3 + "','" + data4 + "','" + data5 +"')"
        cur.execute(sql)
        
    except :
        print("예외 발생")
    else :
        print("성공")

    con.commit()
    con.close()

def remove_special_characters(sentence):
    # 정규 표현식을 사용하여 특수 문자 제거
    pattern = r'[^a-zA-Z0-9가-힣\s]'  # 영문자, 숫자, 한글, 공백을 제외한 문자 패턴
    sentence = re.sub(pattern, '', sentence)
    return sentence

num = 1
nateUrl = "https://news.daum.net/breakingnews/digital?page="
while True :
    Url = nateUrl + str(num)
    num += 1
    htmlObject = urllib.request.urlopen(Url,context=ssl_context)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
    tag_list = bsObject.findAll('div', {'class': 'cont_thumb'})
    print('###### 실시간 뉴스 속보 #######')
    
    for tag in tag_list :

        link = tag.find('a', {'class': 'link_txt'})['href']
        link = 'https:' + link
        print("link : " + link)
        title = tag.find('a', {'class': 'link_txt'}).text
        print("title : " + title)
        if tag.find('span', {'class': 'link_txt'}) != None :
            subject = tag.find('span', {'class': 'link_txt'}).text.strip()
            subject = remove_special_characters(subject)
        else :
            continue
        print("subject1 : " + subject)
        if tag.find('span', {'class': 'info_news'}) != None :
            news = tag.find('span', {'class': 'info_news'}).text
            news.replace('\t',' ')
            news.replace('\n', '')
            if len(news.split()) == 3 :
                company, pDate, pTime = news.split()
            else :
                continue
        else :
            continue
        print("company : " + company)
        print("pDate : " + pDate)
        print("pTime : " + pTime)
        
        insertData(link,title, subject, company, pTime)

    time.sleep(20)