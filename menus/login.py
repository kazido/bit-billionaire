import time

from custom.menu import Menu
from database.mongo import User


class Login(Menu):

    def run(self):
        term = self.term

        print(term.move_y(term.height // 2))
        username = ""
        password = ""

        print(term.move_x(term.width // 2 - 10), end="")
        print(term.move_up(1), end="")
        print(term.yellow("LOG IN! LOG IN! LOG IN!"))

        # Display username field
        print(term.move_x(term.width // 2 - 10), end="")
        print("Username: ", end="", flush=True)

        # Display password field
        print(term.move_x(term.width // 2 - 10), end="")
        print(term.move_down(1), end="")
        print("Password: ", end="", flush=True)

        # Show the username as it is being typed
        print(term.move_up(1) + term.move_x(term.width // 2), end="")
        while True:
            char = term.inkey()
            if char.name == "KEY_ENTER" or char.name == "KEY_TAB":
                break
            elif char.name == "KEY_BACKSPACE":
                if len(username) > 0:
                    username = username[:-1]
                    print(term.move_left() + " " + term.move_left(), end="", flush=True)
            else:
                username += char
                print(char, end="", flush=True)

        # Show the password as it is being typed
        print(term.move_down(1) + term.move_x(term.width // 2), end="", flush=True)
        while True:
            char = term.inkey()
            if char.name == "KEY_ENTER" or char.name == "KEY_TAB":
                break
            elif char.name == "KEY_BACKSPACE":
                if len(password) > 0:
                    password = password[:-1]
                    print(term.move_left() + " " + term.move_left(), end="", flush=True)
            else:
                password += char
                print("*", end="", flush=True)

        # Test validity of login information
        result = User.login(username, password)
        if result == 1:
            print(term.move_down(3) + term.move_x(term.width // 2 - 15), end="", flush=True)
            print(term.red("Invalid login, please try again."), end="", flush=True)
            time.sleep(1)
            print(term.home + term.clear)
            return self.run()
        
        elif result == 2:
            print(term.move_down(3) + term.move_x(term.width // 2 - 15), end="", flush=True)
            print(term.red("You are already logged in elsewhere!"), end="", flush=True)
            time.sleep(1)
            print(term.home + term.clear)
            return self.run()

        # We have successfully logged in, set our signal and exit this function
        self.term.user = result
        print(term.move_down(2) + term.move_x(term.width // 2 - 13), end="")
        print(term.green("Successfully logged in!"))
        time.sleep(1)
        self.term.move_to("MAIN")
