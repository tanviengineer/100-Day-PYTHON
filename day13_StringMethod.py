# strings are immutable : we can not change string we can create a new sting using a string methods 
a="tanvi  .......jamnyal  .......tanvi  ....."
# length
print(len(a))
# upper case
print(a.upper())
# lower case
print(a.lower())
# rstrip() : Removes any trailing characters 
print(a.rstrip("."))
# replace()
print(a.replace("tanvi","tanu"))
# split() : It and divides a data and create a list 
print(a.split(" "))
# capitalize() :this method turns only the first character of the string to uppercase 
print(a.capitalize())
#  center() : move the data in center
print(a.center(50))
print(len(a))
print(len(a.center(50)))
#  count() : how to many time a given valve occurs in the string 
print(a.count("tanvi"))
# endswith() : this method checks if the string ends with a given value . if yes given True else retuen False
#              we can checks for a value in between the string by providing start and end index position 
print(a.endswith(".."))
print(a.endswith("yal"))
print(a.endswith("jamnayal",0,30))
# startswith()
print(a.startswith("a"))
print(a.startswith("t"))
#  find() : method serach foo the first occurrences of the given value and given value and return index where it is present .
#            if value is absent then return the -1
print(a.find("tanvi"))
print(a.find("tanu"))
# index() : it hepls to search the value and give index. if value is absent the give error 
print(a.index("tanvi"))
# print(a.index("tanu"))
# isalnum() : it gives True only if the entire string only consists of A-Z , a-z , 0-9 . otherwise it returns false 
b= "My name is Tanvi  I am from Shimla I am 20 yeras old"
tanu = "MyNameIsTanvi"
print(b.isalnum())
print(tanu.isalnum())
#  isalpha : only consist A-Z ,a-z otherwise gives an error
print(tanu.isalpha())
print(b.isalpha ())
# islower() : is all the values in a lower case
print(a.islower())
#  isupper()
print(a.isupper())
# isprintable(): ir gives True if all the values within the string are printable , if not it gives false
print(a.isprintable())
#  isspsce(): it gives a True if string consists of white space , else returns false
print(a.isspace())
#  istitle() : give true when first letter of  
print(a.istitle())
print(b.istitle())
# swapcase()
print(a.swapcase())
print(b.swapcase())
# title()
print(a.title())
