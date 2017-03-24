import pickle

from MyProj.helpFunctions import toLatin
from MyProj.makeSet import makeWordSet
from MyProj.readFiles import getHotelsDict
from pyspell.pyspell import Dictionary


import json
from os import listdir
from os.path import isfile, join

file_path = join("data", "spell_dict.p")

if not isfile(file_path):
    spell_dict = Dictionary()
    allHotels = getHotelsDict()
    i = 0
    for hotel in allHotels:
        i += 1
        if i % 1000 == 0:
            print(i)
        spell_dict.add_words(makeWordSet(toLatin(hotel), onSpell=True, doubled=False))
    spell_dict.add_words(["stars", "star"])
    with open(file_path, 'wb') as outfile:
        pickle.dump(spell_dict, outfile)
else:
    with open(file_path, "rb") as infile:
        spell_dict = pickle.load(infile)


def get_spell_dict():
    return spell_dict


if __name__ == "__main__":
    print("here")
    spell_dict = get_spell_dict()
    print(spell_dict.lookup("hamerous", return_distances = True))
