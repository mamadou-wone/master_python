#  ___       __   ________  ________   _______      
# |\  \     |\  \|\   __  \|\   ___  \|\  ___ \     
# \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \   __/|    
#  \ \  \  __\ \  \ \  \\\  \ \  \\ \  \ \  \_|/__  
#   \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ \  \_|\ \ 
#    \ \____________\ \_______\ \__\\ \__\ \_______\
#     \|____________|\|_______|\|__| \|__|\|_______|

from art_hagman import calculator

print(calculator)
def add(a , b):
    return a +b


def soustract(a , b):
    return a - b 

def multiply(a , b):
    return a * b

def divide(a , b):
    if b == 0:
        return print("Enter a valid number")
    else:
        return a / b
        

operator = {
    "+": add,
    "-": soustract,
    "*": multiply,
    "/": divide
}  

finish = ''      

# stop = False
num1 = int(input("What is the first number ? "))
for item in operator:
    print(item)
symbol = input("What is the operator ? ")
num2 = int(input("What is the second number ? "))
result = operator[symbol](num1 , num2)
print(result)

while finish != "n":

    finish = input(f"Tape 'y' to continue calculating with {result} , or 'n' to exit ")
    if finish != 'n':
        nextNumber = int(input("What is the next number ? "))
        for item in operator:
            print(item)
        symbol = input("What is the operator ? ")
        result = operator[symbol](result , nextNumber)
    print(result)   

