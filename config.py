import time
from timeit import default_timer


class Time:
    def __enter__(self):
        self.t0 = default_timer()
        return self

    def __exit__(self, *args, **kwargs):
        self.t1 = default_timer()
        res = self.t1 - self.t0
        print(f'Среднее время выполнения: {res * 1000} секунд.')
    
    def time_this(NUM_RUNS):
        def decorator(func):
            def wrapper():
                avg_time = 0
                for i in range(NUM_RUNS):
                    t0 = time.time()
                    res = func()
                    t1 = time.time()
                    avg_time += t1 - t0
                print(f'Среднее время выполнения: {avg_time / NUM_RUNS} секунд.')
                return res
            return wrapper
        return decorator