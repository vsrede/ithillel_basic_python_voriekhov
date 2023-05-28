import time
import functools
from collections import OrderedDict
import requests


def profile(msg="Elapsed time for function"):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            start = time.time()
            deco._num_call += 1
            result = f(*args, **kwargs)
            deco._num_call -= 1

            if deco._num_call == 0:
                print(msg, f'{f.__name__}: {time.time() - start}s')
            return result

        deco._num_call = 0
        return deco

    return internal


def cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            
            if cache_key in deco._cache:
                # переносимо в кінець списку
                deco._cache.move_to_end(cache_key, last=True)
                return deco._cache[cache_key]

            result = f(*args, **kwargs)
            # видаляємо якшо досягли ліміта
            if len(deco._cache) >= max_limit:
                # видаляємо перший елемент
                deco._cache.popitem(last=False)
            deco._cache[cache_key] = result
            return result

        deco._cache = OrderedDict()
        return deco

    return internal


# @profile(msg='Elapsed time')
@cache
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


print(fetch_url('https://google.com'))
print(fetch_url('https://google.com'))
print(fetch_url('https://google.com'))
print(fetch_url('https://ithillel.ua'))
print(fetch_url('https://dou.ua'))
print(fetch_url('https://ain.ua'))
