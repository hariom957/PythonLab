def my_max(*cont):
    maxi = cont[0]
    for value in cont[1:]:
        if value > maxi:
            maxi = value
    return maxi

def main():
    l = [1,2,3,4,5]
    print(my_max(*l))

    tup = (1,5,3,7,9,3)
    print(my_max(*tup))

    set = {1,6,3,0,10,7,3}
    print(my_max(*set))       

main()     