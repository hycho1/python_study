# 코드 목적: 지역정보조회 (시군구)
# 작성자: 최한영
# 작성일: 2024-05-20
# 상세 설명: 투어 API의 지역 코드 조회 API를 통해 모든 지역 코드를 조회하고자 함

import requests
import csv
import os
from func_def import *


url= 'http://apis.data.go.kr/B551011/KorService1/areaCode1'

data_list = []

csv_file_path = '지역정보조회_광역시_도.csv'

file_path = '지역정보조회_시군구.csv'

# 파일이 존재하는지 확인 후 삭제
if os.path.exists(file_path):
    os.remove(file_path)


with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    next(csv_reader)
    
    for row in csv_reader:
        data_list.append(row)

for i in data_list:

    params = {
    'serviceKey': '',   # 발급받은 API 키
    '_type': 'json',         # 반환 타입 (json, xml)
    'numOfRows': '100',      # 한 페이지 결과 수
    'pageNo': '1',           # 페이지 번호
    'MobileApp': 'AppTest',  # 시/도 이름
    'MobileOS': 'ETC',       # 버전
    'areaCode' : i[0]           # 지역코드     // 지역코드 미입력 - 광역시/도
    }

    response = requests.get(make_url(url, params), verify=False)

    if response.status_code == 200:
        make_csv(response.text,'지역정보조회_시군구', 'areaCode_sub')
    else:
        print(f'Error: {response.status_code}')