from statistics import mode

size = int(input("enter size: "))
numbers = []

for i in range(0,size):
    element = int(input("enter element: "))
    numbers.append(element)

# mean
num = 0
for i in range(0,size):
    num += numbers[i]

print("mean is: ", num/size)

# median

numbers.sort()

if size % 2 == 0:
    print("medians are: ", numbers[int(size/2)], numbers[int(size/2) + 1])
else :
    print("median is: ", numbers[int((size/2))])


# mode
print("mode is: ", mode(numbers)) 
    
