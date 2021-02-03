def_username = "kobe" # default username
def_password = "24" # default password

while(True):
    username = input("Username:")
    password = input("Password:")
    if (def_username == username and def_password == password):
        print("Welcome,",username)
        break
    elif (def_username != username and def_password == password):
        print("Your username is wrong,",username)
    elif (def_username == username and def_password != password):
        print("Password is wrong.")
        answer = input("Do you want to change your password? (Y/N)")
        if (answer == "Y"):
            while (True):
                new_password = input("Enter your new password:")
                if new_password == def_password:
                    print("New password cannot be the same with old password.")

                elif new_password != def_password:
                    def_password = new_password
                    print("Your password is changed.")
                    print(new_password)
                    break
        elif (answer == "N"):
            print('Please enter your password again.')

    elif (def_username != username and def_password != password):
        print('Password and username are wrong.')


