from menus._menu import Menu

instructions = """
Welcome to Bit Billionaire!
This terminal-based game is a Runescape/Skyblock-like skill grinding game!
Level up your profile in various areas like combat, foraging, mining, fishing, and farming!
Compete for your top spot on the skill leaderboards!
And have a good time with your friends in the in-game chat.

-Bry
"""

instructions_art = []
instructions_art_path = "/home/bry/blessedApp/txts/instructions_art.txt"

with open(instructions_art_path, "r") as f:
    for line in f.readlines():
        instructions_art.append(line.strip("\n"))


class Instructions(Menu):
    """
    Prints the instructions for the game.
    Navigation:
        Q > Back
    """

    def display(self):
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

        return super().display()
