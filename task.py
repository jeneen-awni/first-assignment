#Create a Python login system using nested conditions.
#The program should contain:
#A variable for the correct username
#A variable for the correct password
#A variable for the user role
#The roles can be: admin, moderator,user
correct_name= "Jeneen"
correct_password= "jeneen123"
user_role= "User"
username= input(" enter the username: ")
if username== correct_name:
    password= input(" enter the password: ")
    if password== correct_password:
        if user_role== "Admin":
            print("Welcome Admin")
        elif user_role== "Moderator":
            print("Welcome Moderator")
        elif user_role== "User":
            print("Welcome User")
        else:
            print("Unknown role")
    else:
        print("Wrong password")
else:
    print("User not found")

