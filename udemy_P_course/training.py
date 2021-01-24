#  ___       __   ________  ________   _______      
# |\  \     |\  \|\   __  \|\   ___  \|\  ___ \     
# \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \   __/|    
#  \ \  \  __\ \  \ \  \\\  \ \  \\ \  \ \  \_|/__  
#   \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ \  \_|\ \ 
#    \ \____________\ \_______\ \__\\ \__\ \_______\
#     \|____________|\|_______|\|__| \|__|\|_______|
from art_hagman import  logo2
alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo2)
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text):
    encrypt = ''
    text2 = []
    for i in text:
        text2.append(i)
        
    for i in text2:
        if i in alphabet :
            shift2 = alphabet.index(i) + shift
            if shift2 >= len(alphabet):
                shift3 = len(alphabet) - alphabet.index(i)
                shift2 = shift - shift3     
            i = alphabet[shift2]           
            encrypt += i
        else:
            i = i   
            encrypt += i     
    print(f"The encode text is {encrypt} ")        
# encrypt(text)    


def decrypt(text):
    decrypt = ''
    encrypt = []

    for i in text:
        encrypt.append(i)
    # print(encrypt)    
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position - shift
            shift2 = new_position
            if new_position < 0:
                shift2 = len(alphabet) + new_position
            i = alphabet[shift2]
            decrypt += i   
        else:
            i = i   
            encrypt += i 
    print(f"The decrypt message is {decrypt}")    
          
          
         
decrypt(text)  
