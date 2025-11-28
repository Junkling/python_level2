# 제네레이터는 iter를 반환함
from collections import abc

from line_util import print_line

# 파이썬에서 반복 가능한 타입
# collections , text file, list, dict, set, tuple, unpacking, *args

print_line('제네레이터')
s = 'ABCDE'
print(dir(s))
print('dir(s) 에 iter가 있나? ', '__iter__' in dir(s))

for c in s:
    print(c)

print_line('제네레이터 내부 동작')
w = iter(s)
print('dir(s) 에 next가 있나? ', '__next__' in dir(w))
while True:
    try:
        print(next(w))
    except StopIteration:
        break

print('s iter?', hasattr(s, '__iter__'))
print('w iter?', hasattr(w, '__iter__'))

print('s extends Iterable?' , isinstance(s, abc.Iterable))
print('w extends Iterable?' , isinstance(w, abc.Iterable))

print_line('next 패턴')
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('call __next__')
        try:
            result = self._text[self._idx]
            self._idx += 1
            return result
        except IndexError:
            raise StopIteration('Iterator is empty')

    def __repr__(self):
        return 'WordSplitter({})'.format(repr(self._text))

ws = WordSplitter('Hello World!! study python')
print(ws)

while True:
    try:
        print(next(ws))
    except StopIteration as e:
        print(e.value)
        break


print_line('generator 패턴')
# 지능형 리스트/딕셔너리/집합 -> 데이터 양 증가 후 메모리 사용량 증가
# 메모리를 아끼기위해 제네레이터 사용 권장
# 단위 실행 가능한 코루틴

class WordSplitterGen:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            # 제네레이터
            yield word
        return

    def __repr__(self):
        return 'WordSplitterGen({})'.format(repr(self._text))

wg = WordSplitterGen('Hello World!! study python 22 33 44 55')


print(wg)
wg_gen = iter(wg)
while True:
    try:
        print(next(wg_gen))
    except StopIteration as e:
        break