class Calculator:
    def add(self,num1,num2):
        print("Addition is :",num1+num2)
    def sub(self,num1,num2):
        print("Subtraction is :",num1-num2)
    def mul(self,num1,num2):
        print("Multiplication is :",num1*num2)
    def div(self,num1,num2):
        print("Division is :",num1/num2)
        
cl= Calculator()

while True:
    print("Hii i am calculator")
    print("1.Addition ")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    ch = int(input("Enter Your choice :"))
    if ch==5:
        break
        print("Hope you got the ")
    num1= int(input("Enter Number 1: "))
    num2= int(input("Enter Number 2: "))
    
    if ch==1:
        cl.add(num1,num2)
    elif ch==2:
        cl.sub(num1,num2)
    elif ch==3:
        cl.mul(num1,num2)
    elif ch==4:
        cl.div(num1,num2)
    elif ch==5:
        break
    else:
        print("Invalid Number")
