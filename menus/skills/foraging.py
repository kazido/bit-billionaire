from custom.menu import Menu
from utils import ascii_print

class Tree:
    variants = {
        1: "txts/tree.txt",
    }
    
    def __init__(self, hp):
        self.max_hp: int = hp
        self.hp = hp
        self.art = self._get_art()
        
    def _get_art(self):
        return ascii_print.get_lines(self.variants[1])


class Foraging(Menu):

    def run(self):
        term = self.term
        # Clear the screen once at the start
        print(term.home + term.normal + term.clear)
        
        tree = Tree(25)
        user = term.user

        while True:
            # Clear the tree area before redrawing
            with term.location(0, term.height // 2):
                print(term.clear_eos, end="")

            # Scale the tree art with the tree's HP
            scaled_height = int(len(tree.art) * (tree.hp / tree.max_hp))
            with term.location(0, term.height // 2):
                for line in tree.art[:scaled_height]:
                    print(term.center(line))

            # Display the tree's HP
            with term.location(0, term.height // 4):
                print(term.clear_eol + f"Tree HP: {tree.hp} / {tree.max_hp}")

            # Display the user's bits
            with term.location(0, term.height // 4 + 2):
                print(term.clear_eol + f"Your Bits: {user.get_bits()}")

            # NAVIGATION TIME!
            keypress = term.inkey()

            if keypress == " ":
                tree.hp = max(0, tree.hp - 1)  # Prevent HP from going below 0

                # If the tree is fully chopped down
                if tree.hp == 0:
                    reward = 10  # Reward bits for chopping down the tree
                    user.set_field("bits", user.get_bits() + reward)

                    # Display a message
                    with term.location(0, term.height // 2 + 4):
                        print(term.green + term.center(f"You earned {reward} bits!"))

                    # Reset the tree
                    tree = Tree(25)

            if keypress == "q":
                return term.go_back()
