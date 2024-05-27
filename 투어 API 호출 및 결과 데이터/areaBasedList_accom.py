# 코드 목적: 지역기반 관광정보조회 (숙박(32) 관광정보 전체조회)
# 작성자: 최한영
# 작성일: 2024-05-20
# 상세 설명: 투어 API의 지역코드와 관광코드를 조합하여 여행지 정보 조회

import requests
from func_def import *

url= 'http://apis.data.go.kr/B551011/KorService1/areaBasedList1'

filename = ''

# 관광타입
contentTypeId = '39'

# 지역코드
areaCode = '1'

# 시군구코드
sigunguCode = '1'

csv_file_path2 = '지역정보조회_시군구.csv'
data_list2 = []

with open(csv_file_path2, mode='r', newline='', encoding='cp949') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    next(csv_reader)
    
    for row in csv_reader:
        data_list2.append(row)

count = 0
for i in data_list2:
    params = {
        # 필수
        'numOfRows':'10',
        'pageNo':'1',
        'MobileOS':'ETC',
        'MobileApp':'AppTest',
        'serviceKey': '',
        # 선택
        '_type':'json',
        'listYN':'Y',
        'arrange':'A',
        'contentTypeId':contentTypeId,       # 관광타입
        'areaCode':i[1],                     # 지역코드
        'sigunguCode':i[0]                   # 시군구코드
    #    'cat1':'B02',                       # 대분류
    #    'cat2':'B0201',                     # 중분류
    #    'cat3':'B02010100',                 # 소분류
    #    'modifiedtime':'20240721'           # 수정일
    }

    print("광역시_도 코드 :::: ", i[1], "    시군구 코드 :::: " , i[0])

    filename = f'지역기반정보조회_{i[1]}_{i[0]}_{contentTypeId}'

    response = requests.get(make_url(url, params), verify=False)

    if response.status_code == 200:
        make_csv(response.text, filename,'areaBasedList_accom')
        print(f"{filename} done!")
    else:
        print(f'Error: {response.status_code}')