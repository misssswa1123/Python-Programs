# a=10
# def hello():
#     a=20
#     print(a)
# hello()
# print(a)
a=10
print("a=",a)
def hello():
    global a
    a=90

print("a=",a)
hello()
print("a=",a)