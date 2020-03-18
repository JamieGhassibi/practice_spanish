import collections
import random
import os

path = os.getcwd()

def main():
    """Extract two lists, phrases and words, then shuffle."""
    """Iterate through the English then Spanish of each list."""
    """The user can break the loop by entering a nonempty string."""
    phrases = random.shuffle(read_txt("phrases.txt"))
    words = random.shuffle(read_txt("words.txt"))
    for items in (phrases, words):
        for item in items:
            os.system('cls')
            print("ENTER for next.")
            print("Any key then ENTER to practice vocab or exit.")
            print()
            if input(item.en): break
            if input(item.es): break

def read_txt(filename):
    """Read from specified text file into a list."""
    Translation = collections.namedtuple("Translation", "en es")
    with open(os.path.join(path, filename), 'r') as lines:
        return [Translation(*line[:-1].split("\t")) for line in lines if line]

def write_list():
    """Write list to a python file to save the state of the program."""
    raise NotImplemented
    with open(os.path.join(path, py_file), 'w') as lines:
        pass

main()
