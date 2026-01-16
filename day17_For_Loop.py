# for loop : for loop can iterate over a sequence of iterable objects in python
#          : when we know how many time over code is excecute . 

# name = "tanvi jamnyal "
# for i in name :
#     print(i)


# fruits = ["Apple ", "Banana", "Graph" , "Mango", "Lichi"]
# for fruit in fruits :
#     print(fruit)
#     for i in fruit:
#         print(i)
# name = str(input("Enter your name :"))
# for i in name :
#     print(i)
# for ii in name:
#     ii= str(input("Enter your name :"))
#     print(ii)


num1= int(input("Enter the first number : "))
num2= int(input("Enter the second number : "))
print( "1 : Additon ")
print("2 : Substraction")
print("3 : Multiplication")
print("4 : Division ")
print("5 : Modulus")

while True:
    option =str(input("Choose an option :"))

# for i  in option:

    if option =="1":
        print(num1 +num2)
    elif option =="2":
        print(num1-num2)
    elif option =="3":
        print(num1*num2)
    elif option == "4":
        print(num1/num2)
    elif option=="5":
        print(num1%num2)
    else:
        print("Invalid choice")
    for ii in option :
        option =str(input("Choose an option :"))
        print(i)

# # range()
for k in range(11):
    print(k)
for i in range(11,22):
    print (i)


# write a program tp print the multiplication table of a number entered by the user (up to 10 ) using the for loop
num = int (input("Enter the value : "))
for i in range(1,11):
    result =num*i
    print(num ,"*",i,"=",result)

#  print even number between 1 to 20 
print("Even number between 1 to 20 ")
for i in range(1,21):
    if i%2==0:
     print(i)

# print reverse of a given number


#  factorial calculater
num = int(input("Enter the number : "))
for a in num :
    fact = num *num-1
    print(fact)
    num =num-1 