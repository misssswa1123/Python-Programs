tup=(11,34,54,76,34,23,35,23,566,4677,765,434)
print(tup)
print(tup[-1])
print(tup[1:5])

print(tup.count(34))
print(tup.index(34,1,4))

t1=((12,23)*2)
print(t1)

t2=tup+t1
print(t2)

list=list(tup)
list.append([12,22]*3)
print(list)
