from blessed import Terminal

from menus._menu import Menu
from menus.main_menu import MainMenu
from menus.instructions import Instructions
from menus.game import Game

term = Terminal()

menus = {
    "MAIN": MainMenu(term),
    "INSTRUCTIONS": Instructions(term),
    "GAME": Game(term),
}

history = [menus["MAIN"]]

menu: Menu = history[len(history)-1]

while True:
    # Hide the cursor and allow input to be instantly read
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        
        if not history:
            break
        else:
            menu = history[len(history)-1]
        
        # Run the current menu and set whatever it returns to the new menu
        menu.display()
        
        # Process navigation inputs after we have done everything in the screen
        signal = menu.process_navigation()
        
        # Handle signals at the highest level
        if signal not in menus.keys():
            continue # AKA: Ignore random keypresses
        
        if signal == "BACK":
            history.pop()
        else:
            history.append(menus[signal])
