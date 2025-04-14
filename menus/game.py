from custom.menu import Menu


class Game(Menu):
    """Displays the game menu with options to access everything."""

    def run(self):
        term = self.term
        # Clear the screen once at the start
        print(term.home + term.normal + term.clear)
        
        # TODO: Display the main game menu!
        # TODO: If the user hasn't played before, get them started with a tutorial!
        for line in term.user.get_profile():
            print(term.center(line))

        
         # NAVIGATION TIME!
        inp = term.inkey()
        
        if inp == '1':
            term.move_to("FORAGING")
        
        if inp == 'q':
            term.go_back()
