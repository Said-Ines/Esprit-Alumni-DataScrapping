import json
from pymongo import MongoClient
import chardet


# Making Connection
myclient = MongoClient("mongodb://localhost:27017/")

# database
db = myclient["EspritAlumni"]

# Created or Switched to collection
# names: GeeksForGeeks
Collection = db["linkedin_jobs_germany"]

# Loading or Opening the json file
with open('C:/Users/jerby/Downloads/basic-scrapy-project-main/m/jobs3.json',encoding='utf-8') as file:
	file_data = json.load(file)
	
# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else insert_one is used
if isinstance(file_data, list):
	Collection.insert_many(file_data)
else:
	Collection.insert_one(file_data)
