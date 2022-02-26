print("Welcome to Tip Calculator")
total=float(input("Total Bill: "))
tip=int(input("How much % would you like to give? 10,12,15? "))
people=int(input("Enter Total People: "))
total_after_tip = total*(tip/100) + total
per_person=round(total_after_tip/people,2)
per_person="{:.2f}".format(per_person)
print(f"Each Person Should Pay: {per_person}")
