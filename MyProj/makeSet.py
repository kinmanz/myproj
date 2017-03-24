import re

from MyProj.helpFunctions import separateString, toLatin
from MyProj.readFiles import getHotelsDict

def makeWordSet(hotelName, onSpell=True, doubled=True, triple=False):
    wordList = (separateString(hotelName.lower()))
    if onSpell:
        wordList = [word for word in wordList if len(word) > 3]
    doubledWords = set()
    if doubled:
        for word1 in wordList:
            if not len(word1) > 3: continue
            for word2 in wordList:
                if not len(word2) > 3: continue
                if word1 == word2: continue
                doubledWords.add(word1 + word2)
                doubledWords.add(word2 + word1)
                if triple:
                    for word3 in wordList:
                        if word1 == word3 or word2 == word3: continue
                        doubledWords.add(word1 + word2 + word3)
                        doubledWords.add(word1 + word3 + word2)
                        doubledWords.add(word2 + word1 + word3)
                        doubledWords.add(word2 + word3 + word1)
                        doubledWords.add(word3 + word1 + word2)
                        doubledWords.add(word3 + word2 + word1)


    wordList += doubledWords
    return wordList

def preparedSet(hotelNameOrQuery):
    return makeWordSet(toLatin(hotelNameOrQuery), onSpell=False, doubled = False)

hotels_names_dict = {name: preparedSet(name)for name in getHotelsDict().keys()}

def preparedSetHotel(hotelName):
    return hotels_names_dict[hotelName]

if __name__ == "__main__":
    print(makeWordSet(hotelName="THE Star of Hill Hotel"))
    print(preparedSet("St.THE Star of Hill Hotel"))