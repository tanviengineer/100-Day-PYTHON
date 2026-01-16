# match case statement 
# "_" is a defult 

age = int(input("Enter the age of person : "))
match age:
    case 0 : 
        print("tanvi age is ",age)
    case 1:
        print("tanvi age is ",age)
    case 2:
        print("tanvi age is ",age)
    case 3 if age!=3:
        print ("hy")
    case _ :
        print("tanvi is not born ")
    

