# Tuple Advanced
# unpacking
from typing import List

print('=' * 40)

# b,a = a,b
a = 10
b = 20

b, a = a, b
print(a, b)

print(divmod(a, b))
print(divmod(*(a, b)))
print(*divmod(*(a, b)))
print('=' * 40)

# x, y , rest = range(10)
# 예상(x = 0 , y = 1, rest = 2)
# 위 방식은 에러
x, y, *rest = range(10)

print(x, y, rest)

*x, y, rest = range(10)
print(x, y, rest)

x, *y, rest = range(10)
print(x, y, rest)

x, y, *rest = range(2)
print(x, y, rest)

print(x, y, rest)

x, y, *rest = 1, 2, 3, 4, 5, 6
print(x, y, rest)
print('=' * 40)

# Mutable(가변) vs Immutable(불변)
l = (10, 15, 20)
m = [10, 15, 20]

print(l, id(l))
print(m, id(m))

print('=' * 40)
l = l * 2
m = m * 2
print(l, id(l))
print(m, id(m))

# 가변형인 리스트는 같은 id 공간에 원소가 추가되지만
# 불변형인 튜플은 새로운 메모리 공간을 할당하여 재생성
print('=' * 40)
l *= 2
m *= 2
print(l, id(l))
print(m, id(m))

# sort vs sorted
str_list1 = ['z', 'x', 'y', 'c', 'd', 'w', 'v', 'n', 'm']

# sorted -> 정렬후 새 객체
print('=' * 20, 'sorted', '=' * 20)

sorted1 = sorted(str_list1)
sorted2 = sorted(str_list1, key=lambda x: x[-1])
sorted3 = sorted(str_list1, key=lambda x: x[-1], reverse=True)
sorted_reverse = sorted(str_list1, reverse=True)
print('sorted1 = ', sorted1)
print('sorted2 = ', sorted2)
print('sorted3 = ', sorted3)
print('sorted_reverse = ', sorted_reverse)
print('origin = ', str_list1)

# sort -> 정렬후 객체 직접 변경
# --- 아하! 그래서 같은 리스트를 참조해서 변수 선언시 하나만 변경해도 전체가 정렬되었구나
temp_list1 = str_list1
temp_list2 = str_list1

print('=' * 20, 'sort', '=' * 20)
print('sort() temp_list1')
temp_list1.sort()
# temp_list1.sort(key=len)
# temp_list1.sort(key=lambda x: x[-1])
# temp_list1.sort(reverse=True)
# str_list1.sort()
print('temp_list1 = ', temp_list1)
print('temp_list2 = ', temp_list2)
print('str_list1 = ', str_list1)

# List vs Array
# 리스트 기반 :융통성 + 자유로운 자료형, 범용성
# 숫자 기반 : array

# 모듈을 통한 제네릭 사용
nums = List[int]
