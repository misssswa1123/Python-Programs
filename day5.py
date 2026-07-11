# print(type(f"(2*3)"))
# price=89.898988900
# print(f"The price is {price:.2f} only")

# Docstring 
# def square():
#     '''This is docstring gives info about the function'''
#     print("Hello")
# square()
# print(square.__doc__)

# Factorial
# def fact(n):
#     if n==0 or n==1:
#         return 1
    
#     return n*fact(n-1)
    
# print(fact(3))

# for with else
for i in range(6):
    print(i)
else:
    print("Done")

for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("Done")
i=1
while i<6:
    print(i)
    if(i==4):
        break
    i=i+1
else:
    print("Done")