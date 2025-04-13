from menus._menu import Menu





class Game(Menu):
    """
    Displays the main game menu, with options to access everything.
    Navigation:
        1 > Profile
        2 > Explore
    """

    def display(self):
        # TODO: Display the main game menu!

        

        return super().display()

    
    def process_navigation(self) -> str:
        inp = self.term.inkey()

        if inp == "1":
            return "PROFILE"
        if inp == "2":
            return "EXPLORE"
        else:
            return super().process_navigation(keystroke=inp)
