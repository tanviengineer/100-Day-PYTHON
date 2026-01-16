# TYPE CASTING 
# the conversion of one data type into the other data type is known as type casting in python or type conversion in python .
# Python suppoets a wide veritety of functions or methods like : int() , float() , str() ,ord(), hex(), oct(), tuple(), 
#                                                                set(), list(), dict() etc.
# TYPE OF TYPE CASTING : 1- EXPLICIT Conversion  2- Implicit Conversion
# EXPLICIT CONVERSION : The conversion of one data type into another data type, done via developer or programmer
#                       intervention or manually as per the requirement . It can achieved with the help of pythons built in type conversion functions 
#                        such as : int(), float(), hex(), oct() , str(), etc.

a = ("100")
b= 200
c = int(a)
print(b+c)

a= "1"
b= 2
print(int(a)+ b)

# IMPLICIT CONVERSION : Python converts a smaller data type with two higher data type to prevent the data loss according to the level one data type 
#                       is converted into other by the Python interpreter itself automatically This is called implicit type casting in Python
d = 100
print(type(d))
e = 200.22
print(type(e))
f = d+e
print(f)
print(type(f))