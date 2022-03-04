import random

print("Welcome to the PyPassword Generator!")
print("How many letters would you like in your password? ")
l=int(input())
print("How many symbols would you like? ")
s=int(input())
print("How many numbers would you like? ")
n=int(input())

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter_string=""

for i in range(0,l):
    letter_string=letter_string+letters[random.randint(0,len(letters)-1)]
    

for i in range(0,n):
    letter_string=letter_string+numbers[random.randint(0,len(numbers)-1)]
    
for i in range(0,s):
    letter_string=letter_string+symbols[random.randint(0,len(symbols)-1)]



ls_list = list(letter_string)
random.shuffle(ls_list)
print("Your Generated Password is: "+''.join(ls_list))
