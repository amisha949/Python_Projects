print("A simple calculator with basic arithmetic operations") 
while True:
    a=int(input("Enter first number="))
    b=int(input("Enter second number="))
    choice=input("Enter 1 to add; 2 to subtract; 3 to multiply; 4 for division=")
    if(choice=="1"):
        print("Addition=",(a+b))
    elif(choice=="2"):
        print("Subtraction=",(a-b))
    elif(choice=="3"):
        print("Multiplication=",(a*b))
    elif(choice=="4"):
        print("Division=",(a/b))
    else:
        print("wrong input")
    next=input("do you want to do another calculation yes or no=")
    if(next!="yes" and next!="no"):
       print("wrong input")
       break;
    elif(next=="no"):
       break;
print("All calculations done")
       
        

