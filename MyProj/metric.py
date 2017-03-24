import re

from fuzzywuzzy import fuzz

from MyProj.makeSet import makeWordSet, preparedSet

# print(fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear"))
# print(fuzz.token_set_ratio(" ".join(makeWordSet("The Star Hill Hotel")), "StarHill"))

# print(get_jaro_distance("Hotel", "haatel"))


re.sub("'", "", "str")
re.sub("[-()!?,\[\](){}]|\s*[\.&!?]?\s+|\.$", " ", "[{(St.Augst bridge), South-West]} . a - a Torreluca! B&B O'Dell! & Cabin& Wastlgasse MM-505?.".lower()).split()

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

print(setDistance(preparedSet("ROC"), preparedSet("roc flamingo 3 торремолинос")))
print(setDistance(preparedSet("The star of hill hotel dfsdf sdfsdfsd sdfsdf"), preparedSet("hill star otel ")))
print(setDistance(preparedSet("Отель Фламинго 3"), preparedSet("roc flamingo 3 торремолинос")))
print(setDistance(preparedSet("Itali starHILL"), preparedSet("The STAR Of Hill Italy 5 star")))

print(realDistance(preparedSet("Itali star HILL"), preparedSet("The STAR Of Hill Italy 5 star")))
print(realDistance(preparedSet("starhill in italy"), preparedSet("The STAR Of Hill Italy 5 star")))
