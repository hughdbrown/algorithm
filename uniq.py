def uniq_sorted(items):
	return [items[0]] + [items[i] for i in range(1, len(items)) if items[i] != items[i-1]]

def uniq(items):
	return uniq_sorted(sorted(items))

if __name__ == '__main__':
	a = [1,2,1,3,1,4,1,5,2,1,3,5,1]
	print uniq(a)
	b = [1,1,1,1,2,2,3,3,4,5,5,5]
	print uniq_sorted(b)
