#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
INVITED_PERSON = "[name]"
with open("./Input/Names/invited_names.txt") as my_guest:
    name = my_guest.readlines()


with open("./Input/Letters/starting_letter.txt") as letters:
    letter_content = letters.read()
    for guest in name:
        stripped_name = guest.strip()
        new_letter = letter_content.replace(INVITED_PERSON, stripped_name)
        with open(f"./Output/ReadyToSend/{stripped_name}.txt", "w") as ready_file:
            ready_file.write(new_letter)
