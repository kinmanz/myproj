from MyProj.readFiles import getHotelsDict
from MyProj.readQueriesFile import getQueriesDict

num = 1011112
name = "адлер камышовая 5"
allHotels = getHotelsDict()
queries = getQueriesDict()

IDsExists = set(val[1] for val in allHotels.values())
IDsQueries = set(id for id, value in queries.items())
print(list(IDsExists)[:10], len(IDsExists))
print(list(IDsQueries)[:10], len(IDsQueries))
print(len(IDsExists & IDsQueries)/len(IDsQueries))



for id, val in queries.items():
    if val[1] == name:
        num = id
        print(val)

if not num in IDsExists: print("Warning!")
for hotel, value in allHotels.items():

    if value[1] == str(num):
        print(value)

"""
Alacat Yal Capk N Otel
Отель Авдалия
Отель Золотой Берег
Гранд отель Уют
Парк Отель Золотая Долина
Эв Рошель Отель
Отель Берег
Отель Park House
Нтон отель
Отель Южный Берег
Отель "Чайковский" (Калининград)
Отель East Time
Отель Деревня Берендеевка
Отель Holiday House Vorontsovo
Casablanca Otel
Отель «Берег»
Отель Черное море Бугаз
Отель Авалон
Отель «Баден-Баден Изумрудный берег»
Отель Лазурный Берег
"""

#
# import re
# from unidecode import unidecode
# from fuzzywuzzy import fuzz
#
# def toLatin(str):
#     return unidecode(str)
#
# def separateString(str, clear=True):
#     if clear:
#         # str = re.sub("[\.]", " ", str)
#         # str = re.sub("[$+&'-]", "", str)
#         str = re.sub("[$+&'-\.]", "", str)
#     REGEX = r"\b\S+\b"
#     finder = re.compile(REGEX)
#
#     matches = re.findall(finder, str)
#     return matches
#
# def makeWordSet(hotelName, onSpell=True, doubled=True, triple=False):
#     wordList = (separateString(hotelName.lower()))
#     if onSpell:
#         wordList = [word for word in wordList if len(word) > 3]
#     doubledWords = set()
#     if doubled:
#         for word1 in wordList:
#             for word2 in wordList:
#                 if word1 == word2: continue
#                 doubledWords.add(word1 + word2)
#                 doubledWords.add(word2 + word1)
#                 if triple:
#                     for word3 in wordList:
#                         if word1 == word3 or word2 == word3: continue
#                         doubledWords.add(word1 + word2 + word3)
#                         doubledWords.add(word1 + word3 + word2)
#                         doubledWords.add(word2 + word1 + word3)
#                         doubledWords.add(word2 + word3 + word1)
#                         doubledWords.add(word3 + word1 + word2)
#                         doubledWords.add(word3 + word2 + word1)
#
#
#     wordList += doubledWords
#     return wordList
#
# def preparedSet(hotelNameOrQuery):
#     return makeWordSet(toLatin(hotelNameOrQuery), onSpell=False, doubled=False)
#
#
# def setDistance(wordsSet, queryWords):
#     # throw away words like hotel
#     # delete words with length 1
#     total_dist = 0
#     for queryWord in queryWords:
#         # total_dist += max([get_jaro_distance(word, queryWord) for word in wordsSet])
#         total_dist += max([fuzz.ratio(word, queryWord) for word in wordsSet])
#
#     return total_dist/len(queryWords)