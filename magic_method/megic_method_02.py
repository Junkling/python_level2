# magic 메서드 = special 메서드
# 파이썬 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(built_in) 메서드 -> 언더바 두개로 시작 __


# 클래스 예제
class Vector(object):
    def __init__(self, *args):
        """
        create a vector , ex : v = Vector(1,2)
        """
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """
        :return the Vector Information
        """
        return '[Vector info] x:%s , y:%s' % (self._x, self._y)

    def __add__(self, other: "Vector") -> "Vector":
        Vector._type_check_(other, f'Vector 타입끼리만 덧셈이 가능합니다')
        return Vector(self._x + other._x, self._y + other._y)

    def __sub__(self, other: "Vector") -> "Vector":
        Vector._type_check_(other, f'Vector 타입끼리만 뺄셈이 가능합니다')
        return Vector(self._x - other._x, self._y - other._y)

    def __mul__(self, other: "Vector") -> "Vector":
        Vector._type_check_(other, f'Vector 타입끼리만 곱셈이 가능합니다')
        return Vector(self._x * other._x, self._y * other._y)

    def __bool__(self):
        return self is None or (self._x == 0 and self._y == 0)

    @staticmethod
    def _type_check_(inst, message):
        if not isinstance(inst, Vector): raise TypeError(message , type(inst))


print(Vector.__init__.__doc__)

v1 = Vector(5, 6)
v2 = Vector(23, 45)
v3 = Vector()

print(v1)
print(v2)
print(v3)

print(f'v1 + v2 : {v1 + v2}')
print(f'v1 - v2 : {v1 - v2}')
print(f'v1 * v2 : {v1 * v2}')
print(v1.__bool__())
print(bool(v2))
print(v3.__bool__())
print(v1 + 1)
print(v1 - 2)
