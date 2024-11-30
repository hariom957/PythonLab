def my_zip(l1, l2, l3, strct) :
    zipped = []
    if strct :
        if(len(l1) == len(l2) == len(l3)):
            for i in range(min(len(l1),len(l2),len(l3))):
                tup = (l1[i], l2[i], l3[i])
                zipped.append(tup)
            return zipped
        else:
            return zipped
    else:
        for i in range(min(len(l1),len(l2),len(l3))):
            tup = (l1[i], l2[i], l3[i])
            zipped.append(tup)
        return zipped    

def my_sort(zipped, key):
    n = len(zipped)
    for i in range(0,n):
        for j in range(i, n-1):
            if zipped[j][key] > zipped[j+1][key]:
                zipped[j], zipped[j+1] = zipped[j+1], zipped[j]
    return zipped 

def main():
    l1 = ["a", "b", "c"]
    l2 = ["12", "14", "13"]
    l3 = ["500", "200", "300",]
    zipped = my_zip(l1,l2,l3, False)
    print(my_sort(zipped, 2))

main()