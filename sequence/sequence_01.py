# 시퀀스 타입 & 시퀀스 자료구조
from array import array

# 자료형 형태 :
# 1. 컨테이너(Container : 서로 다른 자료형 -> [list, tuple , collections , deque]
ca1 = [3, 3.0, 'a']
print(ca1)

# 2. 플랫(Flat : 한개의 자료형 -> [str , bytes, bytearray, array , memoryview]

# 아래 형태는 에러
# fa1 = array([3, 3.0, 'a'])
fa_int = array('i', [3, 5, 6])
fa_str = array('u', ['3', '5', '6'])
fa_str2 = array('u', [chr(42), chr(99), chr(64)])
print(list(fa_int))
print(list(fa_str))
print(list(fa_str2))

# 가변 (list, bytearray, array.array, memoryview, deque)
# 불변 (tuple, str, byte)

chars = ')(*&^$#@!'
chr_list = list(ord(char) for char in chars)
chr_list1 = [ord(char) for char in chars]
chr_list2 = []
for char in chars:
    chr_list2.append(ord(char))
print(chr_list)
print(chr_list1)
print(chr_list2)

# Comprehending Lists + Map, Filter

filter_chr_list1 = list(filter(lambda num: num > 40, list(ord(char) for char in chars)))
filter_chr_list2 = [ord(char) for char in chars if ord(char) > 40]
filter_chr_list3 = list(filter(lambda num: num > 40, map(ord, chars)))

print(filter_chr_list1)
print(filter_chr_list2)
print(filter_chr_list3)

print(list(map(chr, filter_chr_list1)))
print([chr(n) for n in filter_chr_list2])

print('=' * 20, 'generator', '=' * 20)
# Generator : 한번에 한개의 항목 생성(메모리 유지하지 않음)
tuple_gen = (ord(char) for char in chars)


def call_gen_next(gen):
    try:
        return next(gen)  # 값 있음
    except StopIteration:
        return 'is end'


print(tuple_gen)
print(type(tuple_gen))
print(dir(tuple_gen))

print(call_gen_next(tuple_gen))
print(call_gen_next(tuple_gen))
print(call_gen_next(tuple_gen))
print(call_gen_next(tuple_gen))
print(call_gen_next(tuple_gen))
print(call_gen_next(tuple_gen))
print(call_gen_next(tuple_gen))
print(call_gen_next(tuple_gen))
print(call_gen_next(tuple_gen))
print(call_gen_next(tuple_gen))
print(call_gen_next(tuple_gen))
print(call_gen_next(tuple_gen))
print(call_gen_next(tuple_gen))

print('=' * 20, 'array', '=' * 20)
arr_gen = array('i', (ord(char) for char in chars))

print(arr_gen)
print(type(arr_gen))
print(arr_gen.tolist())

# 제네레이터 예제
print('=' * 20, '제네레이터 1', '=' * 20)

print(('%s' % c + str(n) for n, c in enumerate(['A', 'B', 'C', 'D', 'E'])))

for s in ('%s' % c + str(n) for n, c in enumerate(['A', 'B', 'C', 'D', 'E'])):
    print(s)


print('=' * 20, '제네레이터 2', '=' * 20)
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D', 'E']) for n in range(10))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D', 'E'] for n in range(10)):
    print(s)
