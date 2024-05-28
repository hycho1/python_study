import os
import csv
import pymysql
from func_def import *

data_list = getDataFromTable()

temp_list = []
for i in data_list:

    temp_list.append(i[2])

print(temp_list)


# 데이터베이스 연결 설정
connection = pymysql.connect(
    host='192.168.0.103',  # 호스트명
    user='user1',  # 사용자 이름
    password='u1234',  # 비밀번호
    database='project01',  # 데이터베이스 이름
)

try:
    with connection.cursor() as cursor:
        # CSV 파일 경로
        for i in temp_list:

            csv_file = f'C:\Source\Project 1\Project 1\py_code\공통정보조회_{i}.csv'
            
            with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)  # 첫 번째 행은 열 이름이므로 건너뜁니다.
                for row in csv_reader:
                    # 데이터 삽입 쿼리
                    insert_query = "INSERT INTO places_detailcommon (contentid,areacode1,areacode2,detail_description) VALUES (%s,%s,%s,%s)"
                    cursor.execute(insert_query, (row[0],row[12],row[13],row[23])) 

            print(f"{i} 테이블 적재 완료")


    # 변경사항 커밋
    connection.commit()

finally:
    # 연결 종료
    connection.close()

print("데이터 삽입이 완료되었습니다.")