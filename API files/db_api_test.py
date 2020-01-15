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
from flask import Flask, jsonify
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
def hello():
	return "Hello, I love Xing!"

@app.route("/ID/<characterID>")
def IDLookup(characterID):
	mDBobj = col.find_one({"id":characterID})
	response = json.dumps(mDBobj, default=json_util.default)
	print(type(response))
	return response

@app.route("/all_names")
def AllNames():
	names = []
	for i in list(col.find()):
		if i['powerstats']['intelligence'] != "null" and i['powerstats']['strength'] != "null" and i['powerstats']['speed'] != "null" and i['powerstats']['durability'] != "null" and i['powerstats']['power'] != "null" and i['powerstats']['combat'] != "null":
			names.append('{"name":"' + i['name'] + '", "value":"' + i['id'] + '"}')
	response= '{"characters":[' + ','.join(names) + ']}'
	return response

# RUN APPLICATION
if __name__ == "__main__":
	app.run()