import collections
import random
import os

path = os.getcwd()
txt_file = "phrases.txt"
py_file = "phrases.txt"

Phrase = collections.namedtuple("Phrase", "en es")

def shuffle_phrases():
    with open(os.path.join(path, txt_file), 'r') as lines:
        phrases = [Phrase(*line[:-1].split("\t")) for line in lines if line]
    random.shuffle(phrases)
    return phrases

def write_phrases():
    raise NotImplemented
    with open(os.path.join(path, py_file), 'w') as lines:
        pass

def main():
    phrases = shuffle_phrases()
    for phrase in phrases:
        input(phrase.en)
        input(phrase.es)
        print()

main()
