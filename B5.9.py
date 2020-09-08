from config import Time


# @Time.time_this(NUM_RUNS=10)
# with Time():
def f():
    for j in range(1000000):
        pass

f()