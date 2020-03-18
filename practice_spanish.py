import collections
import random
import os

directory = os.getcwd()

def main():
    """Extract two lists, phrases and words. Shuffle."""
    """Iterate through the English then Spanish of each item."""
    """User can break loop by entering nonempty string."""
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
    filepath = os.path.join(directory, 'data', filename)
    with open(filepath, 'r', encoding='utf-8') as lines:
        return [
            Translation(*en_es, filename) for line in lines
            # Assign name to cleaned line.
            # See using walrus expressions in comprehensions.
            if (en_es := line.replace("\n", "").split('\t'))
        ]

def write_list(filename):
    """Write list to a python file to save the state of the program."""
    raise NotImplemented # May be implemented later to allow for SRS-style functionality.
    filepath = os.path.join(directory, 'data', filename)
    with open(filepath, 'w', encoding='utf-8') as lines:
        pass

def display_header(item):
    os.system('cls')
    print("ENTER for next.")
    print("Any key then ENTER to practice vocab or exit.")
    print()
    print(item.type)
    print()

main()
