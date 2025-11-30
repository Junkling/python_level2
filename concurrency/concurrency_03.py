# 쓰레드 : os 에서 관리되는 리소스 (cpu 코어에서 실시간, 시분할 비동기 작업 -> 멀티 쓰레드)
# 코루틴 : 하나의 쓰레드에서, 스텍을 기반으로 동작하는 비동기 작업
# yield를 통한 메인 서브 상호작용
# 코루틴 제어, 상태, 양방향 전송
# 서브 루틴 : 메인루틴 호출 -> 서브루틴에서 수행(흐름제어)
# 코루틴 : 루틴 실행 중 중지 -> 동시성 프로그래밍 -> 쓰레드에 비해 오버헤드 감소
# 쓰레드 : 싱글쓰레드 , 멀티쓰레드 -> 복잡 (자원 공유, 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가)

# def -> async , yield -> await

# 코루틴 예제 1

def coroutine():
    print('start >> coroutine')
    i = yield
    print(f'received >> coroutine : {i}')

# 제네레이터 선언
cr1 = coroutine()
print(cr1)
print(type(cr1))
next(cr1)

# send 는 yield 에 파라미터를 할당함
# cr1.send(100)

# 잘못된 사용
# cr2 = coroutine()
# cr2.send(1000)

# 코루틴 예시 2
# GEN_CREATED : 처음 대기상태
# GEN_RUNNING : 실행상태
# GEN_SUSPENDED : Yield 대기 상태
# GEN_CLOSED : 실행 완료 상태

from inspect import getgeneratorstate

def coroutine2(x):
    print('start >> coroutine2 : {}'.format(x))
    y = yield x
    print(f'received >> coroutine 2-1 : {y}')
    z = yield x + y
    print(f'received >> coroutine 2-2 : {z}')
    t = yield

cr3 = coroutine2(10)
print(cr3)
print(getgeneratorstate(cr3))
print(next(cr3))
print(getgeneratorstate(cr3))
print(cr3.send(20))
print(getgeneratorstate(cr3))
print(cr3.send(10))
print(getgeneratorstate(cr3))

# 코루틴 예제 3
# StopIteration 자동 처리(3.5 이상 -> await)
def coroutine3():
    for x in 'ABCDEFG':
        yield x
    for y in range(1,5):
        yield y

c4 = coroutine3()
print(next(c4))
print(next(c4))
print(next(c4))
print(next(c4))
print(next(c4))
print(next(c4))
print(next(c4))
print(next(c4))
print(next(c4))
print(next(c4))
print(next(c4))
# print(next(c4))

c5 = coroutine3()
print(list(c5))


def coroutine4():
    yield from 'ABCDEFG'
    yield from range(1,5)

c6 = coroutine4()


print(next(c6))
print(next(c6))
print(next(c6))
print(next(c6))
print(next(c6))
print(next(c6))
print(next(c6))
print(next(c6))
print(next(c6))
print(next(c6))
print(next(c6))
# print(next(c6))
