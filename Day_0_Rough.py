ranges={
    "Test1":[20,30],
    "Test2":[35.5,40],
    "Test3":[12,15],
    "Test4":[120,150],
    "Test5":[80,120],
    }

t_name=input("Enter Test Name: ")
t_value=int(input("Enter Test Value: "))

if(t_value>(ranges[t_name][1]) or t_value<(ranges[t_name][0])):
    print("Abnormal")
else:
    print("Normal")

    