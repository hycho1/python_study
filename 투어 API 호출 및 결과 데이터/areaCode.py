# 코드 목적: 지역정보조회 (광역시_도)
# 작성자: 최한영
# 작성일: 2024-05-20
# 상세 설명: 투어 API의 지역 코드 조회 API를 통해 모든 지역 코드를 조회하고자 함


import requests
from func_def import *


url= 'http://apis.data.go.kr/B551011/KorService1/areaCode1'

params = {
'serviceKey': '',   # 발급받은 API 키
'_type': 'json',         # 반환 타입 (json, xml)
'numOfRows': '100',      # 한 페이지 결과 수
'pageNo': '1',           # 페이지 번호
'MobileApp': 'AppTest',  # 시/도 이름
'MobileOS': 'ETC'        # 버전
#'areaCode' : ''         # 지역코드     // 지역코드 미입력 - 광역시/도
}

response = requests.get(make_url(url, params), verify=False)

if response.status_code == 200:
    make_csv(response.text, '지역정보조회_광역시_도', 'areaCode')
else:
    print(f'Error: {response.status_code}')





