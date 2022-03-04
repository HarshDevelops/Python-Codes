import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print()
print()

bid={}
while True:
    name=input("Enter Your Name: ")
    price=int(input("Enter Your Bid: $"))
    bid[name]=price
    x=input("Are There Any Other Bidders?[Y/N]: ")
    if(x.lower()=="y"):
        os.system("cls")
        continue
    else:
        break

highest_bid=0
highest_bidder_name=""
for i in bid:
    if(bid[i]>highest_bid):
        highest_bid=bid[i]
        highest_bidder_name=i

print("Highest Bidder is: "+highest_bidder_name+" with bid: "+str(highest_bid))