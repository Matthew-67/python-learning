x = [1,2 ,"hello", True]
print(x[0])
print(x[2])
print(x)
x[3] = False

print(x[3])
print(x)




x.append("new thing")
print(x)
x.pop()

print(x)

x.pop(0)

x.insert(2, 1)
print(x)
print(x[-1])
print(x[-2])

y = [0,1,2,3,4,5,6,7,8,9]
print(y)
slice = y [:6:3]
print (slice)


length = len(slice)
print(length)

big_list = [x for x in range(1000000)]

slice2 = big_list [999000:]
print(slice2)

newlist = [x *3 for x in range(4)]

print(newlist)

