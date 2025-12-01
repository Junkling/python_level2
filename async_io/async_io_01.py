# Async I/O
# 비동기 I/O 작업
# Generator -> 반복 객체 Return
# Non-blocking 비동기

# Blocking vs Non-blocking
# Blocking : 호출된 함수가 작업이 완료 될때까지 제어권을 가지고 있음 (스텍 구조)
# Non-blocking : 호출된 함수가(서브루틴) return 후 호출한 함수(메인 루틴)에 제어권 전달 -> 타 함수는 일 지속


# 쓰레드 단점 : 디버깅, 자원 접근 레이스 컨디션, 데드락 고려해야함
# 코루틴 -> 하나의 루틴만 실해아-> 락 필요 없음 -> 제어권으로 실행 , 사용 함수가 비동기로 구현 되어있어야 함

import asyncio
import threading
import timeit
import urllib.request
import concurrent.futures
from urllib.request import urlopen

from bs4 import BeautifulSoup

start = timeit.default_timer()

urls = ['https://www.daum.net/', 'https://www.naver.com/', 'https://www.inflearn.com/', 'https://www.youtube.com/',
        'https://www.tistory.com/']


async def main():
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    # future 객체 모아서 gather에서 한번에 실행
    futures = [asyncio.ensure_future(fetch(url, executor)) for url in urls]
    rst = await asyncio.gather(*futures)
    print()
    print('main result = ', rst)


async def fetch(url, executor):
    print(f'thread {str(threading.current_thread())} start , url = {url}')
    res = await loop.run_in_executor(executor, urlopen, url)
    print(f'thread {str(threading.current_thread())} done , url = {url}')
    # return res.read()[0:5]
    soup = BeautifulSoup(res.read(), 'html.parser')

    title_text = soup.title
    return title_text
    # return title_text.text

    # title_text1 = soup.find_all('title')
    # return title_text1[0]
    # return title_text1[0].text



if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    duration = timeit.default_timer() - start
    print(f'duration = {duration}')
