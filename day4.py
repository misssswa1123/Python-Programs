
# print(list[-2])
# print(list[len(list)-2])

# if 'hello' not in list:
#     print('no Present')
# else:
#     print('present')

# if 'ar' in 'harry':
#     print('yes')
# if 'ar' is not 'haar':
#     print('yess')
# str='Swapnali34'
# print(str[0:len(str):2])
#list comprehension
# lst=[i**2 for i in range(1,10) if i%2==0]
# print(lst)

# lis=[]
# for i in range(3):
#     a=input('Enter ele')
#     lis.append(a)
# print(lis)

# #instead above we can do
# li=[int(input('Enter the num=')) for i in range(3)]
# print(li)
# list=[1,2,'hello',12,2333,4,34,65,32,67,886,657,'kska']
# print(list[1:6:2])
# print(list)

"""METHODS OF LIST"""
list=[]
for i in range(11,21):
    list.append(i)
print("Append=",list)

list.sort(reverse=True)
print("Sort=",list)

print("Index=",list.index(12))
print("Count",list.count(15))
list.sort()

# newlist=list #reference created
# print("Newlist=",newlist)
# list[0]=12
# print("After reference'list'=",list)
# print("After reference 'Newlist=",newlist)

#To avoid the reference

newlist=list.copy()
print('Copy=',newlist)

newlist.insert(11,89)
print("Insert=",newlist)

newlist.reverse()
print('Reverse=',newlist)

list.extend(newlist)
print("Extend list==",list)


