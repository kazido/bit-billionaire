from blessed import Terminal

from menus.login import Login
from menus.main_menu import MainMenu
from menus.instructions import Instructions
from menus.game import Game


master = {
    "LOGIN": Login,
    "MAIN": MainMenu,
    "INSTRUCTIONS": Instructions,
    "GAME": Game,
    "BACK": None,
}


class CTerminal(Terminal):
    def __init__(self):
        super().__init__(None, None, True)
        self.history: list = []
        self.current_menu = Login(self)
        
    def update(self):
        self.current_menu = self.history[-1]

    def move_to(self, menu_key: str):
        self.history.append(master[menu_key](self))

    def go_back(self):
        self.history.pop()

    def quit_game(self):
        print(self.home + self.clear)
        return exit(1)