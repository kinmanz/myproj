import re
from unidecode import unidecode
from fuzzywuzzy import fuzz

def toLatin(str):
    return unidecode(str)

def separateString(str, clear=True):
    if clear:
        # str = re.sub("[\.]", " ", str)
        # str = re.sub("[$+&'-]", "", str)
        str = re.sub("[$+&'-\.]", "", str)
    REGEX = r"\b\S+\b"
    finder = re.compile(REGEX)

    matches = re.findall(finder, str)
    return matches

def makeWordSet(hotelName, onSpell=True, doubled=True, triple=False):
    wordList = (separateString(hotelName.lower()))
    if onSpell:
        wordList = [word for word in wordList if len(word) > 3]
    doubledWords = set()
    if doubled:
        for word1 in wordList:
            for word2 in wordList:
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
    return makeWordSet(toLatin(hotelNameOrQuery), onSpell=False, doubled=True)


def setDistance(wordsSet, queryWords):
    # throw away words like hotel
    # delete words with length 1
    total_dist = 0
    for queryWord in queryWords:
        # total_dist += max([get_jaro_distance(word, queryWord) for word in wordsSet])
        total_dist += max([fuzz.ratio(word, queryWord) for word in wordsSet])

    return total_dist/len(queryWords)

def realDistance(wordsSet, queryWords):
    return (setDistance(wordsSet, queryWords) + setDistance(queryWords, wordsSet))/2

def takeTheBest(hotels_names, query_string, num = 20):
    query_set = preparedSet(query_string)
    return sorted(hotels_names,
                  key=lambda hotel: (-setDistance(preparedSet(hotel), query_set), abs(len(hotel) - len(query_string)))
                  )[:num]