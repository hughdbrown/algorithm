Function Rank(Of T)(Byref x() as T) as Integer()
	Dim original_pos = x.Select(Function(xx, index) New With {.Val = xx, .Index = index}).ToLookup(Function(xxx) xxx.Val)
	Dim result(x.Count-1) as Integer
	Dim i as Integer = 1
	For Each item in original_pos.OrderByDescending(Function(yy) yy.Key)
		For Each v in item
			result(v.Index) = i
		Next
		i = i + item.Count
	Next
	Return result
End Function
