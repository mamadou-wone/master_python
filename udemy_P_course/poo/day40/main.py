from sheety_data import SheetyData



sheet_data = SheetyData()

def add_user():
    print("Welcome to Boss's Flight Club.\n"
          "We find the best flight deals and email you.")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    email = input("What is your email?\n")
    confirm_email = input("Type your email again\n")

    if email == confirm_email:
        sheet_data.post_data(first_name, last_name, email)
    else:
        print("Check your email input")


add_user()