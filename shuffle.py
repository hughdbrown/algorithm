def shuffle(arr):
	from random import randint
	for length in reversed(range(len(arr))):
		k = randint(0, length)
		arr[k], arr[length] = arr[length], arr[k]
