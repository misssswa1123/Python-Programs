# for i in range(0,10,2):
#     print(i)

# for i in range(10):
#     print(i)
#     if i==4:
#         print('get')
#         break
# else:
#     print("Get out")
# i=1
# while i<10:
#     print(i)
#     i+=1
#     if i==3:
#         print('wjw')
#         continue
# to make it work like do while
# x=0
# while True:
#     print(x)
#     x+=1
#     if x>10:
#         break

def avg(*num):
    print(type(num))
    
    for i in num:
       print('Colors:',i)

avg('Red','Yellow','Pink')

def name(**abc):
    print(type(abc))
    print(abc['fname'],abc['lname'])
name(fname='swapnali',lname='Vyawahare')

set=(True,1.0,1,'1')
print(len(set))
