'''
#QUIZ 3

cash = 1000
snack = 200
charge = cash - snack
print("잔돈 = %d" % charge)


# sub 1) 가로가 4이고 세로가 2인 삼각형의 넓이 출력

width = 4
height = 2 

print("삼각형의 넓이는 " ,int(width*height/2))


# sub 2) 월급이 100원이다 세금 10%를 제외한 연봉 출력

sales = 100
year_sales = sales*12
tax = year_sales*0.1

print(year_sales - tax)


# sub 3) 100초를 1분 40초로 출력

total = 100
min = 100 / 60
sec = 100 % 60
print("%d분 %d초" % (min, sec))


# sub 4) 800원에서 500원을 제외한 100원의 개수 출력

total = 800
print(total%500/100)
'''
'''
QUIZ #4
주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.

(데이터)
이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌

1김씨와 이씨는 각각 몇 명 인가요?
2."이재영"이란 이름이 몇 번 반복되나요?
3.중복을 제거한 이름을 출력하세요.
4.중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
'''

name_string = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"

name_list = name_string.split(",")

# sub 1
 
count_lee = 0
count_kim = 0

for i in range(len(name_list)):
 if(name_list[i].find('이') == 0):
  count_lee += 1
 if(name_list[i].find('김') == 0):
  count_kim += 1

print("1번 답: 이 : %d, 김: %d" % (count_lee, count_kim))


# sub 2

count_jea = 0

for i in range(len(name_list)):
 if(name_list[i].find('이재영')==0):
  count_jea += 1

print("2번 답: ", count_jea)


# sub 3

name_set = set(name_list)

print("3번 답: ", name_set)


# sub 4

name_list_arrage= list(name_set)

print("4번 답: ", sorted(name_list_arrage))
