'''
a = 3
if a > 1:
 print("a는 1보다 큽니다\n")


i = 0
while i < 3:
 i = i + 1

print(i)
'''
'''
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

mult = """
multiline 
test
string
"""

print("===")
print(mult[0])
print("===")
print("\n")
print("===")
print()
print("===")

a = "20230331Rainy"
year = a[0:4]
month = a[4:6]
date = a[6:8]

weather = a[8:]

print(year + month + date + weather)


'''
'''
num = 99
width = 10
f_str = f"{num:>{10}}"

print(f_str)



f_strr = "{2:(>5}{1:<5}{0:<5} ".format("hi", "yes", "yeet")

print(f_strr)
'''
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


data = input('회전수와 문자열을 입력하세요. : ').split()
rn = int(data.pop(0)) % len(data)
print(' '.join([
        (data*2)[len(data) + i - rn]
            for i in range(len(data))
                ])
    )




interest = ['삼성','LG','Naver']

interest.pop(1)
print(interest)


interest2 = ['삼성','LG', 'Naver', '하이닉스', '대우']


def add(a, b):
    return a+b

print(add(1, 2))

a = 3.123123123123 
print("%-10.5f" % a)

dict_2 = {'j': 1, 'k':2, 'l':3}
dict_ = {'a': [1,2,3], 'b': dict_2}


print(dict_['a'])

s1 = set("i love u")
s2 = set("u love me");

s3 = s1 & s2

print(s3)

s4 = s1 |  s2

print(s4)

s5 = s1 - s2

print(s5)

print(True==1)
