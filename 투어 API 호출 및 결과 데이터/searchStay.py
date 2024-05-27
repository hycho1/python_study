# 코드 목적: 숙박정보조회
# 작성자: 최한영
# 작성일: 2024-05-20
# 상세 설명: 투어 API의 숙박정보조회

import requests
from func_def import *

url= 'http://apis.data.go.kr/B551011/KorService1/searchStay1'

params = {
    # 필수
    'serviceKey': '',
    'MobileOS':'ETC',
    'MobileApp':'AppTest',

    #선택
    'numOfRows':'10',               # 한페이지결과수
    'pageNo':'1',                   # 페이지번호
    '_type':'json',                 # 응답메세지 형식
    'listYN': 'Y',                  # 목록구분
    'arrange': 'A'                  # 정렬구분
}

response = requests.get(make_url(url, params), verify=False)

print(response.text)

if response.status_code == 200:
    #print(response.text)
    make_csv(response.text, '숙박정보조회','searchStay')
else:
    print(f'Error: {response.status_code}')



