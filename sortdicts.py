#!/usr/bin/env python

def sortdicts(sort_field, *iterables):
    from itertools import chain
    from operator import itemgetter
    return sorted(chain(*iterables), key=itemgetter(sort_field))
    
if __name__ == '__main__':
    a = [{'k':i, 'v':2*i} for i in range(10)]
    b = [{'k':i, 'v':3*i} for i in range(10)]
    c = [{'k':i, 'v':5*i} for i in range(10)]
    d = [{'k':i, 'v':7*i} for i in range(10)]
    e = [{'k':i, 'v':11*i} for i in range(10)]
    query = (a, b, c, d, e)
    for d in sortdicts('v', *query):
        print d
