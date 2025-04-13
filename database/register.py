import time

from database.mongo import collection, User


def register():
    username = input("Please enter a username: ")
    while collection.find_one({"username": username}):
        print("This username is already taken!")
        username = input("Please enter a username: ")
    
    print("Note: Passwords must be at least 3 characters long.")
    password = input("Please enter a password: ")
    if len(password) < 3:
        print("That's too short...")
        password = input("Please enter a password: ")
        
    if User.new_user(username, password):
        print("Account successfully created!")
        time.sleep(1)
        print("Launching Bit Billionaire...")
        time.sleep(1)
    else:
        print("Something went wrong...")
        exit(1)
        