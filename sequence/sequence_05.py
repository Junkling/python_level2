# 불변형 Dict
# Set 선언 최적화 방식
# Dict , Set 심화
from dis import dis
from types import MappingProxyType

d = {'key1': 'value1', 'key2': 'value2'}

# Read-only

d_frozen = MappingProxyType(d)
print(d_frozen)

# 수정 -> 에러
# d_frozen['key1'] = 'value2'
# 추가 -> 에러
# d_frozen['key3'] = 'value2'
# 변경 함수조차 없음
print(d_frozen)

# del d['key1']
d.__delitem__('key1')
print(d)

# Set

s1 = {'Apple', 'Orange', 'Banana', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Banana', 'Kiwi'])
s3 = {3}
# 아래는 dict 타입임
# s4 = {}
s4 = set()

s_frozen = frozenset(s1)

print(s1)
s1.add('Melon')
print(s1)

# 에러임
# s_frozen.add('Melon')
print(s_frozen)
print(set(s_frozen))

# 선언 최적화

print('=' * 10, '선언 최적화1', '=' * 10)

print('-' * 50)
# 여기선 frozenset이 먼저 만들어지네...??
print(dis("{'Apple', 'Orange', 'Banana', 'Kiwi'}"))
print('-' * 50)
print(dis("set(['Apple', 'Orange', 'Banana', 'Kiwi'])"))

print('=' * 10, '선언 최적화2', '=' * 10)
print('-' * 50)
print(dis("{10}"))
print('-' * 50)
print(dis("set([10])"))

from unicodedata import name
# 지능형 집합(Comprehending set)
print('=' * 10, 'Comprehending set', '=' * 10)
print({chr(i) for i in range(97, 123)})
print({name(chr(i), '') for i in range(0, 256)})