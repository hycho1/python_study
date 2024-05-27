# 코드 목적: 서비스분류코드 조회
# 작성자: 최한영
# 작성일: 2024-05-20
# 상세 설명: 투어 API의 서비스분류코드 조회

import requests
from func_def import *

url= 'http://apis.data.go.kr/B551011/KorService1/categoryCode1'

# 관광타입 ID
contentTypeId = '15'

# 대분류
cat1 = ''
# 중분류
cat2 = ''
# 소분류
cat3 = ''

params = {
    # 필수
    'serviceKey': '',
    'MobileOS':'ETC',
    'MobileApp':'AppTest',

    #선택
    'numOfRows':'10',               # 한페이지결과수
    'pageNo':'1',                   # 페이지번호
    '_type':'json',                 # 응답메세지 형식
    'contentTypeId': contentTypeId, # 관광타입 ID
    'cat1': cat1,                   # 대분류
    'cat2': cat2,                   # 중분류
    'cat3': cat3                    # 소분류
}

response = requests.get(make_url(url, params), verify=False)

if response.status_code == 200:
    print(response.text)
    make_csv(response.text, '서비스분류코드 조회','categoryCode')
else:
    print(f'Error: {response.status_code}')



