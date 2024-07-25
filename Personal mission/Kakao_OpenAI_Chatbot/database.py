import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI)
db = client['chatbot']

def add_schedule(details):
    schedule_collection = db['schedule']
    schedule_collection.insert_one({"details": details})

def get_schedules():
    schedule_collection = db['schedule']
    schedules = schedule_collection.find()
    return list(schedules)

def delete_schedule(details):
    schedule_collection = db['schedule']
    schedule_collection.delete_one({"details": details})

def add_assignment(action, details):
    assignment_collection = db['assignment']
    assignment_collection.insert_one({"action": action, "details": details})

def get_assignments(action):
    assignment_collection = db['assignment']
    assignments = assignment_collection.find({"action": action})
    return list(assignments)

def add_material(topic, link):
    materials_collection = db['materials']
    materials_collection.insert_one({"topic": topic, "link": link})

def get_materials(topic):
    materials_collection = db['materials']
    materials = materials_collection.find({"topic": topic})
    return list(materials)

def add_notice(content):
    notice_collection = db['notice']
    notice_collection.insert_one({"content": content})

def get_notices():
    notice_collection = db['notice']
    notices = notice_collection.find()
    return list(notices)