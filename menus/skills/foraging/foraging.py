import time

import random
from custom.menu import Menu
from utils import ascii_print


class Tree:
    variants = {
        1: "menus/skills/foraging/tree.txt",
        2: "menus/skills/foraging/tree2.txt",
    }

    def __init__(self):
        self.max_hp = random.randint(20, 30)  # Randomize tree HP
        self.hp = self.max_hp
        self.reward = random.randint(5, 15)  # Randomize reward bits
        self.art = self._get_art()

    def _get_art(self):
        variant = random.choice(list(self.variants.values()))
        return ascii_print.get_lines(variant)

    def chop(self):
        self.hp = max(0, self.hp - 1)  # Reduce HP but not below 0
        return self.hp == 0  # Return True if the tree is fully chopped down

    def get_scaled_art(self):
        scaled_height = round(len(self.art) * (self.hp / self.max_hp))
        return self.art[min(-1, -scaled_height) :]

    def get_status_bar(self, term):
        bar_length = 30
        filled_length = int(bar_length * (self.hp / self.max_hp))
        bar = (
            term.green
            + "█" * filled_length
            + term.red
            + "█" * (bar_length - filled_length)
            + term.normal
        )
        return f"Tree HP: [{bar}] {self.hp} / {self.max_hp}"


class Foraging(Menu):

    def run(self):
        term = self.term
        print(term.home + term.normal + term.clear)

        tree = Tree()
        user = term.user

        chop_speed = 1
        auto_chop = False

        while True:
            # Display the tree art
            with term.location(0, term.height // 2):
                print(term.center(tree.get_status_bar(term)))
                print(term.move_down(1))
                # Make it look like the tree is being chopped top to bottom
                for _ in range(0, len(tree.art) - len(tree.get_scaled_art())):
                    print(term.clear_eol)
                for line in tree.get_scaled_art():
                    print(term.green + term.center(line))

            # Display the user's bits
            with term.location(0, term.height // 4 + 2):
                print(term.center(f"Your Bits: {user.get_bits()}"))
                if auto_chop:
                    print(term.clear_eol + term.center("AUTOCHOPPING..."))

            # NAVIGATION TIME!
            keypress = term.inkey(chop_speed)
            if keypress == "a" or auto_chop:
                auto_chop = True
                if tree.chop():  # If the tree is fully chopped down
                    user.set_field("bits", user.get_bits() + tree.reward)

                    # Display a message
                    with term.location(0, term.height // 2 - 3):
                        print(term.green + term.center(f"You earned {tree.reward} bits!"))

                    with term.location(0, term.height // 2 + 1):
                        print(term.clear_eos)

                    time.sleep(0.25)

                    # Reset the tree
                    tree = Tree()

            if keypress == "q":
                return term.go_back()
