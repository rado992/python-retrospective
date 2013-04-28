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


CACHE = OrderedDict()


def cache(func, levels):

    def func_cached(*args):
        if args not in CACHE:
            if len(CACHE) >= levels:
                CACHE.popitem(False)
            CACHE[args] = func(*args)
        return CACHE[args]
    return func_cached