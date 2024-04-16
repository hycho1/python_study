a = 10
b = 2

print("a + b : ", a + b)
print("a + b : ", a + b)
print("a / b : ", a / b)
print("a // b : ", a // b)
print("a % b : ", a % b)

c= 2
c **= 3;
print(c)

mult = '''
multiline
test
string
'''


a = "Life is too short"

b = a.upper()
c = b.lower()
d = c.replace(" ",",")
print(a.upper())
print(b.lower())
print(c.replace(" ",","))
print(d.split(","))

'''

#odd = [1, 3, [7, 9], 5]
#odd.sort()
#print(odd)

'''
str = "0 똘기 떵이 호치 새초미"

list1 = str.split(" ");

cnt = int(list1[0])
list1.pop(0)


if(int(cnt) >= 0):
    for i in range(cnt):
        list1.insert(0,list1.pop())
else:
    cnt *= -1
    for i in range(cnt):
        list1.insert(len(list1)-1 ,list1.pop(0))

print(list1)
'''

'''
data = input('회전수와 문자열을 입력하세요. : ').split()
rn = int(data.pop(0)) % len(data)
print(' '.join([
        (data*2)[len(data) + i - rn]
            for i in range(len(data))
                ])
    )

'''


interest = ['삼성','LG','Naver']

interest.pop(1)
print(interest)


interest2 = ['삼성','LG', 'Naver', '하이닉스', '대우']


def add(a, b):
    return a+b

print(add(1, 2))
