# l=[2,4,3,5,3,2,1,3]
# for index,value in enumerate(l,start=1):
#     print(index,":",value)
#     if index==3:
#         print("index is 3")

# Short hand if else
a=56
b=5
print(a) if a>b else print("=") if a==b else print(b)
c=True if a>b else False
print(c)
import pandas as pd
print(pd.__version__)