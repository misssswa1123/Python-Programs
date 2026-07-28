# def func():
#     try:
#         a=int(input("Enter number"))
#         s=[2,32,4]
#         print(s[a])
#         print(12/a)
#         return 0
#     # except ValueError:
#     #     print("Enter the integer value")
#     # except IndexError:
#     #     print("inValid index")
#     except Exception as e:
#         print(e)
#         return 1
#     # except ZeroDivisionError as d:
#     #     print(d)
#     finally:
#         print("Excuted successfully!!")
#     # print("Compulsory print!!")
# x=func()
# print(x)
# custom errors
# age=int(input("ENter the age="))
# if age<18:
#     raise Exception("Invalid age")
# age=input("Enter age=")
# if not type(age) is int:
#     raise TypeError("ENter integer")

name=input("Enter =")
if name!="quit":
    raise NameError("Enter valid name")
else:
    print("No error")