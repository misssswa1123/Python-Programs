# f=open('hello.txt','w')
# f.write("hello I am swapnali")
# # r=f.read()
# # print(r)
# f.close()
# f=open('hello.txt','r')
# # f.write("hello I am swapnali")
# r=f.read()
# print(r)
# f.close()

# f=open('hello.txt','a')

# f.write("\n Hello i amm appending")
# f.close()

# f=open('hello.txt','r')
# r=f.read()
# print(r)
# f.close()

# # To avoid the closing of the File

# with open('hello.txt','a') as f:
#     f.write("\n From the without close")

# with open('hello.txt','r') as f:
#     r1=f.read()
#     print(r1)

# # Readlines

# with open('hello.txt','r') as f:
#     i=0
#     while True:
#         i=i+1
#         lines=f.readline()
#         if not lines:
#             break #helps when file ends
#         # print(lines)
#         d1=lines.split(',')[0]
#         d2=lines.split(',')[1]
#         d3=lines.split(',')[2]
#         print(f"{i}Name=",d1)
#         print("Age=",d2)
#         print("Branch=",d3)
# with open('hello.txt','r') as f:
#     lines=f.readlines()
#     print(lines)

# writelines

# with open('hello.txt','a') as f:
#     line=['hello line1\n','hello line2\n','hello line3\n']
#     f.writelines(line)
# with open('hello.txt','a') as f:      
#     i=0
#     while True:
#         if i>10:
#             break
#         i=i+1
#         a=f"\n Line {i}"
#         f.write(a)

# seek,tell,truncate

with open('hello.txt','r') as f:
    f.seek(10)
    print("tell=",f.tell())
    s=f.read(100)
    print(s)
with open('hello1.txt','w') as f:
    f.write("123456789")
    f.truncate(5)#printed 12345
    




            