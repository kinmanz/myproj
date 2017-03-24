

import csv
import json
from os import listdir
from os.path import isfile, join
from unidecode import unidecode

# ('partner_ids', 'lt=9022840@@ostrovok=himeros_beach_hotel@@oktogo=253871@@booking=337246@@sunmar=14422')
# ('name', 'Himeros Beach Hotel')
# ('region_id', '21091')
# ('country_id', '983')
# ('review_count', '1')
# ('rooms_search', 'true')
# ('longitude', '30.5636912584')
# ('tours_search', 'true')
# ('langed_name', 'en=Himeros Beach Hotel@@ru=Himeros Beach Hotel')
# ('features', 'hair_dryer=true@@table_tennis=true@@type_rooms=non_smoking_room@@transfer=true@@private_beach=true@@billiards=true@@24_front_desk=true@@pool_type=outdoor_pool@@air_conditioning=true@@tv_set=true@@internet=true@@floors=3@@left_luggage_office=luggage@@type_parking=free_parking@@distance_to_water=300@@currency_exchange=true@@spa=true@@has_conference_halls=true@@car_park=true@@territory_size=2800@@number_bar=1@@dry_cleaning=true@@beach=mixed_sand_pebble@@garden=true@@animation_staff=true@@beach_size=40@@internet_in_hotel=free_wi_fi_in_the_room@@internet_in_hotel=free_wi_fi_in_public_areas@@number_restaurant=1@@distance_to_aeroport=60000@@steam=turkish_bath@@laundry=true@@has_bar=true@@reconstruct_year=2015@@build_year=2005@@kids_pool=true@@rental=rent_a_car@@has_restaurant=true@@playground=true@@hotel_line=3@@room_number=94@@sauna=true')
# ('en_name', 'Himeros Beach Hotel')
# ('ru_name', 'Himeros Beach Hotel')
# ('id', '1000000')
# ('rating', '5.1')
# ('stars', '3')
# ('latitude', '36.6034015971')


path_to_files = "data"
input_file_name = "hotels.tsv"
output_file_name = "hotels.json"

input_file_path = join(path_to_files, input_file_name)
output_file_path = join(path_to_files, output_file_name)

if not isfile(output_file_path):
 with open(input_file_path) as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    allHotels = {}
    for row in reader:
        allHotels[row["name"]] = (unidecode(row["name"]), row["id"], row['stars'])

    with open(output_file_path, 'w+') as outfile:
        json.dump(allHotels, outfile, indent=4)
else:
    with open(output_file_path) as infile:
        allHotels = json.load(infile)

if __file__ == "__main__":
    print(len(allHotels))
    for name, hotel in list(allHotels.items())[:1000]:
        print(name, "||", hotel[0])

def getHotelsDict():
    return allHotels


