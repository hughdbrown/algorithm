import collections
def rank(arr):
	"""
	>>> a = list(range(10))
	>>> print rank(a)
	[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
	>>> b = list(range(10))
	>>> b.reverse()
	>>> print rank(b)
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	>>> c = [5] * 10
	>>> print rank(c)
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	>>> d = ([5] * 5) + ([1] * 5)
	>>> d
	[5, 5, 5, 5, 5, 1, 1, 1, 1, 1]
	>>> print rank(d)
	[1, 1, 1, 1, 1, 6, 6, 6, 6, 6]
	"""
	d = collections.defaultdict(list)
	for i, v in enumerate(arr):
		d[v].append(i)
	result = [0] * len(arr)
	i = 0
	for k in sorted(d, reverse = True):
		for j in d[k]:
			result[j] = i + 1
		i += len(d[k])
	return result

if __name__ == '__main__':
	import doctest
	doctest.testmod()
