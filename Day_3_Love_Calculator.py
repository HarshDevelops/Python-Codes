from re import U
from tkinter import E


n1=input('Enter your name: ').lower()
n2=input("Enter the other person's name: ").lower()
t=n1.count("t")+n2.count("t")
r=n1.count("r")+n2.count("r")
u=n1.count("u")+n2.count("u")
e=n1.count("e")+n2.count("e")
sum_true=t+r+u+e

l=n1.count("l")+n2.count("l")
o=n1.count("o")+n2.count("o")
v=n1.count("v")+n2.count("v")
e=n1.count("e")+n2.count("e")
sum_love=l+o+v+e

print(f"Your Love Percentage Is: {sum_true}{sum_love}%")