import bs4

webPage = open('PythonTest/HTML/Sample02.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag_li_all= bsObject.findAll('li')
for tag_li in tag_li_all :
    print(tag_li)
    # 값만 추출하려면 text추가
    print(tag_li.text)
print()
for i in range(len(tag_li_all)) :
    print(tag_li_all[i].text)