# 코드 목적: 소개정보조회
# 작성자: 최한영
# 작성일: 2024-05-21
# 상세 설명: 투어 API의 소개정보조회

import requests
from func_def import *

url= 'http://apis.data.go.kr/B551011/KorService1/detailIntro1'

# 콘텐츠 ID
contentId = '2674675'

# 관광타입
contentTypeId = '15' 

params = {
    # 필수
    'serviceKey': '',
    'MobileOS':'ETC',
    'MobileApp':'AppTest',
    'contentId':contentId,          # 콘텐츠 ID
    'contentTypeId':contentTypeId,  # 관광타입(관광지, 숙박등) ID

    #선택
    'numOfRows':'10',               # 한페이지결과수
    'pageNo':'1',                   # 페이지번호
    '_type':'json'                  # 응답메세지 형식
}

response = requests.get(make_url(url, params), verify=False)

if response.status_code == 200:
    #print(response.text)
    make_csv(response.text, '소개정보조회','detailIntro')
else:
    print(f'Error: {response.status_code}')