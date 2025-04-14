import time
from random import choice, randint

from custom.menu import Menu
from database.mongo import User
from utils import ascii_print


title_art_path = "txts/title_art.txt"
title_art = ascii_print.get_lines(title_art_path)


class MainMenu(Menu):
    """Displays the home menu of the game."""

    def __init__(self, term):
        super().__init__(term=term)
        self.term.user = User("bry400")

    def run(self):
        term = self.term
        tick = 0

        # Clear the screen once at the start
        print(term.home + term.normal + term.clear)

        # Display static content (splash message, user info, menu options) only once
        with term.location(0, term.height // 2 - 2):
            with open("txts/splash_messages.txt", "r") as f:
                splash_message = choice(f.readlines())
            print(term.blink + term.yellow + term.center(splash_message))

        with term.location(0, term.height // 2 + 2):
            print(term.center(f"Currently logged in as: {term.green(str(term.user))}"))

        with term.location(0, term.height // 2 + 4):
            print(term.center("[1]" + "Start Game".rjust(20)))
            print(term.center("[2]" + "Instructions".rjust(20)))
            print(term.center("[q]" + "Quit Game".rjust(20)))

        # Continuously update only the title art
        while True:
            if tick < len(title_art):
                if tick == 0:
                    color1, color2, color3 = randint(50, 255), randint(50, 255), randint(50, 255)
                # At the correct location (1/4th of term height)
                with term.location(0, term.height // 4):
                    print(term.color_rgb(color1, color2, color3), end="")
                    for idx, line in enumerate(title_art):
                        if idx in range(0, tick % len(title_art) + 1):
                            print(term.center(line, width=term.width - 2))
                        else:
                            print(term.gray10, end="")
                            print(term.center(line))

            # Wait for user input
            inp = self.term.inkey(timeout=0.1)

            if inp == "1":
                return self.term.move_to("GAME")

            elif inp == "2":
                return self.term.move_to("INSTRUCTIONS")

            elif inp == "q":
                return self.term.quit_game()

            # Increment the tick for the next title update
            tick += 1

            if tick > 12:
                tick = 0
