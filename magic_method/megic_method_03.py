# 파이썬 데이터 모델
import math
from collections import namedtuple

# 일반 튜플
p1 = (1.0, 5.0)
p2 = (2.5, 1.5)

length_1 = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

print(length_1)

# 띄어쓰기 기준 구분
Point = namedtuple('Point', 'x y')

p3 = Point(1.0, 5.0)
p4 = Point(2.5, 1.5)

length_2 = math.sqrt((p3[0] - p4[0]) ** 2 + (p3[1] - p4[1]) ** 2)
length_3 = math.sqrt((p3.x - p4.x) ** 2 + (p3.y - p4.y) ** 2)
print(length_2)
print(length_3)

Point2 = namedtuple('Point', ['x', 'y'])
Point3 = namedtuple('Point', 'x, y')
Point4 = namedtuple('Point', 'x y')
# 예약어를 쓰려면 옵션 줘야함
# 키값이 중복되면 _2,_3 등으로 빠짐
Point5 = namedtuple('Point', 'x y x class', rename=True)

print(Point2, Point3, Point4, Point5)

point2 = Point2(x=1, y=2)
point3 = Point3(1, 2)
point4 = Point4(1, y=2)
point5 = Point5(1, 2, 3, 4)

# Dict to Unpacking
temp_dict = {
    'x': 75,
    'y': 90
}
# 튜플은 * dict는 **
point6 = Point2(**temp_dict)

print(point2, point3, point4, point5, point6)

x, y = point6

# _make() : 객체 생성
temp = [1.5, 2.3]
point7 = Point2._make(temp)
print(point7)

# _field() : 필드 네임 확인
print(point7._fields)

# _asdict() : OrderedDict 반환
print(point2._asdict())
print(point5._asdict())
print(point6._asdict())

# 실사용 예시

Classes = namedtuple('Classes', ['rank', 'number'])

numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split(' ')

print(numbers)
print(ranks)

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print(len(students))
print(students)

students2 = [Classes(rank, number)
             for rank in 'A B C D'.split(' ')
             for number in [str(n)
                            for n in range(1, 21)]]

print(len(students2))
print(students2)