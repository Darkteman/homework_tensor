import time


def func_time(func):
    def wrapper():
        start_time = time.time()
        result = func()
        execution_time = round(time.time() - start_time, 4)
        print(f'Функция {func.__name__} выполнялась {execution_time} сек')
        return result
    return wrapper()


@func_time
def sleep_one_sec():
    time.sleep(1)
