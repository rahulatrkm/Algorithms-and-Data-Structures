# Python3 program to count
# inversions in an array

def getInvCount(arr, n):

	inv_count = 0
	for i in range(n):
		for j in range(i+1, n):
			if (arr[i] > arr[j]):
				inv_count += 1

	return inv_count

# Driver Code
f = open("input.in", "r")
if f.mode == "r" :
	f1 = f.readlines()
arr = []
for i in f1 :
	arr.append(int(i.strip()))
n = len(arr)
print("Number of inversions are",getInvCount(arr, n))

# This code is contributed by Smitha Dinesh Semwal
