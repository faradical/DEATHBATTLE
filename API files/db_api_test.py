'''
---------------------------------------------------------------------------------------------------------------------
Name:			app.py

Version:		1.0

Author:			Seth Pruitt

Usage:			Included in files for apache configuration

Description:	Defines routes for API to pull character information from Mongo DB

Comments:		01-11-20 Began writing script
---------------------------------------------------------------------------------------------------------------------
'''

#DENDENCIES
from pymongo import MongoClient as MC
from flask import Flask, jsonify, request
from bson import json_util
import json
#from flask_pymongo import PyMongo

# DEFINE FLASK APPLICATION
app = Flask(__name__)

#ESTABLISH BATABASE CONNECTION
client = MC()
db = client.death_battle
col = db.characters

# DEFINE ROUTES
@app.route("/")
def home():
	print("Home Route accessed.")
	return "Hello, I love Xing!"

@app.route("/ID/<characterID>")
def IDLookup(characterID):
	print(f"Character Lookup for {characterID} attempted.")
	mDBobj = col.find_one({"id":characterID})
	response = json_util.dumps(mDBobj)
	return response

@app.route("/all_names")
def AllNames():
	print(f"All names route requested.")
	names = []
	for i in list(col.find()):
		if i['powerstats']['intelligence'] != "null" and i['powerstats']['strength'] != "null" and i['powerstats']['speed'] != "null" and i['powerstats']['durability'] != "null" and i['powerstats']['power'] != "null" and i['powerstats']['combat'] != "null":
			names.append({"name": i['name'], "value": i['id']})
	response= json_util.dumps({"characters": names})
	return response

@app.route("/new_hero", methods=['POST'])
def new_hero():
	data = request.get_json(force=True)
	print(f"New hero post attempted for {data['name']}")
	print(list(col.find())[-1])
	last_id = int(list(col.find())[-1]['id'])
	print(last_id)
	new_id = last_id + 1
	# Insertion into Mongo DB
	data['id'] = str(new_id)
	print(data['id'])

	col.insert_one(data)

	record = col.find_one({"id":str(data['id'])})
	name = data['name']
	if record:
		return(f'{name}: Successfully inserted into database.')
	else:
		return(f'{name}: Encountered an error inserting into database.')

	# If Mongo is not running, try this instead:
	# return(f"New hero post attempted for {data['name']}")


# RUN APPLICATION
if __name__ == "__main__":
	app.run() #debug=True, port=5000) #Turn debug off in production