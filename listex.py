questions=[["1.what is the capital of India?\n 1.Mumbai \t 2.Delhi \t 3.Banglore \t 4.Kolkata",2,10000],
           ["2.what is the economy capital of India?\n 1.Mumbai \t 2.Delhi \t 3.Banglore \t 4.Kolkata",1,10000],
           ["3.what is the cultural capital of India?\n 1.Mumbai \t 2.Pune \t 3.Banglore \t 4.Kolkata",2,10000],
           ["4.who of prime minister of India?\n 1.Rahul \t 2.Mamta \t 3.Modi \t 4.Devendra",3,10000],
           ["5.what is the natial anthem of India?\n 1.vande mataram \t 2.Janagana man \t 3.Ye mere vatan \t 4.None of the above",2,10000],]

i=0
cnt=0
while i<len(questions):
    print(questions[i][0])
    ans=int(input("Enter the option="))
    if ans>4:
        print("Enter valid option")
    elif ans==questions[i][1]:
        cnt+=questions[i][2] 
        print("Congrats!!!Your answer is correct")
        i+=1
    else:
        print("OOPs your answer is wrong!!!")
        i=i+len(questions)

if cnt>0:
    print('*************#####***************')
    print("You won",f"${cnt}"," Congratulations!!!!!")
else:
    print('*************#####***************')
    print("Sorry You won Nothing !!Better Luck next time")

    