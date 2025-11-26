# 클로저
# - 변수 범위
# - 글로벌 선언
# - 클로저 사용 이유
# - 클레스 -> 클로저 구현
import uuid

from line_util import print_line

# 변수 범위

print_line('func_v1')


def func_v1(a):
    print(a)
    # 변수가 없어 에러
    # print(b)


func_v1(2)

print_line('func_v2')
b = 20


def func_v2(a):
    print(a)
    print(b)


func_v2(10)

print_line('func_v3')

c = 30


def func_v3(a):
    global c
    print(a)
    # 변수선언보다 사용이 먼저되어서 에러
    print(c)
    c = 40


print('global before func = ', c)

func_v3(10)

print('global after func = ', c)

# 클로져
# 사용 이유 : 함수 영역에서 선언된 값을 유지하고 있는다
# 동시성 제어 -> 메모리 공간의 교착상태를 만들지 않기 위해 메시지도 전달 하기 위한 기능
# 클로저는 공유되지만 변경은 불가 (Immutable , Read only)
# 클로저는 불변자료구조(atomic , stm) -> 멀티스레드(Coroutine) 프로그레밍에 강점
print_line('closure')

a = 100
print(a + 100)
print(a + 1000)

print(sum(range(1, 51)))
print(sum(range(51, 100)))

print_line('Averager')


# 별거 아니고 호출시 배열로 값을 관리할 수 있게 한다.
class Averager:
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print(f'inner {self._series}/{self._series.__len__()}')
        return sum(self._series) / len(self._series)


averager = Averager()

print('\n', '-' * 10)
print(dir(averager))

print('\n', '-' * 10)
print('dict : ', averager.__dict__)
print(averager(10))

print('\n', '-' * 10)
print('dict : ', averager.__dict__)
print(averager(30))

print('\n', '-' * 10)
print('dict : ', averager.__dict__)
print(averager(80))

print('\n', '-' * 10)
print('dict : ', averager.__dict__)
print(averager(70))

print_line('ClosureEx')


class ClosureEx:
    series = []
    _name: str
    _age: int

    def __init__(self, *args):
        self._name, self._age = args
        self._series = []
        ClosureEx.series.append(id(self))

    def __call__(self):
        self._series.append(uuid.uuid1())
        print(f'inner inst id = {id(self)} , {self._series}')


ce1 = ClosureEx('KIM', 10)
ce2 = ClosureEx('LEE', 20)
ce3 = ClosureEx('PARK', 30)

print('\n', '-' * 5, 'dir', '-' * 5)
print('\n', dir(ce1))

print('\n', '-' * 5, 'ce1', '-' * 5)
ce1()
ce1()
ce1()
print('dict : ', ce1.__dict__)
print(ClosureEx.series)

print('\n', '-' * 5, 'ce2', '-' * 5)
ce2()
ce2()
ce2()
print('dict : ', ce2.__dict__)
print(ClosureEx.series)

print('\n', '-' * 5, 'ce3', '-' * 5)
ce3()
ce3()
ce3()
print('dict : ', ce3.__dict__)
print(ClosureEx.series)
