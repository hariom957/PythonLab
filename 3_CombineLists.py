size = int(input("enter size: "))
courseCode = []
courseName = []

for i in range(0,size):
    code = (input("enter course code: "))
    name = input("enter course name: ")

    courseCode.append(code)
    courseName.append(name)

newList = []
for i in range(0, size):
    element = courseCode[i] + ":" + courseName[i]
    newList.append(element)

for i in range(0, size):
    print(newList[i])
