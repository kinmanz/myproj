import pickle
from multiprocessing.pool import Pool

import time

from MyProj.makeSet import preparedSet, preparedSetHotel
from MyProj.metric import setDistance, realDistance
from MyProj.readFiles import getHotelsDict
from MyProj.readQueriesFile import getQueriesDict
from MyProj.spell_corrector import correction
from datasketch import MinHashLSHForest, MinHash
from os.path import isfile, join

NN_PERM = 128
# NN_PERM = 50

def makeMinHash(hotelName):
    newMinHash = MinHash(num_perm=NN_PERM)
    for word in preparedSet(hotelName.lower()):
        newMinHash.update(word.encode('utf8'))
    return (hotelName, newMinHash)

def growForest(forest, minHahs):
    for hotel, hash in minHahs:
        forest.add(hotel, hash)

allHotels = getHotelsDict()

file_path = join("data", "lshforrest.p")


# Создаю minHahs для всех слов
if not isfile(file_path):
    # Create a MinHash LSH Forest with the same num_perm parameter
    forest = MinHashLSHForest(num_perm=NN_PERM)
    allKeys = list(allHotels.keys())
    print(len(allKeys))
    with Pool(4) as pool:
        minHahs = pool.map(makeMinHash, allKeys[0:100000])
        print("Done 1!"); growForest(forest, minHahs)
        minHahs = pool.map(makeMinHash, allKeys[100000:200000])
        print("Done 2!"); growForest(forest, minHahs)
        minHahs = pool.map(makeMinHash, allKeys[200000:300000])
        print("Done 3!"); growForest(forest, minHahs)
        minHahs = pool.map(makeMinHash, allKeys[300000:400000])
        print("Done 4!"); growForest(forest, minHahs)
        minHahs = pool.map(makeMinHash, allKeys[400000:500000])
        print("Done 5!"); growForest(forest, minHahs)
        minHahs = pool.map(makeMinHash, allKeys[500000:600000])
        print("Done 6!"); growForest(forest, minHahs)
        minHahs = pool.map(makeMinHash, allKeys[600000:700000])
        print("Done 7!"); growForest(forest, minHahs)
        minHahs = pool.map(makeMinHash, allKeys[700000:800000])
        print("Done 8!"); growForest(forest, minHahs)
        minHahs = pool.map(makeMinHash, allKeys[800000:900000])
        print("Done 9!"); growForest(forest, minHahs)
        minHahs = pool.map(makeMinHash, allKeys[900000:1000000])
        print("Done 10!"); growForest(forest, minHahs)
        minHahs = pool.map(makeMinHash, allKeys[1000000:])
        print("Done 11!"); growForest(forest, minHahs)
    print("Make Forest!")

    forest.index()
    with open(file_path, 'wb') as outfile:
        pickle.dump(forest, outfile)
else:
    with open(file_path, "rb") as infile:
        forest = pickle.load(infile)

# IMPORTANT: must call index() otherwise the keys won't be searchable
# forest.index()

IDsExists = set(val[1] for val in allHotels.values())
IDsQueries = set(id for id in getQueriesDict().keys())
IDs = IDsExists & IDsQueries
print(len(IDs), len(IDsQueries))

# Check for membership using the key
print("Himeros Beach Hotel" in forest)

# searchMinHash = MinHash(num_perm=NN_PERM)

# spell correction
# query_string = "махх роял кемер цена"
# query_set = preparedSet(query_string.lower())
# print(query_set)
# for word in query_set:
#     searchMinHash.update(correction(word).encode('utf8'))

# # Using m1 as the query, retrieve top 1000 keys that have the higest Jaccard
# result = forest.query(searchMinHash, 1000)
# print(result)
# result1 = sorted(result, key=lambda hotel: (-setDistance(preparedSet(hotel), query_set), abs(len(hotel) - len(query_string))))
# result2 = sorted(result, key=lambda hotel: (query_set, -setDistance(query_set, preparedSet(hotel)), abs(len(hotel) - len(query_string))))
# print(*result1[:20], sep='\n')
# print("************************************")
# print(*result2[:20], sep='\n')

# exit()
print("Start test!")

queriesById = getQueriesDict()
total = 0
total_true = 0
total_time = 0
# бежим по всем запросам
for hotelId, value in queriesById.items():
    if value[0] != "True": continue
    if not hotelId in IDs: continue
    total += 1
    print(total, total_true, total_true/total)
    start = time.time()
    query_set = preparedSet(value[1])
    # print(query_set)

    # Создаём поисковый minHash
    searchMinHash = MinHash(num_perm=NN_PERM)
    # print("===========================================================")
    # print("Query =", value[1])

    # Добовляем в него слова после спел корректишина
    for word in query_set:
        searchMinHash.update(correction(word).encode('utf8'))

    # allHotels[row["name"]] = (unidecode(row["name"]), row["id"], row['stars'])
    # Using m1 as the query, retrieve top 20 keys that have the higest Jaccard

    # берём первые 500
    result = forest.query(searchMinHash, 500)
    # сортируем по метрике похожести и сходству длины фразы запроса
    result = sorted(result, key=lambda hotel: (-setDistance(preparedSetHotel(hotel), query_set), abs(len(hotel) - len(query_string))))
    end = time.time()
    # result1 = sorted(result, key=lambda hotel: (-setDistance(query_set, preparedSet(hotel)), abs(len(hotel) - len(query_string))))
    # result2 = sorted(result, key=lambda hotel: (-realDistance(preparedSet(hotel), query_set), abs(len(hotel) - len(query_string))))
    # print("Res 1 ________")
    # print(*result[:5], sep='\n')
    # print("Res 2 ________")
    # print(*result1[:5], sep='\n')
    # print("Res 3 ________")
    # print(*result[:5], sep='\n')
    # print(result)
    timenow = end - start
    total_time += timenow

    # берём 1-ый из отсортированого результата, и проеверяем что совпал
    for res in result[:1]:
        if str(allHotels[res][1]) == hotelId:
            total_true += 1
            # print("Result:", True, " ============= ")
            continue
    print("Time:", timenow)
    print("Time average:", total_time/total)
print(total_true, total)
print(total_true/total)
print(total_time)
print(total_time/total)
