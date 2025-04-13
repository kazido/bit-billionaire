from custom.CTerminal import CTerminal


def main():
    # blessed Terminal instance
    term = CTerminal()

    # Hide the cursor and allow input to be instantly read
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():

        while True:
            term.current_menu.run()

            term.update()


if __name__ == "__main__":
    main()
