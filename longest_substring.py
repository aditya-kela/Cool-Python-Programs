def longest_substring(string, m):
	n = len(string)
	i = 0
	longest_len = 0
	dic ={}
	st = ""
	for i in range(0, n):
		(str1, dicn, s) = sub_string(string, i, n, m)		
		if str1 > longest_len:
			longest_len = str1
			dic = dicn
			st = s

	print longest_len
	print dic
	print st
def sub_string(string, i, n, m):
	mydic = {}
	seq = ""
	while len(mydic) <= m and i < n:
			if string[i] in mydic:
				mydic[string[i]] += 1
				seq = seq + string[i]
				i = i + 1
			else:
				mydic[string[i]] = 1
				seq = seq + string[i]
				if(len(mydic) > m):
					del mydic[string[i]]
					seq = seq.replace(string[i], "")
					i = i + 1
					break
				else:	
					i = i + 1
							
	substring_len = sum(mydic.values())
	return substring_len, mydic, seq			

#longest_substring('abaccc', 2)
longest_substring('abaaaaasssddddddddd', 3)		

