# OPERATERS :
# airthmetic operters: +,-,*,/,%,^
num1 = float(int(input(" Enter a first number : ")))   
num2 = float(int(input(" Enter a second number : ")))
print("1 : Addition")
print("2 : Substraction ")
print("3 : MUltipliaction")
print("4 : Division")    
print("5 : Modules" )
print("6 : Exponential ")
operater = int(input("Choose an Operater"))
if operater == 1:
    print(num1 + num2)
elif operater==2:
    print(num1- num2)
elif operater==3:
    print(num1* num2)
elif operater ==4:
    print(num1/num2)
elif operater ==5:
    print(num1//num2)
elif operater ==6:
    print(num1**num2)
else:
    print("Invalid operater")