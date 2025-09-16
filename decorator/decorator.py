import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func()
        end = time.time()
        print(f"{func.__name__} takes {int((end-start)*1000)} msec")
        return result
    return wrapper    
    
@time_it
def some_op():
    print('starting..')
    time.sleep(1)
    print('we are done')
    return

some_op()