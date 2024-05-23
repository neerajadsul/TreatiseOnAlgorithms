import time


def timeit_wrapper(func, print_stdout=False):
    """Measures execution time using stopwatch.

    Args:
        func: _description_
    """
    print('Inside the timeit, above wrapper')
    def wrapper(*args, **kwargs):
        begin = time.time_ns()
        result = func(*args, **kwargs)
        ending = time.time_ns()
        total_time = (ending - begin)/1e9
        if print_stdout:
            print(f'{func.__name__} Total Time: {total_time:.1f}')
        return result, total_time
    print('Returning wrapper')
    return wrapper


def testing(how_long):
    """How long to sleep."""
    import time
    time.sleep(how_long)
    return f'Slept {how_long}s'

if __name__ == "__main__":
    result = timeit_wrapper(testing,True)(0.3)
    print(result)
    result = timeit_wrapper(testing,False)(0.3)
    print(result)
    # testing(.4)