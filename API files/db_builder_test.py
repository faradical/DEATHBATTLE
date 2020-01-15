'''
---------------------------------------------------------------------------------------------------------------------
Name:			deathbattle_DB_builder.py

Version:		1.0

Author:			Seth Pruitt

Usage:			python3 deathbattle_DB_builder.py

Description:	This script builds out the deathbattle mongo database

Comments:		01-4-20 Began writing script
---------------------------------------------------------------------------------------------------------------------
'''

#DENDENCIES
from pymongo import MongoClient as MC
import requests

#ESTABLISH BATABASE CONNECTION
client = MC()
db = client.death_battle
col = db.characters

col.drop()

#URL FOR SUPERHERO API
url = 'https://www.superheroapi.com/api.php/10220306273917389/'

#LOOP THROUGH DATA  ADDING CHARACTERS TO API
count = 0
for i in range(1, 732):

	#EXECUTE API REQUEST
	hero_url = url + str(i)
	superhero_info = requests.get(hero_url).json()

	#INSERT RESPONSE INTO DATABASE
	col.insert_one(superhero_info)

	#CHECK DATABASE INSERTION
	record = col.find_one({"id":str(i)})
	name = superhero_info['name']
	if record:
		print(f'{name}\t\t\tID:{i}\t\t\tSuccessfully inserted into database')
	else:
		print(f'{name}\t\t\tID:{i}\t\t\tEncountered an error')

	#INCREMENT COUNTER
	count += 1