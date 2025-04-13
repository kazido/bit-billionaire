from blessed import Terminal


class Menu:
    def __init__(self, term: Terminal):
        self.term = term

    def display(self):
        """Meant to be overwritten with terminal output."""
        # After some space, print out our main menu.
        print(self.term.move_y(self.term.height-5), end='')
        print(self.term.center(self.term.rosybrown3("[q] Go Back")))

    def process_navigation(self, keystroke=None) -> str:
        """Takes input if subclass menu needs to handle input. If not, wait for q."""
        if not keystroke:
            keystroke = self.term.inkey()
        if keystroke == 'q':
            return "BACK"
