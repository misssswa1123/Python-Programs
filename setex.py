# to create the empty set
set1=set()
print(set1)
set2={1,2,3,4,5}
set1.update(set2)
print(set1)
for i in range(set1):
    set1.remove(i)

print("after deletion=",set1) 
# not working
# Set Methods**********

a={1,2,3,4}
b={5,6,3,4}

print("a union b=",a.union(b))
print("b u a=",b.union(a))

print("a i b=",a.intersection(b))
print("b i a=",b.intersection(a))
a.intersection_update(b)
print(a)
print("a d b=",a.difference(b))
print("b d a=",b.difference(a))

print("a sy dif b=",a.symmetric_difference(b))

c={6,7,8,9,1,2,3,4}
d={1,2,3,4}
print("isdisjoint=",a.isdisjoint(b))
print("isdisjoint=",c.isdisjoint(d))
print("issuperset=",c.issuperset(d))
print("issuperset=",d.issuperset(c))

print("Issubset=",d.issubset(c))
print("Issubset=",c.issubset(d))

d.update(c)
print(d)

c.add(5)
print(c)

print(c.pop())
print(c)
print(c.remove(3))
print(c)

print(c.discard(3))
print(c)

c.clear()
print(c)

del c
print(c)

set3={1,2,3}
set3.update([4,5,6])
print("set3=",set3)

a={1,2,3}
b={1,2,3,4}
print(a.issubset(b))

# Find missing numbers from 1 to 100 using sets.

def mis(set1):
    allnum=set(range(1,11))
    missing=allnum-set1
    print("Missing Number=",missing)
set1={1,2,3,5,6,9}
mis(set1)