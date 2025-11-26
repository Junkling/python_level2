# 외부에서 호출 된 함수의 변수값, 상태, 레퍼런스 등을 복사한 후에 저장
from line_util import print_line

print_line('closure_ex_1')
def closure_ex_1():
    series = []

    def averager(value):
        series.append(value)
        print(f'Averaging = {series, len(series)}')
        return sum(series) / len(series)

    return averager


averager1 = closure_ex_1()
print(averager1(10))
print(averager1(20))
print(averager1(20))
print(averager1(30))
print(averager1(40))
print(averager1(50))
print(averager1(60))
print(averager1(70))

print_line('closure_ex_2')
def closure_ex_2():
    series = []

    def averager(value1, value2):
        series.append(value1 + value2)
        print(f'Averaging = {series, len(series)}')
        return sum(series) / len(series)

    return averager


averager2 = closure_ex_2()
print(averager2(10, 10))
print(averager2(20, 10))
print(averager2(20, 10))
print(averager2(30, 10))
print(averager2(40, 10))
print(averager2(50, 10))
print(averager2(60, 10))
print(averager2(70, 10))

print_line('dir()')
print(dir(averager1))
print(dir(averager2))
print_line('__code__')
print(dir(averager1.__code__))
print(dir(averager2.__code__))
print_line('co_freevars')
print(averager1.__code__.co_freevars)
print(averager2.__code__.co_freevars)

print_line('cell_contents')
print(averager1.__closure__[0].cell_contents)
print(averager2.__closure__[0].cell_contents)

# 잘못된 예시
print_line('잘못된 예시')

def closure_ex_3():
    cnt = 0
    total = 0

    def averager(value):
        # 로컬변수가 아닌 값을 참조할 수 있음
        nonlocal cnt ,total
        total += value
        cnt += 1
        print(f'Averaging = {total} / {cnt}')

        return total / cnt

    return averager


ex_3 = closure_ex_3()

print(ex_3(10))
print(ex_3(20))
print(ex_3(30))
print(ex_3(40))