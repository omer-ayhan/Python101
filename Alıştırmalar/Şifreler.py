def check_login(users, username, password):
    # '.items()' method lets us loop with two variables
    for key, val in users.items():
        # if both variables match with the parameters return "True" and end the function
        if key == username and val==password:
            return True
    return False
            
users={"a":"b", "c":"d", "e":"f","t":"y"}
try: 
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print(check_login(users, username, password))
except:
    print("Please enter credentials correctly")
    quit()

