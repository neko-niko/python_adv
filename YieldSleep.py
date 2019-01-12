import time
import asyncio
def yield_sleep():
    time1 = time.time()
    while time.time() - time1 < 1:
        yield
    return

@asyncio.coroutine
def test1():
    print(1)
    # sleep = yield_sleep()
    yield from yield_sleep()
    # x = yield from yield_sleep()
    print(2)