# 코드 목적: 공통정보조회
# 작성자: 최한영
# 작성일: 2024-05-21
# 상세 설명: 투어 API의 공통정보조회

import requests
from func_def import *

url= 'http://apis.data.go.kr/B551011/KorService1/detailCommon1'



data_list = getDataFromTable()

print(data_list[2][2],data_list[2][3])

'''
# 콘텐츠 ID
contentId = '125534'
# 관광타입
contentTypeId = '' 
'''

for i in data_list:
    
    params = {
        # 필수
        'serviceKey': '',
        'MobileOS':'ETC',
        'MobileApp':'AppTest',
        'contentId':str(i[2]),          # 콘텐츠 ID

        #선택
        'contentTypeId':str(i[3]),  # 관광타입(관광지, 숙박등) ID
        'defaultYN':'Y',                # 기본정보조회여부
        'firstImageYN':'Y',             # 원본, 썸네일대표이미지조회여부
        'areacodeYN':'Y',               # 지역코드, 시군구코드조회여부
        'catcodeYN':'Y',                # 대,중,소분류코드조회여부
        'addrinfoYN':'Y',               # 주소, 상세주소조회여부
        'mapinfoYN':'Y',                # 좌표X, Y 조회여부
        'overviewYN':'Y',               # 콘텐츠개요조회여부
        'numOfRows':'10',               # 한페이지결과수
        'pageNo':'1',                   # 페이지번호
        '_type':'json'                  # 응답메세지 형식
    }

    response = requests.get(make_url(url, params), verify=False)

    if response.status_code == 200:
        print(response.text)
        make_csv(response.text, f'공통정보조회_{str(i[2])}','detailCommon')
    else:
        print(f'Error: {response.status_code}')

    
