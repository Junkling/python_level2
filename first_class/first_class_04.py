# 데코레이터
# 장점 : 중복 제거
# -> 공통 함수를 데코레이터 패턴으로 구현시 강력함 (공통 기능)
# 단점 :
# -> 디버깅 및 리펙토링이 어려워질 수 있음
import time

from line_util import print_line


def func_run_time(func):
    def perf_clocked(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        name = func.__name__
        arg_str = ', '.join(str(s) for s in args)
        print('[{}소요] {}~{}\n{}({})'.format(end - start, start, end, name, arg_str))
        return result

    return perf_clocked


def func_ex(seconds):
    print('{} seconds'.format(seconds))
    time.sleep(seconds)


def sum_func_ex(*num):
    return sum(num)


# 데코레이터 미사용
print_line('일반 함수')

func_ex(2)
print(sum_func_ex(1, 2, 3, 5, 8, 8, 9))

# 함수로 래핑하는 방식
print_line('함수로 래핑')
time_check_ex = func_run_time(func_ex)
time_check_sum = func_run_time(sum_func_ex)

time_check_ex(1)
time_check_sum(*(range(1, 1000)))

print_line('데코레이터')


@func_run_time
def func_ex_deco(seconds):
    print('{} seconds'.format(seconds))
    time.sleep(seconds)


@func_run_time
def sum_func_ex_deco(*num):
    return sum(num)


func_ex_deco(1)
sum_func_ex_deco(*(range(1, 1000)))
