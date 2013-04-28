import itertools
from collections import OrderedDict


def groupby(criteria, sequence):
    groups = {}
    for elem in sequence:
        i = criteria(elem)
        if i in groups.keys():
            groups[i].append(elem)
        else:
            groups[i] = [elem]
    return groups


def iterate(func):
    element = lambda x: x
    for i in itertools.count():
        yield element
        element = compose(func, element)
        

def compose(func1,func2):
    return lambda *args: func1(func2(*args))


def zip_with(func, *args):
    if(len(args) == 0):
        return iter([])
    return iter(map(func, *args))


def cache(func, levels):

    if levels <= 0:
        return func

    result_cache = OrderedDict()

    def func_cached(*args):
        if args not in result_cache:
            if len(result_cache) >= levels:
                result_cache.popitem(False)
            result_cache[args] = func(*args)
        return result_cache[args]
    return func_cached