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

def main():
    l1 = ["a", "b", "c"]
    l2 = ["12", "13", "14"]
    l3 = ["100", "200", "300", "500"]
    print(my_zip(l1,l2,l3, False))

main()