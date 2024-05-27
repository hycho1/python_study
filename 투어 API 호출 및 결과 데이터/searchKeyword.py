# 코드 목적: 키워드검색 조회
# 작성자: 최한영
# 작성일: 2024-05-21
# 상세 설명: 투어 API의 키워드검색 조회

import requests
from func_def import *

url= 'http://apis.data.go.kr/B551011/KorService1/searchKeyword1'

# 요청 키워드 국문 인코등 필요
keyword = '김치'

keyword_encoding = url_encoding(keyword)

contentTypeId = '12'


params = {
    # 필수
    'serviceKey': '',
    'MobileOS':'ETC',
    'MobileApp':'AppTest',
    'keyword' : keyword_encoding,

    #선택
    'contentTypeId':contentTypeId,  # 관광타입
    'areaCode':'',
    'sigunguCode':'',
    'cat1':'',
    'cat2':'',
    'cat3':'',
    'numOfRows':'10',               # 한페이지결과수
    'pageNo':'1',                   # 페이지번호
    '_type':'json',                 # 응답메세지 형식
    'listYN': 'Y',                  # 목록구분
    'arrange': 'A'                  # 정렬구분
}

response = requests.get(make_url(url, params), verify=False)

if response.status_code == 200:
    print(response.text)
    make_csv(response.text, '키워드검색 조회_'+ keyword ,'searchKeyword')
else:
    print(f'Error: {response.status_code}')