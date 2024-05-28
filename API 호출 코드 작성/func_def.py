import csv
import json
import urllib.parse
import mysql.connector


def make_url(url, params):

    temp = '?'
    count = 0
    for i in params:
        temp = temp + i + '=' + params[i]
        count = count + 1

        if count != (len(params)):    
            temp = temp + '&'

    return url + temp


def getDataFromTable():

    # 데이터베이스 연결 설정
    config = {
        'user': 'user1',
        'password': 'u1234',
        'host': '192.168.0.103',
        'database': 'project01',
        'port': '3306'
    }

    # 데이터베이스 연결
    conn = mysql.connector.connect(**config)

    # 커서 생성
    cursor = conn.cursor()

    # SQL 쿼리 실행
    query = "SELECT place_id, place_name, contentid, category FROM places limit 5"
    cursor.execute(query)

    # 결과를 리스트로 변환
    data_list = []
    for (column1, column2, column3, column4) in cursor:
        data_list.append((column1, column2, column3, column4))

    # 연결 종료
    cursor.close()
    conn.close()

    # 결과 출력
    return data_list




def url_encoding(text):

    # URL 인코딩
    encoded_text = urllib.parse.quote(text)
    return encoded_text



def make_csv(data, fileName, info):
    # 지역정보조회_광역시_도
    if(info == 'areaCode'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        filtered_data = [{"code": item["code"], "name": item["name"]} for item in items]

        csv_file_path = f'{fileName}.csv'

        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:

            csv_writer = csv.DictWriter(csv_file, fieldnames=["code", "name"])
            
            csv_file.seek(0, 2)
            file_empty = csv_file.tell() == 0
            
            if file_empty:
                csv_writer.writeheader()
            
            for row in filtered_data:
                csv_writer.writerow(row)
    # 지역정보조회_시군구
    elif(info == 'areaCode_sub'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        filtered_data = [{"code": item["code"], "name": item["name"]} for item in items]

        csv_file_path = f'{fileName}.csv'

        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:

            csv_writer = csv.DictWriter(csv_file, fieldnames=["code", "name"])
            
            csv_file.seek(0, 2)
            file_empty = csv_file.tell() == 0
            
            if file_empty:
                csv_writer.writeheader()
            
            for row in filtered_data:
                csv_writer.writerow(row)

    # 지역기반정보조회_(예시_숙박)
    elif(info == 'areaBasedList_accom'):

        data = json.loads(data)
        # CSV 파일로 저장
        csv_file_path = f'{fileName}.csv'
        
        if(data["response"]["body"]["totalCount"] > 0):
            items = data["response"]["body"]["items"]["item"]
            parsed_list = []

            # 리스트에 필요한 데이터 추가
            for item in items:
                parsed_item = {
                    "title": item["title"],
                    "addr1": item["addr1"],
                    "addr2": item["addr2"],
                    "contentid": item["contentid"],
                    "firstimage": item["firstimage"],
                    "mapx": item["mapx"],
                    "mapy": item["mapy"],
                    "tel": item["tel"]
                }
                parsed_list.append(parsed_item) 

            # CSV 파일 열기 (쓰기 모드)
            with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
                # CSV 작성자 생성
                csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid", "title", "addr1", "addr2", "tel","mapx", "mapy", "firstimage"])
                
                # 헤더 작성
                csv_writer.writeheader()
                
                # 데이터 작성
                for row in parsed_list:
                    csv_writer.writerow(row)
        else:
            print("TotalCount 0 - No Data")

            parsed_list = []

            parsed_item = {
                "title": "",
                "addr1": "",
                "addr2": "",
                "contentid": "",
                "firstimage": "",
                "mapx": "",
                "mapy": "",
                "tel": ""
            }
            parsed_list.append(parsed_item)

            with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
                # CSV 작성자 생성
                csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid", "title", "addr1", "addr2", "tel","mapx", "mapy", "firstimage"])
                
                # 헤더 작성
                csv_writer.writeheader()
                
                # 데이터 작성
                for row in parsed_list:
                    csv_writer.writerow(row)

    # 위치기반정보조회
    elif(info == 'locationBasedList'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        parsed_list = []

        # 리스트에 필요한 데이터 추가
        for item in items:
            parsed_item = {
                "title": item["title"],
                "tel": item["tel"],
                "mapx": item["mapx"],
                "mapy": item["mapy"],
                "dist": item["dist"],           # 중심좌표로부터거리
                "cat1": item["cat1"],
                "cat2": item["cat2"],
                "cat3": item["cat3"],
                "addr1": item["addr1"],
                "addr2": item["addr2"],
                "booktour": item["booktour"],
                "contentid": item["contentid"]
            }
            parsed_list.append(parsed_item)

        # CSV 파일로 저장
        csv_file_path = f'{fileName}.csv'

        # CSV 파일 열기 (쓰기 모드)
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            # CSV 작성자 생성
            csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid", "title", "addr1", "addr2", "tel", "mapx", "mapy", "dist", "cat1", "cat2", "cat3", "booktour"])
            
            # 헤더 작성
            csv_writer.writeheader()
            
            # 데이터 작성
            for row in parsed_list:
                csv_writer.writerow(row)
    # 서비스분류코드조회
    elif(info == 'categoryCode'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        parsed_list = []

        # 리스트에 필요한 데이터 추가
        for item in items:
            parsed_item = {
                "rnum": item["rnum"],
                "name": item["name"],
                "code": item["code"]
            }
            parsed_list.append(parsed_item)

        # CSV 파일로 저장
        csv_file_path = f'{fileName}.csv'

        # CSV 파일 열기 (쓰기 모드)
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            # CSV 작성자 생성
            csv_writer = csv.DictWriter(csv_file, fieldnames=["rnum", "name", "code"])
            
            # 헤더 작성
            csv_writer.writeheader()
            
            # 데이터 작성
            for row in parsed_list:
                csv_writer.writerow(row)
    # 숙소정보조회
    elif(info == 'searchStay'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        parsed_list = []

        # 리스트에 필요한 데이터 추가
        for item in items:
            parsed_item = {
                "addr1": item["addr1"],
                "addr2": item["addr2"],
                "booktour": item["booktour"],
                "benikia": item["benikia"],                 # 베니키아 여부(해당=1)
                "goodstay": item["goodstay"],               # 굿스테이 여부(해당=1)
                "hanok": item["hanok"],                     # 한옥 여부(해당=1)
                "cat1": item["cat1"],
                "cat2": item["cat2"],
                "cat3": item["cat3"],
                "contentid": item["contentid"],
                "contenttypeid": item["contenttypeid"],             
                "firstimage": item["firstimage"],
                "firstimage2": item["firstimage2"],
                "mapx": item["mapx"],
                "mapy": item["mapy"],
                "mlevel": item["mlevel"],
                "modifiedtime": item["modifiedtime"],
                "tel": item["tel"],
                "title": item["title"]
            }
            parsed_list.append(parsed_item)

        # CSV 파일로 저장
        csv_file_path = f'{fileName}.csv'

        # CSV 파일 열기 (쓰기 모드)
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            # CSV 작성자 생성
            csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid", "title", "addr1", "addr2", "tel", "mapx", "mapy", "mlevel", "modifiedtime", "contenttypeid", "firstimage", "firstimage2", "cat1", "cat2", "cat3", "booktour", "benikia","goodstay","hanok"])
            
            # 헤더 작성
            csv_writer.writeheader()
            
            # 데이터 작성
            for row in parsed_list:
                csv_writer.writerow(row)
    # 행사정보조회
    elif(info == 'searchFestival'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        parsed_list = []

        # 리스트에 필요한 데이터 추가
        for item in items:
            parsed_item = {
                "addr1": item["addr1"],
                "addr2": item["addr2"],
                "booktour": item["booktour"],
                "cat1": item["cat1"],
                "cat2": item["cat2"],
                "cat3": item["cat3"],
                "contentid": item["contentid"],
                "contenttypeid": item["contenttypeid"],
                "eventstartdate": item["eventstartdate"],       # 행사시작일
                "eventenddate": item["eventenddate"],           # 행사종료일
                "firstimage": item["firstimage"],
                "firstimage2": item["firstimage2"],
                "mapx": item["mapx"],
                "mapy": item["mapy"],
                "mlevel": item["mlevel"],
                "modifiedtime": item["modifiedtime"],
                "tel": item["tel"],
                "title": item["title"]
            }
            parsed_list.append(parsed_item)

        # CSV 파일로 저장
        csv_file_path = f'{fileName}.csv'

        # CSV 파일 열기 (쓰기 모드)
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            # CSV 작성자 생성
            csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid", "title", "eventstartdate", "eventenddate", "addr1", "addr2", "tel", "mapx", "mapy", "mlevel", "modifiedtime", "contenttypeid", "firstimage", "firstimage2", "cat1", "cat2", "cat3", "booktour"])
            
            # 헤더 작성
            csv_writer.writeheader()
            
            # 데이터 작성
            for row in parsed_list:
                csv_writer.writerow(row)
    # 키워드검색 조회
    elif(info == 'searchKeyword'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        parsed_list = []

        # 리스트에 필요한 데이터 추가
        for item in items:
            parsed_item = {
                "addr1": item["addr1"],
                "addr2": item["addr2"],
                "booktour": item["booktour"],
                "cat1": item["cat1"],
                "cat2": item["cat2"],
                "cat3": item["cat3"],
                "contentid": item["contentid"],
                "contenttypeid": item["contenttypeid"],
                "firstimage": item["firstimage"],
                "firstimage2": item["firstimage2"],
                "mapx": item["mapx"],
                "mapy": item["mapy"],
                "mlevel": item["mlevel"],
                "modifiedtime": item["modifiedtime"],
                "tel": item["tel"],
                "title": item["title"],
                "cpyrhtDivCd": item["cpyrhtDivCd"],                
                "areacode": item["areacode"],
                "sigungucode": item["sigungucode"],
                "createdtime": item["createdtime"],

            }
            parsed_list.append(parsed_item)

        # CSV 파일로 저장
        csv_file_path = f'{fileName}.csv'

        # CSV 파일 열기 (쓰기 모드)
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            # CSV 작성자 생성
            csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid", "title", "addr1", "addr2", "tel", "mapx", "mapy", "mlevel", "modifiedtime", "contenttypeid", "firstimage", "firstimage2", "cat1", "cat2", "cat3", "booktour", "cpyrhtDivCd","areacode","sigungucode","createdtime"])
            
            # 헤더 작성
            csv_writer.writeheader()
            
            # 데이터 작성
            for row in parsed_list:
                csv_writer.writerow(row)  

    # 반려동물 여행 정보 조회
    elif(info == 'detailPetTour'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        parsed_list = []

        # 리스트에 필요한 데이터 추가
        for item in items:
            parsed_item = {
                "acmpyPsblCpam": item["acmpyPsblCpam"],
                "relaRntlPrdlst": item["relaRntlPrdlst"],
                "acmpyNeedMtr": item["acmpyNeedMtr"],
                "relaFrnshPrdlst": item["relaFrnshPrdlst"],
                "etcAcmpyInfo": item["etcAcmpyInfo"],
                "relaPurcPrdlst": item["relaPurcPrdlst"],
                "relaAcdntRiskMtr": item["relaAcdntRiskMtr"],
                "acmpyTypeCd": item["acmpyTypeCd"],
                "relaPosesFclty": item["relaPosesFclty"],
                "contentid": item["contentid"],
                "petTursmInfo": item["petTursmInfo"]
            }
            parsed_list.append(parsed_item)

        # CSV 파일로 저장
        csv_file_path = f'{fileName}.csv'

        # CSV 파일 열기 (쓰기 모드)
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            # CSV 작성자 생성
            csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid","acmpyPsblCpam", "relaRntlPrdlst", "acmpyNeedMtr", "relaFrnshPrdlst", "etcAcmpyInfo", "relaPurcPrdlst", "relaAcdntRiskMtr", "acmpyTypeCd", "relaPosesFclty", "petTursmInfo"])
            
            # 헤더 작성
            csv_writer.writeheader()
            
            # 데이터 작성
            for row in parsed_list:
                csv_writer.writerow(row)  

    # 공통정보 조회
    elif(info == 'detailCommon'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        parsed_list = []

        # 리스트에 필요한 데이터 추가
        for item in items:
            parsed_item = {
                "contentid": item["contentid"],
                "contenttypeid": item["contenttypeid"],
                "booktour": item["booktour"],
                "createdtime": item["createdtime"],
                "homepage": item["homepage"],
                "modifiedtime": item["modifiedtime"],
                "tel": item["tel"],
                "telname": item["telname"],
                "title": item["title"],
                "firstimage": item["firstimage"],
                "firstimage2": item["firstimage2"],
                "cpyrhtDivCd": item["cpyrhtDivCd"],
                "areacode": item["areacode"],
                "sigungucode": item["sigungucode"],
                "cat1": item["cat1"],
                "cat2": item["cat2"],
                "cat3": item["cat3"],
                "addr1": item["addr1"],
                "addr2": item["addr2"],
                "zipcode": item["zipcode"],
                "mapx": item["mapx"],
                "mapy": item["mapy"],
                "mlevel": item["mlevel"],
                "overview": item["overview"]
            }
            parsed_list.append(parsed_item)

        # CSV 파일로 저장
        csv_file_path = f'{fileName}.csv'

        # CSV 파일 열기 (쓰기 모드)
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            # CSV 작성자 생성
            csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid", "contenttypeid", "booktour", "createdtime", "homepage", "modifiedtime", "tel", "telname", "title", "firstimage", "firstimage2", "cpyrhtDivCd", "areacode", "sigungucode", "cat1", "cat2", "cat3", "addr1", "addr2", "zipcode", "mapx", "mapy", "mlevel", "overview"])
            
            # 헤더 작성
            csv_writer.writeheader()
            
            # 데이터 작성
            for row in parsed_list:
                csv_writer.writerow(row)  

    # 소개정보 조회
    elif(info == 'detailIntro'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        parsed_list = []

        # 리스트에 필요한 데이터 추가
        for item in items:
            if (item["contenttypeid"] == '12'):
                parsed_item = {
                    "contentid": item["contentid"],
                    "contenttypeid": item["contenttypeid"],
                    "accomcount": item["accomcount"],
                    "chkbabycarriage": item["chkbabycarriage"],
                    "chkcreditcard": item["chkcreditcard"],
                    "chkpet": item["chkpet"],
                    "expagerange": item["expagerange"],
                    "heritage1": item["heritage1"],
                    "heritage2": item["heritage2"],
                    "heritage3": item["heritage3"],
                    "infocenter": item["infocenter"],
                    "opendate": item["opendate"],
                    "parking": item["parking"],
                    "restdate": item["restdate"],
                    "useseason": item["useseason"],
                    "usetime": item["usetime"]
                }
            elif (item["contenttypeid"] == '14'):
                parsed_item = {
                    "contentid": item["contentid"],
                    "contenttypeid": item["contenttypeid"],
                    "accomcountculture": item["accomcountculture"],
                    "chkbabycarriageculture": item["chkbabycarriageculture"],
                    "chkcreditcardculture": item["chkcreditcardculture"],
                    "chkpetculture": item["chkpetculture"],
                    "discountinfo": item["discountinfo"],
                    "infocenterculture": item["infocenterculture"],
                    "parkingculture": item["parkingculture"],
                    "parkingfee": item["parkingfee"],
                    "restdateculture": item["restdateculture"],
                    "usefee": item["usefee"],
                    "usetimeculture": item["usetimeculture"],
                    "scale": item["scale"],
                    "spendtime": item["spendtime"]
                }
            elif (item["contenttypeid"] == '15'):
                parsed_item = {
                    "contentid": item["contentid"],
                    "contenttypeid": item["contenttypeid"],
                    "agelimit": item["agelimit"],
                    "bookingplace": item["bookingplace"],
                    "discountinfofestival": item["discountinfofestival"],
                    "eventenddate": item["eventenddate"],
                    "eventhomepage": item["eventhomepage"],
                    "eventplace": item["eventplace"],
                    "eventstartdate": item["eventstartdate"],
                    "festivalgrade": item["festivalgrade"],
                    "placeinfo": item["placeinfo"],
                    "playtime": item["playtime"],
                    "program": item["program"],
                    "spendtimefestival": item["spendtimefestival"],
                    "sponsor1": item["sponsor1"],
                    "sponsor1tel": item["sponsor1tel"],
                    "sponsor2": item["sponsor2"],
                    "sponsor2tel": item["sponsor2tel"],
                    "subevent": item["subevent"],
                    "usetimefestival": item["usetimefestival"]
                }
            elif (item["contenttypeid"] == '25'):
                parsed_item = {
                    "contentid": item["contentid"],
                    "contenttypeid": item["contenttypeid"],
                    "distance": item["distance"],
                    "infocentertourcourse": item["infocentertourcourse"],
                    "schedule": item["schedule"],
                    "taketime": item["taketime"],
                    "theme": item["theme"]
                }
            elif (item["contenttypeid"] == '28'):
                parsed_item = {
                    "contentid": item["contentid"],
                    "contenttypeid": item["contenttypeid"],
                    "accomcountleports": item["accomcountleports"],
                    "chkbabycarriageleports": item["chkbabycarriageleports"],
                    "chkcreditcardleports": item["chkcreditcardleports"],
                    "chkpetleports": item["chkpetleports"],
                    "expagerangeleports": item["expagerangeleports"],
                    "infocenterleports": item["infocenterleports"],
                    "openperiod": item["openperiod"],
                    "parkingfeeleports": item["parkingfeeleports"],
                    "parkingleports": item["parkingleports"],
                    "reservation": item["reservation"],
                    "restdateleports": item["restdateleports"],
                    "scaleleports": item["scaleleports"],
                    "usefeeleports": item["usefeeleports"],
                    "usetimeleports": item["usetimeleports"]
                }
            elif (item["contenttypeid"] == '32'):
                parsed_item = {
                    "contentid": item["contentid"],
                    "contenttypeid": item["contenttypeid"],
                    "accomcountlodging": item["accomcountlodging"],
                    "benikia": item["benikia"],
                    "checkintime": item["checkintime"],
                    "checkouttime": item["checkouttime"],
                    "chkcooking": item["chkcooking"],
                    "foodplace": item["foodplace"],
                    "goodstay": item["goodstay"],
                    "hanok": item["hanok"],
                    "infocenterlodging": item["infocenterlodging"],
                    "parkinglodging": item["parkinglodging"],
                    "pickup": item["pickup"],
                    "roomcount": item["roomcount"],
                    "reservationlodging": item["reservationlodging"],
                    "reservationurl": item["reservationurl"],
                    "roomtype": item["roomtype"],
                    "scalelodging": item["scalelodging"],
                    "subfacility": item["subfacility"],
                    "barbecue": item["barbecue"],
                    "beauty": item["beauty"],
                    "beverage": item["beverage"],
                    "bicycle": item["bicycle"],
                    "campfire": item["campfire"],
                    "fitness": item["fitness"],
                    "karaoke": item["karaoke"],
                    "publicbath": item["publicbath"],
                    "publicpc": item["publicpc"],
                    "sauna": item["sauna"],
                    "seminar": item["seminar"],
                    "sports": item["sports"],
                    "refundregulation": item["refundregulation"]
                }
            elif (item["contenttypeid"] == '38'):    
                parsed_item = {
                    "contentid": item["contentid"],
                    "contenttypeid": item["contenttypeid"],
                    "chkbabycarriageshopping": item["chkbabycarriageshopping"],
                    "chkcreditcard": item["chkcreditcard"],
                    "shopping": item["shopping"],
                    "chkpetshopping": item["chkpetshopping"],
                    "culturecenter": item["culturecenter"],
                    "fairday": item["fairday"],
                    "infocentershopping": item["infocentershopping"],
                    "opendateshopping": item["opendateshopping"],
                    "opentime": item["opentime"],
                    "parkingshopping": item["parkingshopping"],
                    "restdateshopping": item["restdateshopping"],
                    "restroom": item["restroom"],
                    "saleitem": item["saleitem"],
                    "saleitemcost": item["saleitemcost"],
                    "scaleshopping": item["scaleshopping"],
                    "shopguide": item["shopguide"]
                }
            elif (item["contenttypeid"] == '39'):    
                parsed_item = {
                    "contentid": item["contentid"],
                    "contenttypeid": item["contenttypeid"],
                    "chkcreditcardfood": item["chkcreditcardfood"],
                    "discountinfofood": item["discountinfofood"],
                    "infocenterfood": item["infocenterfood"],
                    "kidsfacility": item["kidsfacility"],
                    "opendatefood": item["opendatefood"],
                    "opentimefood": item["opentimefood"],
                    "packing": item["packing"],
                    "parkingfood": item["parkingfood"],
                    "reservationfood": item["reservationfood"],
                    "restdatefood": item["restdatefood"],
                    "scalefood": item["scalefood"],
                    "seat": item["seat"],
                    "smoking": item["smoking"],
                    "treatmenu": item["treatmenu"],
                    "lcnsno": item["lcnsno"]
                }
                
            parsed_list.append(parsed_item)

        # CSV 파일로 저장
        csv_file_path = f'{fileName}.csv'

        # CSV 파일 열기 (쓰기 모드)
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            # CSV 작성자 생성

            if(parsed_list[0]['contenttypeid'] == '12'):
                csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid","contenttypeid","accomcount","chkbabycarriage","chkcreditcard","chkpet","expagerange","heritage1","heritage2","heritage3","infocenter","opendate","parking","restdate","useseason","usetime"])
            elif(parsed_list[0]['contenttypeid'] == '14'):
                csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid","contenttypeid","accomcountculture","chkbabycarriageculture","chkcreditcardculture","chkpetculture","discountinfo","infocenterculture","parkingculture","parkingfee","restdateculture","usefee","usetimeculture","scale","spendtime"])
            elif(parsed_list[0]['contenttypeid'] == '15'):
                csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid","contenttypeid","agelimit","bookingplace","discountinfofestival","eventenddate","eventhomepage","eventplace","eventstartdate","festivalgrade","placeinfo","playtime","program","spendtimefestival","sponsor1","sponsor1tel","sponsor2","sponsor2tel","subevent","usetimefestival"])
            elif(parsed_list[0]['contenttypeid'] == '25'):
                csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid","contenttypeid","distance","infocentertourcourse","schedule","taketime","theme"])
            elif(parsed_list[0]['contenttypeid'] == '28'):
                csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid","contenttypeid","accomcountleports","chkbabycarriageleports","chkcreditcardleports","chkpetleports","expagerangeleports","infocenterleports","openperiod","parkingfeeleports","parkingleports","reservation","restdateleports","scaleleports","usefeeleports","usetimeleports"])
            elif(parsed_list[0]['contenttypeid'] == '32'):
                csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid","contenttypeid","accomcountlodging","benikia","","checkintime","checkouttime","chkcooking","foodplace","goodstay","hanok","infocenterlodging","parkinglodging","pickup","roomcount","reservationlodging","reservationurl","roomtype","scalelodging","subfacility","barbecue","beauty","beverage","bicycle","campfire","fitness","karaoke","publicbath","publicpc","sauna","seminar","sports","refundregulation"])
            elif(parsed_list[0]['contenttypeid'] == '38'):
                csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid","contenttypeid","chkbabycarriageshopping","chkcreditcard","shopping","chkpetshopping","culturecenter","fairday","infocentershopping","opendateshopping","opentime","parkingshopping","restdateshopping","restroom","saleitem","saleitemcost","scaleshopping","shopguide"])
            elif(parsed_list[0]['contenttypeid'] == '39'):
                csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid","contenttypeid","chkcreditcardfood","discountinfofood","infocenterfood","kidsfacility","opendatefood","opentimefood","packing","parkingfood","reservationfood","restdatefood","scalefood","seat","smoking","treatmenu","lcnsno","overview"])
            
            # 헤더 작성
            csv_writer.writeheader()
            
            # 데이터 작성
            for row in parsed_list:
                csv_writer.writerow(row)  

    # 반복정보 조회
    elif(info == 'detailInfo'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        parsed_list = []

        # 리스트에 필요한 데이터 추가
        for item in items:
            if (item["contenttypeid"] == '25'):
                parsed_item = {
                    "contentid": item["contentid"],
                    "contenttypeid": item["contenttypeid"],
                    "subcontentid": item["subcontentid"],
                    "subdetailalt": item["subdetailalt"],
                    "subdetailimg": item["subdetailimg"],
                    "subdetailoverview": item["subdetailoverview"],
                    "subname": item["subname"],
                    "subnum": item["subnum"]
                }
            elif (item["contenttypeid"] == '32'):
                parsed_item = {
                    "contentid": item["contentid"],
                    "contenttypeid": item["contenttypeid"],
                    "roomcode": item["roomcode"],
                    "roomtitle": item["roomtitle"],
                    "roomsize1": item["roomsize1"],
                    "roomcount": item["roomcount"],
                    "roombasecount": item["roombasecount"],
                    "roommaxcount": item["roommaxcount"],
                    "roomoffseasonminfee1": item["roomoffseasonminfee1"],
                    "roomoffseasonminfee2": item["roomoffseasonminfee2"],
                    "roompeakseasonminfee1": item["roompeakseasonminfee1"],
                    "roompeakseasonminfee2": item["roompeakseasonminfee2"],
                    "roomintro": item["roomintro"],
                    "roombathfacility": item["roombathfacility"],
                    "roomhometheater": item["roomhometheater"],
                    "roomaircondition": item["roomaircondition"],
                    "roomtv": item["roomtv"],
                    "roompc": item["roompc"],
                    "roomcable": item["roomcable"],
                    "roominternet": item["roominternet"],
                    "roomrefrigerator": item["roomrefrigerator"],
                    "roomtoiletries": item["roomtoiletries"],
                    "roomsofa": item["roomsofa"],
                    "roomcook": item["roomcook"],
                    "roomtable": item["roomtable"],
                    "roomhairdryer": item["roomhairdryer"],
                    "roomsize2": item["roomsize2"],
                    "roomimg1": item["roomimg1"],
                    "roomimg1alt": item["roomimg1alt"],
                    "cpyrhtDivCd1": item["cpyrhtDivCd1"],
                    "roomimg2alt": item["roomimg2alt"],
                    "cpyrhtDivCd2": item["cpyrhtDivCd2"],
                    "roomimg3": item["roomimg3"],
                    "roomimg3alt": item["roomimg3alt"],
                    "cpyrhtDivCd3": item["cpyrhtDivCd3"],
                    "roomimg4alt": item["roomimg4alt"],
                    "cpyrhtDivCd4": item["cpyrhtDivCd4"],
                    "roomimg5": item["roomimg5"],
                    "roomimg5alt": item["roomimg5alt"],
                    "cpyrhtDivCd5": item["cpyrhtDivCd5"]                    
                }
            else :
                parsed_item = {
                    "contentid": item["contentid"],
                    "contenttypeid": item["contenttypeid"],
                    "fldgubun": item["fldgubun"],
                    "infoname": item["infoname"],
                    "infotext": item["infotext"],
                    "serialnum": item["serialnum"]
                }
                            
            parsed_list.append(parsed_item)

        # CSV 파일로 저장
        csv_file_path = f'{fileName}.csv'

        # CSV 파일 열기 (쓰기 모드)
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            # CSV 작성자 생성

            if(parsed_list[0]['contenttypeid'] == '25'):
                csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid","contenttypeid","subcontentid","subdetailalt","subdetailimg","subdetailoverview","subname","subnum"])
            elif(parsed_list[0]['contenttypeid'] == '32'):
                csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid","contenttypeid","roomcode","roomtitle","roomsize1","roomcount","roombasecount","roommaxcount","roomoffseasonminfee1","roomoffseasonminfee2","roompeakseasonminfee1","roompeakseasonminfee2","roomintro","roombathfacility","roombath","roomhometheater","roomaircondition","roomtv","roompc","roomcable","roominternet","roomrefrigerator","roomtoiletries","roomsofa","roomcook","roomtable","roomhairdryer","roomsize2","roomimg1","roomimg1alt","cpyrhtDivCd1","roomimg2","roomimg2alt","cpyrhtDivCd2","roomimg3","roomimg3alt","cpyrhtDivCd3","roomimg4","roomimg4alt","cpyrhtDivCd4","roomimg5","roomimg5alt","cpyrhtDivCd5"])
            else:
                csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid","contenttypeid","fldgubun","infoname","infotext","serialnum"])
            # 헤더 작성
            csv_writer.writeheader()
            
            # 데이터 작성
            for row in parsed_list:
                csv_writer.writerow(row)

    # 이미지정보 조회
    elif(info == 'detailImage'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        parsed_list = []

        # 리스트에 필요한 데이터 추가
        for item in items:
            parsed_item = {
                    "contentid": item["contentid"],
                    "imgname": item["imgname"],
                    "originimgurl": item["originimgurl"],
                    "serialnum": item["serialnum"],
                    "cpyrhtDivCd": item["cpyrhtDivCd"],
                    "smallimageurl": item["smallimageurl"]
            }
            parsed_list.append(parsed_item)

        # CSV 파일로 저장
        csv_file_path = f'{fileName}.csv'

        # CSV 파일 열기 (쓰기 모드)
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:

            # CSV 작성자 생성
            csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid","imgname","originimgurl","serialnum","cpyrhtDivCd","smallimageurl"])

            # 헤더 작성
            csv_writer.writeheader()
            
            # 데이터 작성
            for row in parsed_list:
                csv_writer.writerow(row)

    # 이미지정보 조회
    elif(info == 'areaBasedSyncList'):

        data = json.loads(data)

        items = data["response"]["body"]["items"]["item"]
        parsed_list = []

        # 리스트에 필요한 데이터 추가
        for item in items:
            parsed_item = {
                    "addr1": item["addr1"],
                    "addr2": item["addr2"],
                    "areacode": item["areacode"],
                    "booktour": item["booktour"],
                    "cat1": item["cat1"],
                    "cat2": item["cat2"],
                    "cat3": item["cat3"],
                    "contentid": item["contentid"],
                    "contenttypeid": item["contenttypeid"],
                    "createdtime": item["createdtime"],
                    "firstimage": item["firstimage"],
                    "firstimage2": item["firstimage2"],
                    "cpyrhtDivCd": item["cpyrhtDivCd"],
                    "mapx": item["mapx"],
                    "mapy": item["mapy"],
                    "mlevel": item["mlevel"],
                    "modifiedtime": item["modifiedtime"],
                    "sigungucode": item["sigungucode"],
                    "tel": item["tel"],
                    "title": item["title"],
                    "zipcode": item["zipcode"]
            }
            parsed_list.append(parsed_item)

        # CSV 파일로 저장
        csv_file_path = f'{fileName}.csv'

        # CSV 파일 열기 (쓰기 모드)
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:

            # CSV 작성자 생성
            csv_writer = csv.DictWriter(csv_file, fieldnames=["contentid","imgname","originimgurl","serialnum","cpyrhtDivCd","smallimageurl"])

            # 헤더 작성
            csv_writer.writeheader()
            
            # 데이터 작성
            for row in parsed_list:
                csv_writer.writerow(row)