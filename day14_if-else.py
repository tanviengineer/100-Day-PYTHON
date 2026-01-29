#  if else statement 
# IDEs in python ?
age = int(input("Enter your age : "))
if age >=18:
    print("you are eligible")
else :
    print("you are not eligible")
#  if elif else statement
a = int(input("enter a  value : "))
# nested if else statement
a= "\nchecking you are eligible or not for voting \n "
print(a)
ages= int(input("Enter the age of person : "))
if ages >= 18:
    print("you are above 18 , now check your city  ")
    city = str(input("Enter the name of the city : "))
    if city == "Shimla" : 
        print("you are eligible for voting")
    else: 
        print("You are not citizen , so you are not eligible for voting")
else: 
    print("You are under age ,you are not eligible for voting ")
# if elif else statement
b= "\nchecking the day of week of September  using date\n "
print(b)
date = int(input("Enter the date  : ")) 
if date <=31 and date % 7 ==0 :
    print("Today is SATURDAY ")
elif date <=31 and date%7 ==1:
    print("Today is SUNDAY ")
elif date <=31 and  date%7 ==2:
    print("Today is MONDAY ")
elif date <=31 and date%7 ==3:
    print("Today is TUESDAY")
elif date <=31 and  date%7==4:
    print("Today is WEDNESDAY")
elif date <=31 and date%7==5: 
    print("Today is THUESDAY ")
elif date <=31 and date%7 ==6:
    print("Today is FRIDAY")
else :
    print("Given date is invalid ")

