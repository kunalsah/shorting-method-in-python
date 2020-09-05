aList=[12,354,3,3641,3,136,54,2]
print("original list is:",aList)
for i in range (1,len(aList)):
	key=aList[i]
	j=i-1
	while  j>=0 and key <aList[j]:
		aList[j+1] = aList[j]   #shift elements to right to make room for key
		j=j-1
	else:
		aList[j+1]=key
print("list after sorting:",aList)
		