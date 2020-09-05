aList = [12,5,64,3,55,324,3,1]
print("original list is:", aList)
n= len(aList)
#Traversing through all list elements
for i in range(n):
	# Last i elements are already in place
	for j in range(0,n-i-1):
		#traverse thhe list from 0 to n-1-i
		#swap if the element found is greater
		#that the next element
		if aList[j]>aList[j+1]:
			aList[j],aList[j+1]=aList[j+1], aList[j]
	print("list after sorting:",aList)