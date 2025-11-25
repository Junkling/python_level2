# 리스트 주의점 (깊은복사 얕은복사)
mark1 = [['~'] * 3 for n in range(4)]
print(mark1)

mark2 = [['~'] * 3] * 4
print(mark2)

# 수정

mark1[0][1] = 'X'
print('=' * 30, '{:^8}'.format('mark1'), '=' * 30)
print(mark1)
mark2[0][1] = 'X'
print('=' * 30, '{:^8}'.format('mark2'), '=' * 30)
print(mark2)

# 이유!! -> * (곱셈)은 같은 객체를 붙히는것!!
# 주소 값이 같음!!

print('=' * 30, '{:^8}'.format('reason'), '=' * 30)
print([id(a) for a in mark1])
print([id(a) for a in mark2])