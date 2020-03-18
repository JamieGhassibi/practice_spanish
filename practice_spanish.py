import collections
import random
import os

filepath = os.getcwd()

def main():
    """Extract two lists, phrases and words, then shuffle."""
    """Iterate through the English then Spanish of each item."""
    """The user can break the loop by entering a nonempty string."""
    filenames = "phrases.txt", "words.txt"
    phrases, words = (read_txt(filename) for filename in filenames)
    for list_ in (phrases, words): random.shuffle(list_)
    for items in (phrases, words):
        for item in items:
            display_header(item)
            if input(item.en): break
            if input(item.es): break

def read_txt(filename):
    """Read from specified text file into a list."""
    Translation = collections.namedtuple('Translation', 'en es type')
    with open(os.path.join(filepath, 'data', filename), 'r') as lines:
        type_ = filename[:-4]
        return [
            Translation(*en_es, type_) for line in lines
            if (en_es := line[:-1].split('\t')) # Assign name to cleaned line.
        ]

def write_list():
    """Write list to a python file to save the state of the program."""
    raise NotImplemented
    with open(os.path.join(filepath, py_file), 'w') as lines:
        pass

def display_header(item):
    os.system('cls')
    print(item.type)
    print()
    print("ENTER for next.")
    print("Any key then ENTER to practice vocab or exit.")
    print()

main()
