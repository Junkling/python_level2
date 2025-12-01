# 동시성
# 비동기 작업 처리
# 파이썬 GIL
# 지연시간(Block) CPU 및 리소스 나이 방지 -> Network , I/O 관련 작업 -> 동시성 활용 권장

# concurrent.futures
# 1. 멀티스레딩 / 멀티 프로세싱 API 통일 -> 쉽게 변환 가능하도록 지원
# 2. 실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백 추가, 동기화 코드 쉽게 구현 가능 -> Promise


# GIL : global interpreter lock -> 두개의 쓰레드가 동시에 실행될 때 하나의 자원을 엑세스 하는 경우와 같은 문제점을 방지하기 위해 리소스 전체에 락을 검 -> 컨텍스트 스위칭
#   - 우회 방법 : 멀티프로세싱 사용, CPython


# 3.2 버전 이하 구현시
# import threading
# import multiprocessing


# 1. map 예시
import os
import time
from concurrent import futures

WORK_LIST = [100000, 1000000, 10000000, 100000000]


# 동시성 합계 계산 메인 함수
# 제네레이터로 구현
def sum_gen(n):
    return sum(i for i in range(1, n + 1))


def main():
    worker = min(10, len(WORK_LIST))
    result = []

    st = time.time()

    # 프로세스 할당 , 쓰레드 할당
    # with futures.ProcessPoolExecutor(max_workers=worker) as executor:
    with futures.ThreadPoolExecutor(max_workers=worker) as executor:
        # map은 작업 순서를 유지하고 즉시 실행됨
        result = executor.map(sum_gen, WORK_LIST)

    et = time.time()

    msg = '\n result :{} , time : {}'
    print(msg.format(list(result), et - st))

if __name__ == '__main__':
    main()