# 코드 목적: 이미지정보조회
# 작성자: 최한영
# 작성일: 2024-05-21
# 상세 설명: 투어 API의 이미지정보조회

import requests
from func_def import *

url= 'http://apis.data.go.kr/B551011/KorService1/detailImage1'

# 콘텐츠 ID
contentId = '1095732'

params = {
    # 필수
    'serviceKey': '',
    'MobileOS':'ETC',
    'MobileApp':'AppTest',
    'contentId':contentId,          # 콘텐츠 ID
    
    #선택
    'imageYN':'Y',                  # 이미지조회1(Y:콘텐츠이미지조회 / N:"음식점"타입의음식메뉴이미지)
    'subImageYN':'Y',               # 이미지조회2(원본,썸네일이미지조회)
    'numOfRows':'10',               # 한페이지결과수
    'pageNo':'1',                   # 페이지번호
    '_type':'json'                  # 응답메세지 형식
}

response = requests.get(make_url(url, params), verify=False)
print(response.text)
if response.status_code == 200:
    print(response.text)
    make_csv(response.text, '이미지정보조회','detailImage')
else:
    print(f'Error: {response.status_code}')