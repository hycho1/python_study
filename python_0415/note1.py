
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

