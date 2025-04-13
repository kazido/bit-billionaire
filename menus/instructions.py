from custom.menu import Menu
from utils import ascii_print

instructions = """
Welcome to Bit Billionaire!
This terminal-based game is a Runescape/Skyblock-like skill grinding game!
Level up your profile in various areas like combat, foraging, mining, fishing, and farming!
Compete for your top spot on the skill leaderboards or just have a good time with your friends in the in-game chat.

-Bry
"""

instructions_art_path = "txts/instructions_art.txt"
instructions_art = ascii_print.aprint(instructions_art_path)

class Instructions(Menu):
    """Prints the instructions for the game."""

    def run(self):
        term = self.term

        # Clear the screen once at the start
        print(term.home + term.normal + term.clear)

        with term.location(0, term.height // 3):
            for line in instructions_art:
                print(term.blink + term.aquamarine + term.center(line))
                
        with term.location(0, term.height // 3 + 5):
            for line in instructions.split('\n'):
                print(term.normal + term.center(line))
            
        # NAVIGATION TIME!
        inp = self.term.inkey()
        
        if inp == 'q':
            self.term.go_back()
