import csv
import json
from os.path import isfile, join

path_to_files = "data"
input_name = "query.yaHotelId.showInTop.sure.final.tsv"
output_name = "testQueries.json"

input_file_path = join(path_to_files, input_name)
output_file_path = join(path_to_files, output_name)

SURE = 0

# if not isfile(input_file_path):
queriesById = {}
if not isfile(output_file_path):
    with open(input_file_path) as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')
        for row in reader:
            if row['sure'] == 'True' and row['showIntop'] == 'True':
                SURE += 1
                queriesById[row['yaHotelId']] = (row['sure'], row['query'])

        with open(output_file_path, 'w+') as outfile:
            json.dump(queriesById, outfile, indent=4)
else:
    with open(output_file_path) as infile:
        queriesById = json.load(infile)

if __name__ == "__main__":
    print(len(queriesById))
    print(list(queriesById.items())[:5])
    print(SURE)

def getQueriesDict():
    return queriesById
