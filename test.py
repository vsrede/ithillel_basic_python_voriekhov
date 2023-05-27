import psutil
import os
import tracemalloc
from memory_profiler import profile


def memory_usage(func):
    def another_func(*args, **kwargs):
        start = psutil.Process(os.getpid()).memory_info().rss
        result = func(*args, **kwargs)
        end = psutil.Process(os.getpid()).memory_info().rss
        use = end - start
        print(f'Usage memory: {use}')

        return result

    return another_func


@memory_usage
def word_to_list(word):
    lst = [x for x in word]
    return lst


def memory_usage_1(func):
    def another_func(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        print(f'Usage memory: {tracemalloc.get_traced_memory()}')
        tracemalloc.stop()

        return result

    return another_func


@memory_usage_1
def word_to_list_1(word):
    lst = [x for x in word]
    return lst


@profile
def word_to_list_2(word):
    lst = [x for x in word]
    return lst


word_to_list('mutants')
word_to_list_1('mutants')
word_to_list_2('mutants')




