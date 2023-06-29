import bs4

webPage = open('PythonTest/HTML/Sample02.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag_ul= bsObject.find('ul')
print(tag_ul)
print()

# li태그 1개
tag_li= bsObject.find('li')
print(tag_li)
print()

# li태그 전부 리스트에 담김
tag_li_all= bsObject.findAll('li')
print(tag_li_all)