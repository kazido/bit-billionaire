import argparse
import time

from database.mongo import collection

def register():
        
    parser = argparse.ArgumentParser(
        prog="Bit-Billionaire",
        description="Play the Bit-Billionaire game!",
        epilog="Developed by bry400"
    )

    parser.add_argument('--register', action='store_true', help="register an account for the game")
    args = parser.parse_args()

    if args.register:
        username = input("Please enter a username: ")
        while collection.find_one({"username": username}):
            print("This username is already taken!")
            username = input("Please enter a username: ")
        
        print("Note: Passwords must be at least 3 characters long.")
        password = input("Please enter a password: ")
        if len(password) < 3:
            print("That's too short...")
            password = input("Please enter a password: ")
            
        user = {
            "username": username,
            "password": password,
        }
        
        if collection.insert_one(user):
            print("Account successfully created!")
            time.sleep(1)
            print("Launching Bit Billionaire...")
            time.sleep(1)
        else:
            print("Something went wrong...")
            exit(1)
            