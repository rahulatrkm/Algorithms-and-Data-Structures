def partition(a, l, r):
    p = a[l]
    i = l + 1
    j = l + 1
    for j in range(j, r + 1):
        if a[j] < p:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
            i = i + 1

    temp = a[l]
    a[l] = a[i - 1]
    a[i - 1] = temp
    return i - 1

c = 0
def quickSort(a, l, r):
    global c
    if l >= r:
        return

    j = partition(a, l, r)
    quickSort(a, l, j-1)
    c += (j-l-1)
    quickSort(a, j+1, r)
    c += (r-j-1)

numbers = []
f = open("QuickSort.in", 'r');
if f.mode == "r" :
    f1 = f.readlines()
for i in f1 :
    numbers.append(int(i.strip()))
quickSort(numbers,0,3)
c += len(numbers) - 1
print(numbers)
print(c)
