list1 = [1, 3, 5, 16, 8]
list2 = [6, 5, 9, 4, 13, 12]
for i in list2:
    list1.append(i)
print('Joined List=', list1)
s = list(set(list1))
print('Unique Values are:', s)
x = int(input("Enter the value to be searched"))
if x in s:
    print("Found at position", s.index(x))
else:
    for j in s:
        if j >x:
            print("Number is", j, "index is", s.index(j))
            break
    else:
        print("Not Found")
