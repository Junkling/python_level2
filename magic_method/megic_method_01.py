# magic 메서드 = special 메서드
# 파이썬 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(built_in) 메서드 -> 언더바 두개로 시작 __

# 기본형

print(int)
print(float)

print(dir(int))
print(dir(float))

# int 선언
n = 10
print(type(n))

print(n + 100)
print(n.__add__(100))
# print(n.__doc__)

print(n.__bool__(), bool(n))
print(n.__mul__(100), n * 100)

print()

# 클래스 예제
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return f'Fruit Info : {self._name}, {self._price}'

    def __add__(self, x):
        return self._price + x._price

    def __sub__(self, x):
        return self._price - x._price

    def __le__(self, other):
        return self._price <= other._price

    def __gt__(self, other):
        return self._price > other._price

f1 = Fruit('Apple', 2000)
f2 = Fruit('Banana', 1000)

print(f1+f2)
print(f1.__add__(f2))

print()

print(f1-f2)
print(f1.__sub__(f2))

print()

print(f1>f2)
print(f1.__gt__(f2))
print()

print(f1<=f2)
print(f1.__le__(f2))