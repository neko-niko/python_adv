import time
def time_count(func):
    def work(*args):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        arg_str = ','.join(str(arg) for arg in args)
        print("[%0.8fs] %s(%s) -> %s" % (end - start, func.__name__, arg_str, result))
        return result
    return work
