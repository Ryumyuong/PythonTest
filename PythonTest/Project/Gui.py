import requests
import pandas as pd

i = 0
array = []
datass = set()

# REST API 엔드포인트 URL
url = 'http://localhost:8088/users'

# REST API GET 요청
response = requests.get(url)

# 응답 처리
if response.status_code == 200:
    data = response.json()
    df1 = pd.DataFrame(data)
    for columns in ['num', 'link', 'title', 'subject', 'company', 'ptime'] :
        for i in range(len(df1)) :
            df2 = df1.loc[i,'tableItems']
            df3 = df2[columns]
            array = array + [df3]
        datas = {columns : array}
        array = []
        if columns == 'num' :
            df4 = pd.DataFrame(datas)
        else :
            df4[columns] = datas[columns]
    print(df4)

    # 데이터프레임을 엑셀 파일로 저장
    df4.to_excel('C:/Temp/data.xlsx', index=False)
            
else:
    print('Error:', response.status_code)