logo='''
 $$$$$$\                                                           $$$$$$\  $$\           $$\                           
$$  __$$\                                                         $$  __$$\ \__|          $$ |                          
$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$\   $$$$$$\        $$ /  \__|$$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$ |       \____$$\ $$  __$$\ $$  _____| \____$$\ $$  __$$\       $$ |      $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ |       $$$$$$$ |$$$$$$$$ |\$$$$$$\   $$$$$$$ |$$ |  \__|      $$ |      $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$\ $$  __$$ |$$   ____| \____$$\ $$  __$$ |$$ |            $$ |  $$\ $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$$$$$$  |\$$$$$$$ |$$ |            \$$$$$$  |$$ |$$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |      
 \______/  \_______| \_______|\_______/  \_______|\__|             \______/ \__|$$  ____/ \__|  \__| \_______|\__|      
                                                                                $$ |                                    
                                                                                $$ |                                    
                                                                                \__|            

                                                                ----By @HarshDevelops                        
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(logo)
print()
count = 0
while True:
    if(count==0):
        count+=1
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift=shift%26
        def encrypt(plain_text, shift_amount):
            cipher_text=""
            for i in range(0,len(plain_text)):
                if(plain_text[i] in alphabet):
                    new_char_no=ord(plain_text[i])+shift_amount
                    new_char=chr(new_char_no)
                    cipher_text+=new_char
                else:
                    cipher_text+=plain_text[i]

            print("The Encrypted Text Is:",cipher_text)

        def decrypt(cipher_text, shift_amount):
            decipher_text=""
            for i in range(0,len(cipher_text)):
                new_char_no=ord(cipher_text[i])-shift_amount
                new_char=chr(new_char_no)
                decipher_text+=new_char

            print("The Decrypted Text Is:",decipher_text)


        if(direction.lower()=="encode"):
            encrypt(plain_text=text, shift_amount=shift)
        else:
            decrypt(cipher_text=text, shift_amount=shift)
    else:
        con=input("Do You Want To Continue?(Y/N): ")
        if(con.lower()=="y"):
            count=0
        else:
            break