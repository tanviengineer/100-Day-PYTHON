#  while loop : while loop execute statement while the condition is True .
#             : As soon as the condition becomes False ,the interpreter comes out of the while loop
#             : we also use else with while loop 


while True:
    age = int(input("Enter your age : "))
    print(age)

count= int(input("Enter the number : "))
while (count>0 ):
    print(count)
    count = count-1

i= 0
while(i<10):
    print(i)                        
    i = i+1 
print("done")
print ("printing is done")

#  Even Finder : print even numbers between 1 to 20 using while loop 
i=1
while (i<=20):
   if i %2==0:
      print(i)
   i = i+1