#QUIZ

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




