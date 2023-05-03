def valid_pwd():
    while True:
        pwd = input("Create a password: ")
        st = list(pwd)
        if not pwd.isalnum() and len(pwd) < 10:
            print("Your password doesn't meet the requirements, please try again")
            print("Enter at least: ")
            print("- One special character")
            print("- One uppercase and lowercase letter")
            print("- One number")
            print("- The password must be at least 10 characters long")
        else:
            if any(c.isupper() for c in st) and any(c.islower() for c in st) and any(c.isdigit() for c in st):
                print('Your password is OK')
                break
            else:
                print("Your password doesn't meet the requirements, please try again")
            
valid_pwd()