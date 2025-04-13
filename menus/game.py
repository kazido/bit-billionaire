from custom._menu import Menu





class Game(Menu):
    """Displays the game menu with options to access everything."""

    def run(self):
        # TODO: Display the main game menu!
        # TODO: If the user hasn't played before, get them started with a tutorial!

        

        return super().run()

    
    def process_navigation(self) -> str:
        inp = self.term.inkey()

        if inp == "1":
            return "PROFILE"
        if inp == "2":
            return "EXPLORE"
        else:
            return super().process_navigation(keystroke=inp)
