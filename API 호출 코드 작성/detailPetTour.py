# 코드 목적: 반려동물여행정보조회
# 작성자: 최한영
# 작성일: 2024-05-21
# 상세 설명: 투어 API의 반려동물여행정보조회

import requests
from func_def import *

url= 'http://apis.data.go.kr/B551011/KorService1/detailPetTour1'

# 콘텐츠 ID 미입력 시 반려동물 전부 출력
contentId = '125534'

params = {
    # 필수
    'serviceKey': '',
    'MobileOS':'ETC',
    'MobileApp':'AppTest',

    #선택
    'contentId':contentId,          # 콘텐츠 ID             Id 문서 잘못 입력되어 있음
    'numOfRows':'10',               # 한페이지결과수
    'pageNo':'1',                   # 페이지번호
    '_type':'json'                  # 응답메세지 형식
}

response = requests.get(make_url(url, params), verify=False)

if response.status_code == 200:
    print(response.text)
    make_csv(response.text, '반려동물여행정보조회','detailPetTour')
else:
    print(f'Error: {response.status_code}')