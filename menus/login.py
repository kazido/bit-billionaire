from menus._menu import Menu
from getpass import getpass

class Login(Menu):
    
    def run(self):
        term = self.term
        
        print(term.move_y(term.height//2))
        username = ""
        password = ""
        
        print(term.move_x(term.width//2 - 10), end="")
        print(term.move_up(1), end="")
        print(term.yellow("LOG IN! LOG IN! LOG IN!"))

        # Display username field
        print(term.move_x(term.width//2 - 10), end="")
        print("Username: ", end="", flush=True)
        
        # Display password field
        print(term.move_x(term.width//2 - 10), end="")
        print(term.move_down(1), end="")
        print("Password: ", end="", flush=True)

        # Show the username as it is being typed
        print(term.move_up(1) + term.move_x(term.width//2), end="")
        while True:
            char = term.inkey()
            if char.name == "KEY_ENTER":
                break
            elif char.name == "KEY_BACKSPACE":
                if len(username) > 0:
                    username = username[:-1]
                    print(term.move_left() + " " + term.move_left(), end="", flush=True)
            else:
                username += char
                print(char, end="", flush=True)
        
        # Show the password as it is being typed
        print(term.move_down(1) + term.move_x(term.width//2), end="")
        while True:
            char = term.inkey()
            if char.name == "KEY_ENTER":
                break
            elif char.name == "KEY_BACKSPACE":
                if len(password) > 0:
                    password = password[:-1]
                    print(term.move_left() + " " + term.move_left(), end="", flush=True)
            else:
                password += char
                print("*", end="", flush=True)

        # Test validity of login information
        