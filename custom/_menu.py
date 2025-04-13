from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from custom.CTerminal import CTerminal

class Menu:
    def __init__(self, term: 'CTerminal'):
        self.term = term
        self._signal: str

    def run(self):
        pass
