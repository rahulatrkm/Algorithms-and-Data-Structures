count = 0
def QuickSort(n) :
    global count
    count += len(n) - 1
    if len(n) <= 1:
        return n
    else :
        # swapping last & first element
        temporay = n[0]
        n[0] = n[len(n) - 1]
        n[len(n) - 1] = temporay
        pivot = n[0]
        i = 1
        for j in range(1,len(n)) :
            if n[j] < pivot :
                t1 = n[j]
                n[j] = n[i]
                n[i] = t1
                i += 1
        # swap pivot and n[i]
        i = i - 1
        n[0] = n[i]
        n[i] = pivot
        templ = n[:i]
        tempr = n[i+1:]
        temp = []
        temp.extend(QuickSort(templ))
        #count += len(templ) - 1
        temp.append(pivot)
        temp.extend(QuickSort(tempr))
        #count += len(tempr) - 1
        return temp

n = []
f = open("QuickSort.in", 'r');
if f.mode == "r" :
    f1 = f.readlines()
for i in f1 :
    n.append(int(i.strip()))
t = QuickSort(n)
#print(t)
print(count)
fo = open("output3_1.out", "w")
fo.write(str(t))
