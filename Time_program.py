Time = (input("Enter the time: "))
part= Time.split(" ")
#print(part)
#print(part[0])
#print(part[0].split(":"))
clock = part[0].split(":")
Hour = (int(clock[0]))  # hour
Minutes = (int(clock[1]))  # minute
Period = (part[1] )  # AM/PM

if Minutes > 59 or Minutes < 0 or Hour > 12 or Hour < 1 or Period!= "Am" and Period!= "Pm":
    print("Invalid time")

else:
    if Period == "Am" and 4 <= Hour and Hour < 12:
        print("Good morning sir")

    elif Period == "Pm" and (12 == Hour or Hour < 4):
        print("Good afternoon sir")

    elif 4 <= Hour and Hour < 7 and Period == "Pm":
        print("Good evening sir")

    else:
        print("Good night sir")


