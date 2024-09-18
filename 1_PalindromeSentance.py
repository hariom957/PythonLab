
s = input("enter sentence: ")
l = len(s)

cnt = 0

words = s.split()

for word in words:
    if word == word[::-1]:
        cnt += 1
    
print(cnt)

