def BinarySearch(array, x):
	size  = len(array)
	low = 0
	high  = size - 1
	while(low < high):
		mid = (low+high)/2
		if array[mid] == x:
			return mid
		elif x > array[mid]:
			low = mid + 1
		else:
			high = mid - 1	
	return "Not found"		





p = [8,9,4,4,1,3,7,8]
p = sorted(p) 
num2search = raw_input("Please input what no. you want me to search : ")

print p
print BinarySearch(p, num2search)




