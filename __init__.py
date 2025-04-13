import argparse

from database.register import register

# Parse arguments from the command line
parser = argparse.ArgumentParser(
    prog="Bit-Billionaire",
    description="Play the Bit-Billionaire game!",
    epilog="Developed by bry400"
)

parser.add_argument('--register', action='store_true', help="register an account for the game")
args = parser.parse_args()

# If the register flag was passed, start account creation
if args.register:
    register()
