from custom._menu import Menu
from utils import ascii_print

instructions = """
Welcome to Bit Billionaire!
This terminal-based game is a Runescape/Skyblock-like skill grinding game!
Level up your profile in various areas like combat, foraging, mining, fishing, and farming!
Compete for your top spot on the skill leaderboards!
And have a good time with your friends in the in-game chat.

-Bry
"""

instructions_art_path = "txts/instructions_art.txt"
instructions_art = ascii_print.aprint(instructions_art_path)

class Instructions(Menu):
    """Prints the instructions for the game."""

    def run(self):
        term = self.term

        # Move to the center of the screen for the title
        print(term.home + term.clear + term.move_y(term.height // 3))

        # Print out our title from the ascii art in a nice red color. Make it blink too.
        print(term.indianred1)
        for line in instructions_art:
            print(term.blink + term.center(line))

        for _ in range(2):
            print()
            
        for line in instructions.split('\n'):
            print(term.normal + term.yellow + term.center(line))
            
        # NAVIGATION TIME!
        inp = self.term.inkey()
        
        if inp == 'q':
            self.term.go_back()
