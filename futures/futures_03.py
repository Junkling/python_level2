# 2-2. as_completed 예시

import os
import time
from concurrent import futures
from concurrent.futures import wait

WORK_LIST = [10000000, 10000, 1000000, 100000]


# 동시성 합계 계산 메인 함수
# 제네레이터로 구현
def sum_gen(n):
    return sum(i for i in range(1, n + 1))


def main():
    worker = min(10, len(WORK_LIST))

    st = time.time()
    future_list = []

    # 프로세스 할당 , 쓰레드 할당
    # with futures.ProcessPoolExecutor(max_workers=worker) as executor:
    with futures.ThreadPoolExecutor(max_workers=worker) as executor:
        for work in WORK_LIST:
            # 이시점에 실행되지 않고 예정 작업만 반환 (스케쥴링(
            future = executor.submit(sum_gen, work)
            future_list.append(future)
            print(f'Scheduled {work} , {future}')
            print()

        for future in futures.as_completed(future_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled()

            print(f'Future result : {result} , done : {done}')
            print(f'Future cancel : {cancelled}')


    #     as_completed



    et = time.time()
    msg = '\ntime : {}'
    print(msg.format(et - st))

if __name__ == '__main__':
    main()