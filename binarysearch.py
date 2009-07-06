
# This is a correct binary search with a minimum number of comparisons in the loop
# See blog post:
#	http://www.iwebthereforeiam.com/iwebthereforeiam/2009/07/binary-search-coding-test.html
def binarysearch(iter, val):
	lo, hi = 0, len(iter)-1
	while lo <= hi:
		mid = lo + (hi - lo) / 2
		if iter[mid] >= val :
			hi = mid - 1
		else:
			lo = mid + 1
	return (lo if iter[lo] == val else -1)

# This is also correct but less efficient because it has an extra comparison
def binarysearch2(iter, val):
	lo, hi = 0, len(iter)-1
	while lo <= hi:
		mid = lo + (hi - lo) / 2
		if iter[mid] == val :
			return mid
		elif iter[mid] > val:
			hi = mid - 1
		else:
			lo = mid + 1
	return -1

# This driver does not necessarily still work.
# Too much mucking with code.
if __name__ == "__main__":
	j, k = 0, 0 
	#def test_search(arr, val):
	#	j = binarysearch(arr, val)
	#	if j == -1 or arr[j] != val:
	#		print "Error at ", val
	#	j = binarysearch2(arr, val)
	#	if j == -1 or arr[j] != val:
	#		print "Error at ", val
	def test_search(arr, val):
		global j, k
		j += binarysearch(arr, val)
		k += binarysearch2(arr, val)

	from random import randint
	for _ in range(2000):
		a = sorted(randint(1,38) for _ in range(200))
		#a = list(range(200))
		for i, elem in enumerate(a):
			test_search(a, elem)
	print j, k
