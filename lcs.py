

def lcs(x,y):
	m, n = len(x), len(y)
	c = [[0]*(n+1)] * (m+1)

	for i in range(1,m+1):
		for j in range(1,n+1):
			if (x[i-1] == y[j-1]):
				c[i][j] = c[i-1][j-1] + 1
			else:
				c[i][j] = max(c[i][j-1], c[i-1][j])
	print c
	return c[m-1][n-1]

if __name__ == '__main__':
	x = 'ABCBDAB'
	y = 'BDCABA'
	print lcs(x,y)
