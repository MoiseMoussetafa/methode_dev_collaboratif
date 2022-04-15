from contextlib import redirect_stdout
import pathlib
import game
import argparse

FILENAME = "map.txt"

with open(FILENAME, 'w') as f:
    with redirect_stdout(f):
        game.init_game(4)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("map", metavar="F", type=str)
    
    args = parser.parse_args()
    
    if not pathlib.Path(args.map).exists():
        print("File not found.")