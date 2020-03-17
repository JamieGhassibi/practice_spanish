import collections
import random
import os

path = os.getcwd()

Translation = collections.namedtuple("Translation", "en es")

def read_txt(filename):
    """Read from specified text file."""
    with open(os.path.join(path, filename), 'r') as lines:
        items = [Translation(*line[:-1].split("\t")) for line in lines if line]
    random.shuffle(items)
    return items

def write_list():
    """Write list to python file."""
    raise NotImplemented
    with open(os.path.join(path, py_file), 'w') as lines:
        pass

def main():
    phrases = read_txt("phrases.txt")
    words = read_txt("words.txt")
    for items in (phrases, words):
        for item in items:
            os.system('cls')
            print("ENTER for next.")
            print("Any key then ENTER to practice vocab or exit.")
            print()
            if input(item.en): break
            if input(item.es): break

main()
