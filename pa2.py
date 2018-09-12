def merge(a):
    n = len(a)
    if n == 1 :
        return a, 0
    else :
        al = a[:int(n/2)]
        ar = a[int(n/2):]
        x, cx = merge(al)
        y, cy = merge(ar)
        i = 0
        j = 0
        c = 0 + cx + cy
        temp = []
        while i < len(x) and j < len(y) :
            if x[i] <= y[j] :
                temp.append(x[i])
                i += 1
            else:
                temp.append(y[j])
                j += 1
                c += (len(al)-i)
        temp.extend(x[i:])
        temp.extend(y[j:])
        return temp, c



n = []
f = open("input.in", "r")
if f.mode == "r" :
    f1 = f.readlines()
for i in f1 :
    n.append(int(i.strip()))

print(merge(n))
print(len(n))
#print(n)
fo = open("output.out", "w")
fo.write(str(n))
