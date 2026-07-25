# student={
#     "name":"Swapnali",
#     "age":22,
#     "branch":"CSE"}

# for i in student.keys():
#     print(i,":",student[i])

# for i in student.values():
#     print(i)

# for i,j in student.items():
#     print(i,":",student[i])

# freq=dict()
# list=[1,1,2,3,4,2]
# for i in list:
#     if i not in freq.keys():
#         freq[i]=1
#     else:
#         freq[i]+=1    
# print(freq)

# # enumerate

# for i,val in enumerate(freq):
#     print(i,"=",val)

# comprehensions
dic1={x:x*2 for x in range(5)}
print("comprehension:",dic1)
dic2={x:None for x in (4,5,6,7)}
print("comprehension2:",dic2)

l1=[1,2,3]
l2=[100,200,300]
for i,j in zip(l1,l2):
    print("Key {0} and value {1}".format(i,j))
print(dic1)
print(dic1.pop(3))
print(dic1)
print(dic1.popitem())
print(dic1)
print(dic1.popitem())
print(dic1)