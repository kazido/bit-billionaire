import random

from utils import ascii_print
from menus._menu import Menu


title_art_path = "txts/title_art.txt"
title_art = ascii_print.aprint(title_art_path)

# Pick a random splash message!
with open("txts/splash_messages.txt", "r") as f:
    splash_message = random.choice(f.readlines())


class MainMenu(Menu):
    """Displays the home menu of the game."""

    def run(self):
        term = self.term

        # Move to the center of the screen for the title
        print(term.home + term.clear + term.move_y(term.height // 3))

        # Print out our title from the ascii art in a nice red color. Make it blink too.
        print(term.indianred1)
        for line in title_art:
            print(term.blink + term.center(line))

        # Print our splash message beneath the title
        for _ in range(2):
            print()
        print(term.normal + term.yellow + term.center(splash_message))
        for _ in range(2):
            print()

        # After some space, print out our main menu.
        print(term.rosybrown1, end="")
        print(term.center("[1]" + "Start Game".rjust(20)))
        print(term.center("[2]" + "Instructions".rjust(20)))
        print(term.rosybrown3, end="")
        print(term.center("[q]" + "Quit Game".rjust(20)))

    def process_navigation(self) -> str:
        inp = self.term.inkey()

        if inp == "1":
            # If user isn't logged in, prompt them to.

            return "GAME"

        elif inp == "2":
            return "INSTRUCTIONS"

        else:
            return super().process_navigation(keystroke=inp)
