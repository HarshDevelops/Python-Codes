year = int(input("Enter the year: "))
flag=False
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            flag = True
        else:
            flag = False
    else:
        flag = True
else:
    flag = False

if(flag==True):
    print("The Year Is Leap Year")
else:
    print("The Year Is Not A Leap Year")