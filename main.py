from blessed import Terminal

from menus._menu import Menu
from menus.login import Login
from menus.main_menu import MainMenu
from menus.instructions import Instructions
from menus.game import Game

from database.register import register

register()
                
# blessed Terminal instance
term = Terminal()

# Master list of valid menus that we can navigate to.
# TODO: These may not work as initialized off rip. May need to be non-init and called when navigated to.
master = {
    "LOGIN": Login(term),
    "MAIN": MainMenu(term),
    "INSTRUCTIONS": Instructions(term),
    "GAME": Game(term),
    "BACK": None,
}

# List of menu history used for navigation
history = [master["LOGIN"]]

while True:
    # Hide the cursor and allow input to be instantly read
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():

        try:
            menu: Menu = history[len(history) - 1]
        except IndexError:
            break  # We hit Q on main menu

        # Run the current menu and set whatever it returns to the new menu
        menu.run()

        # Process navigation inputs after we have done everything in the screen
        signal = menu.process_navigation()

        # Handle signals at the highest level
        if signal not in master.keys():
            continue  # AKA: Ignore random keypresses

        if signal == "BACK":
            # Signaled to go back, remove current menu from history.
            history.pop()

        else:
            # Valid navigation, add new menu to the history.
            history.append(master[signal])
