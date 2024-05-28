# 코드 목적: 위치기반관광정보조회
# 작성자: 최한영
# 작성일: 2024-05-20
# 상세 설명: 투어 API의 위치기반관광정보조회

import requests
import csv
import os
from func_def import *


url= 'http://apis.data.go.kr/B551011/KorService1/locationBasedList1'

'''
# 파일이 존재하는지 확인 후 삭제
if os.path.exists(file_path):
    os.remove(file_path)
'''

'''
서울특별시 중구 명동 근처 100m 이내에있는모든타입의 관광정보 조회
http://apis.data.go.kr/B551011/KorService1/locationBasedList1?serviceKey=인증키numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&mapX=126.983745&mapY=37.563446&radius=100&listYN=Y
'''


# GPS X좌표
mapX = '126.981611'
# GPS Y좌표
mapY = '37.567477'
# 거리반경(M)
radius = '1000'
# 관광 타입 ID
contentTypeId = '15'


params = {
    # 필수
    'serviceKey': '',   # 발급받은 API 키
    'MobileApp': 'AppTest',             # 시/도 이름
    'MobileOS': 'ETC',                  # 버전
    'mapX' : mapX,                      # GPS X좌표
    'mapY' : mapY,                      # GPS Y좌표
    'radius' : radius,                  # 거리반경
    
    # 선택
    'contentTypeId' : contentTypeId,    # 관광타입 ID    
    'listYN' : 'Y',                     # 목록구분(Y=목록, N=개수)
    'arrange' : 'A',                    # 정렬구분
    '_type': 'json',                    # 반환 타입 (json, xml)
    'numOfRows': '10',                  # 한 페이지 결과 수
    'pageNo': '1',                      # 페이지 번호
    'modifiedtime' : ''                 # 수정일
}

response = requests.get(make_url(url, params), verify=False)

if response.status_code == 200:
    make_csv(response.text,'위치기반관광정보조회', 'locationBasedList')
else:
    print(f'Error: {response.status_code}')