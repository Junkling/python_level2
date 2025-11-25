# HashTable
# key , value 형식 -> key 값을 해싱 함수로 해쉬 주소를 부여하여 key로 바로 접근
# key 값 중복 불가
# dict -> 해시테이블
# print(__builtins__.__dict__)

t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# 가변한 원소가 포함된 t2는 hash값이 부여되지 않음
# print(hash(t2))
print()

# Dict Setdefault

src = (('k1', 'val1'), ('k1', 'val2'), ('k2', 'val3'), ('k2', 'val4'), ('k2', 'val5'))


# 중복시 리스트로 바꾸기 방식
print('='*20 , '합하기 방식', '='*20)

d1 = dict()
for t in src:
    d1.setdefault(t[0], []).append(t[1])

print(d1)
d1_1 = dict()
for k, v in src:
    d1_1.setdefault(k, []).append(v)

print(d1_1)

d3 = dict()

for t in src:
    if t[0] not in d3:
        d3[t[0]] = [t[1]]
    else:
        d3[t[0]].append(t[1])

print(d3)

d3_1 = dict()

for k, v in src:
    if k not in d3_1:
        d3_1[k] = [v]
    else:
        d3_1[k].append(v)

print(d3_1)


# 아래 두 방식은 덮어쓰기

print('='*20 , '덮어쓰기 방식', '='*20)
d2 = dict()

for t in src:
    d2.update({t[0]: t[1]})

print(d2)

d2_1 = {k: v for k, v in src}
print(d2_1)