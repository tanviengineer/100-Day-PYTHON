#  program to print a time using a built in module ie. time 
# import time 
# timestamp = time.strftime("%H : %M : %S ")
# print(timestamp)
# timestamp =time.strftime("%H")
# print(timestamp)
# timestamp = time.strftime("%m")
# print(timestamp)

#  creating a progrma capable of greeting you according to current time 
# import time
# present_time = time.strftime("%h ")
# if present_time <= "12":
#     print("GOOD MORNING MAM")
# elif present_time>="19":
#     print("GOOD AFTERNOON MAM")
# else:
#     print("GOOD NIGHT MAM")
import time
present_time = time.strftime("%h ")
if present_time <= "12":
    print("GOOD MORNING MAM")
elif present_time>="19":
    print("GOOD AFTERNOON MAM")
else:
    print("GOOD NIGHT MAM")


