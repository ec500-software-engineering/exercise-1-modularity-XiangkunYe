"""
Created on 02/10/2019
@author: Xiangkun Ye
"""

import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["sensor"]
mycol = mydb["patient"]

# Please note that all input parameters for all functions should be string (except PatientInfo and SensorData should be json)

def insert(PatientInfo, SensorData):
    '''
    this function will receive the json information returned by getPatientInfo() and readSensorData()
    in input.py from input module and insert them as a whole table into database.
    '''

    try:
        PatientInfo = json.loads(PatientInfo)
        SensorData = json.loads(SensorData)
        dict = {}
        for id in PatientInfo:
            dict['PatientID'] = id
            for k, v in PatientInfo[id].items():
                dict[k] = v
            for k, v in SensorData[id].items():
                dict[k] = v
        mycol.insert_one(dict)
    except Exception:
        print("It seems that some things went wrong with your input file, please check it.")

def searchPerson(PatientID):
    '''
    this function will use PatientID to search and return all tables of this patient as a list.
    '''

    res = mycol.find({'PatientID': PatientID}, {'_id': 0})
    val = []
    for item in res:
        val.append(item)
    if val:
        return val
    else:
        print("It seems that we don't have this person's data.")

def searchTime(PatientID, Time):
    '''
    this function will use PatientID and Time to search a specific table and return as a list.
    '''

    res = mycol.find({'PatientID': PatientID, 'time': Time}, {'_id': 0})
    val = []
    for item in res:
        val.append(item)
    if val:
        return val
    else:
        print("It seems that we don't have this person's data in select time.")

def deletePerson(PatientID):
    '''
    delete all tables for this person.
    '''

    res = mycol.delete_many({'PatientID': PatientID})
    if res.deleted_count:
        print("Successfully delete it!")
    else:
        print("It seems that there's no such table to delete.")


def deleteTime(PatientID, Time):
    '''
    delete a specific table according to ID and Time.
    '''

    res = mycol.delete_many({'PatientID': PatientID, 'time': Time})
    if res.deleted_count:
        print("Successfully delete it!")
    else:
        print("It seems that there's no such table to delete.")

def update(PatientID, Time, Item, Value):
    '''
    update the 'Item' item in the table of PatientID and Time with new value 'Value'.
    '''

    query = {'PatientID': PatientID, 'time': Time}
    new = {'$set': {Item: Value}}
    res = mycol.update_one(query, new)
    if res.modified_count:
        print("Successfully update it!")
    else:
        print("It seems that there's no such table to update.")
