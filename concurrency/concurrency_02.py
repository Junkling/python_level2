# 병행성(Concurrency) : 하나의 리소스가 여러 작업을 동시 수행
# 병렬성(Parallelism) : 여러 리소스가 여러 작업을 동시에 수행
import time

from line_util import print_line

print_line('generator_ex1')
def generator_ex1():
    print('Start ex1()')
    yield 'A point'
    print('Continue ex1()')
    yield 'B point'
    print('End ex1()')

tmp = iter(generator_ex1())
#
# print(tmp)

while True:
    try:
        print(tmp.__next__())
    except StopIteration:
        break
    finally:
        time.sleep(1)

for v in generator_ex1():
    print(v)
    time.sleep(1)

print_line('yield은 리턴값')
tmp2 = [x * 3 for x in generator_ex1()] # -> yield가 리턴값으로 반환된다.
tmp3 = (x * 3 for x in generator_ex1())

print(tmp2)
print(tmp3)

for i in tmp2:
    print(i)

for i in tmp3:
    print(i)

# Generator Ex3(중요 함수)
# filterfalse, accumulate, chain, product, groupby
print_line('count')

import itertools

# 무한대로 늘어나는 기능
g1 = itertools.count(1, 2.5)

while True:
    next_g = next(g1)
    if next_g > 100:
        break
    print(next_g)

print_line('takewhile')

g2 = itertools.takewhile(lambda x: x < 50, itertools.count(1, 2.5))


for i in g2:
    print(i)

print_line('filterfalse')
# filter의 반대
g3 = itertools.filterfalse(lambda x: x > 30, range(1 ,100))

for i in g3:
    print(i)

print_line('accumulate')
# 추적 합계
g4 = itertools.accumulate([i for i in range(1 ,30, 2)])

print(list(g4))


print_line('chain1')
# 연결
g5 = itertools.chain('ABCDEFG' , range(1 ,40, 3))

print(list(g5))

print_line('chain2')
# 연결
g6 = itertools.chain(enumerate('ABCDEFG'))

print(list(g6))

print_line('product1')
# 개별
g7 = itertools.product('ABCDEFG')

print(list(g7))
print_line('product2')
# 경우의 수
g8 = itertools.product('ABCDEFG',repeat=2)

print(list(g8))
print_line('product3')
# 경우의 수
g9 = itertools.product('ABCDEFG',repeat=4)

print(list(g9))

# 그룹화
g9 = itertools.groupby('AAAABBBCCCDDDERRRREAADDGQQQFF')
for c, g in g9:
    print(c ,' : ', list(g))
# print(list(g9))
