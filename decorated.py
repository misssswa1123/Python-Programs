def deco(func):
    def newfun(*args,**kwargs):
        print("Hello")
        func(*args,**kwargs)
        print("Swapnali")
    return newfun

@deco
def greet():
    print("From abc to")
@deco
def add(a,b):
    print("Addition=",a+b)
# deco(greet)()
greet()
add(2,4)
