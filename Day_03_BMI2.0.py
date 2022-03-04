weight=float(input("Enter Weight In KGs: "))
height=float(input("Enter Height In meters: "))
BMI = round(weight/(height**2),2)
print("BMI IS: ", round(BMI,2)) 
if(BMI<18.5):
    print("Underweight")
elif(BMI>18.5 and BMI<25):
    print("Normal")
elif(BMI>25 and BMI<30):
    print("Overweight")
elif(BMI>30 and BMI<35):
    print("Obese")
else:
    print("Clinically Ill")