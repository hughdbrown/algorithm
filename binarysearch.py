def binarysearch(iter, val):
	lo, hi = 0, len(iter)-1
	while lo <= hi:
		mid = lo + (hi - lo) / 2
		if iter[mid] >= val :
			hi = mid - 1
		else:
			lo = mid + 1
	return (lo if iter[lo] == val else -1)

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
