Function Rank(Of T)(Byref x() as T) as Integer()
	Dim original_pos = x.Select(Function(xx, index) New With {.Val = xx, .Index = index}).ToLookup(Function(xxx) xxx.Val)
	dim keys = original_pos.OrderByDescending(Function(yy) yy.Key)
	Dim result(x.Count-1) as Integer
	Dim i as Integer = 1
	for each item in keys
		for each v in item
			result(v.Index) = i
		next
		i = i + item.Count
	Next
	return result
End Function
