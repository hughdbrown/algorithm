# Inspired by thispost:
#   http://lazypython.blogspot.com/2008/11/timeline-view-in-django.html
# Also of interest:
#   http://wordaligned.org/articles/merging-sorted-streams-in-python

from operator import itemgetter

def merge(*querysets, **kwargs):
    field = kwargs.pop('field')
    if field is None:
        raise TypeError('you need to provide a key to do comparisons on')
    key = itemgetter(field)
    # Assume the lists are not initially sorted
    qs = [sorted(x, key=key) for x in querysets]
    while len(qs) > 1:
        #q1, q2 = qs.pop(0), qs.pop(0)
        #q3 = merge_lists(q1, q2, key)
        #qs.append(q3)
        qs.append(merge_lists(qs.pop(0), qs.pop(0), key))
    return qs.pop()

def merge_lists(left, right, key):
    result = []
    while (len(left) and len(right)):
        which_list = (left if key(left[0]) <= key(right[0]) else right)
        result.append(which_list.pop(0))
    return result + left + right

if __name__ == '__main__':
    a = [{'k':i, 'v':2*i} for i in range(10)]
    b = [{'k':i, 'v':3*i} for i in range(10)]
    c = [{'k':i, 'v':5*i} for i in range(10)]
    d = [{'k':i, 'v':7*i} for i in range(10)]
    e = [{'k':i, 'v':11*i} for i in range(10)]
    query = (a, b, c, d, e)
    d = {'field' : 'v'}
    for merged_dict in merge(*query, **d):
        print merged_dict

