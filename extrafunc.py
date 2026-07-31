# a=[12,34,54]
# b=[12,34,54]
# c=a
# print(id(a))
# print(id(b))
# print(id(c))
# if a is b:
#     print("yes")
# elif a is c:
#     print("yes in a and c ")
# else:
#     print("no")
# if a==b:
#     print('yes')
# else:
#     print('no')


# double=lambda x:x*2
# print(double(4))

# cube=lambda x:x*x*x
# print(cube(9))

# sum=lambda a,y,z:a+y+z
# print(sum(2,3,4))

# def demo(f,x):
#     return x+f(x)
# print("function demo:",demo(double,2))
# print("function demo:",demo(lambda x:x*2,1))


# Map function
# def square(x):
#     return x*x*x

# oldlist=[1,2,3,4,5,6]
# newlist=list(map(square,oldlist))
# print(newlist)

# def filter_function(x):
#     return x>1

# newlist1=list(filter(filter_function,oldlist))
# print(newlist1)
# newlist1=list(filter(filter_function,newlist))
# print(newlist1)

# newlist2=list(filter(lambda a:a>3,oldlist))
# print(newlist2)

from functools import reduce
oldlist=[1,2,3,5]
def func(x,y):
    return x*y
newval=reduce(func,oldlist)
# newval=reduce(lambda x,y:x+y,oldlist)
print(newval)



