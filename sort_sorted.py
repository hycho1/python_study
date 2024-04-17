# sort(), sorted() 비교

# sort와 sorted 모두 정렬을 위한 함수이지만
# 공식문서에서 sorted는 'stable'이 보장된다고 함 (비교 항목이 다수 일 경우 상대적 순서 정렬을 보장)
#
'''
내장 sorted() 함수는 안정적(stable)임이 보장됩니다.
정렬은 같다고 비교되는 요소의 상대적 순서를 변경하지 않으면 안정적입니다
이는 여러 번 정렬할 때 유용합니다
(예를 들어, 부서별로 정렬한 후에 급여 등급별로 정렬하기).
'''

# ==============================

'''
# EX 1) sort 함수의 stable을 보장하지 못하는 경우

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [Person("Alice", 30), Person("Bob", 25), Person(
    "Alice", 25), Person("hola", 25), Person("calli", 25)]

try:
    people.sort()
except TypeError as e:
    print(f"Error: {e}")


# 결과: 에러 발생
# Error: '<' not supported between instances of 'Person' and 'Person'

# 비교항목이 name과 age인 상황(다수 비교)에서 비교 대상에 동일한 항목이 (name - 'Alice') 있는 경우 에러 발생
'''

# ==============================

'''
# EX 2) sort 함수 비교 항목의 우선순위 지정 (key지정으로 age 우선)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [Person("Alice", 30), Person("Bob", 25), Person(
    "Alice", 25), Person("hola", 25), Person("calli", 25)]

# key 함수 정의


def sort_key(person):
    return (person.age, person.name)


# 정렬
people.sort(key=sort_key)

# 결과 출력
for person in people:
    print(f"{person.name}: {person.age}")

'''

# 결과
'''
Alice: 25
Bob: 25
calli: 25
hola: 25
Alice: 30
'''

# ==============================

''''''
# EX 3) sort 함수 비교 항목의 우선순위 지정 (key지정으로 name 우선)
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [Person("Alice", 30), Person("Bob", 25), Person(
    "Alice", 25), Person("hola", 25), Person("calli", 25)]

# key 함수 정의


def sort_key(person):
    return (person.name, person.age)


# 정렬
people.sort(key=sort_key)

# 결과 출력
for person in people:
    print(f"{person.name}: {person.age}")
'''

# 결과
'''
Alice: 25
Alice: 30
Bob: 25
calli: 25
hola: 25
'''

# ==============================

# EX 4) sorted 함수 비교 항목의 우선순위 지정 없음

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return (self.name, self.age) < (other.name, other.age)


people = [Person("Alice", 30), Person("Bob", 25), Person(
    "Alice", 25), Person("hola", 25), Person("calli", 25)]


# sorted() 함수 사용
sorted_people = sorted(people)

# 결과 출력
for person in sorted_people:
    print(f"{person.name}: {person.age}")
'''

# 결과
'''
Alice: 25
Alice: 30
Bob: 25
calli: 25
hola: 25
'''

# sorted()는 별도의 키 지정 없이도 정렬에 문제가 없음
# 다만 정렬 기준은 데이터를 기반으로 하게 되는 것으로 보임

'''
input을 아래와 같이 변경한 경우 
    people = [Person(30, "Alice"), Person(25, "Bob"), Person(
        25, "Alice"), Person(25, "hola"), Person(25, "calli")]
output의 정렬 기준이 변경됨을 확인
    25: Alice
    25: Bob
    25: calli
    25: hola
    30: Alice
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [Person("Alice", 30), Person("Bob", 25), Person(
    "Alice", 25), Person("hola", 25), Person("calli", 25)]

# key 함수 정의


def sort_key(person):
    return (person.age, person.name)


# sorted() 함수 사용
sorted_people = sorted(people, key=sort_key)

# 결과 출력
for person in sorted_people:
    print(f"{person.name}: {person.age}")


# 결과
'''
Alice: 25
Bob: 25
calli: 25
hola: 25
Alice: 30
'''

# sorted()도 sort와 동일하게 key 설정 가능
