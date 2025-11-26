# 일급함수 (일급객체)
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달
# 4. 함수 결과 반환 가능
from functools import reduce, partial
from operator import add, mul


def factorial(n):
    """
    Factorial function -> n : int
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)


class A:
    pass


print(factorial(5))
print(factorial.__doc__)
# 타입은 function 이라는 객체
print(type(factorial))
print(type(A))

print(dir(factorial))

print('함수에만 있는 메직 메서드')
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))

print(factorial.__name__)
print(factorial.__code__)

# 변수에 할당
print('-' * 50)

var_func = factorial

print(var_func(10))
print(list(map(var_func, range(1, 11))))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수
# map , filter, reduce

print([var_func(i) for i in range(1, 6) if i % 2])

print(list(map(var_func, filter(lambda i: i % 2, range(1, 6)))))

# reduce
print(sum(range(1, 11)))
print(reduce(add, range(1, 11)))

print(reduce(lambda acc, cur: acc + str(cur), range(1, 11), ""))

# 익명함수 lambda
# 주석으로 해석 추가
# 가급적 함수로

print(reduce(lambda n, cur: n + cur, range(1, 11)))
print(reduce(lambda n, cur: n + cur, range(1, 11), 0))

# Callable : 호출 연산자 -> 메서드 형태로 호출 가능한지 여부

print(callable(str))
print(callable(var_func))
print(callable(A))
print(callable(list))

# partial 사용법 : 인수고정 -> 콜백 함수 사용

mul(10,10)

five = partial(mul , 5)
six = partial(five , 6)

print(five(10))
print(five(20))

print(six())
# 아래는 에러 (인자가 더 많이 들어왔다)
# print(six(10))

print([five(i) for i in range(1, 10)])
print(list(map(five, range(1, 10))))