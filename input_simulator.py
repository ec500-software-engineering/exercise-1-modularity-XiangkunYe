'''
Created on 02/12/2019
@author: Xiangkun Ye
'''

import json
import time
import random

def simulator():

    name = ['Kun', 'Pang', 'Wan', 'Su', 'Chen', 'Jack', 'Steve', 'Jobs', 'Tim', 'Cook']
    gender = ['Male', 'Female']
    age = ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100']

    patientData = {}
    patientId = random.randint(1, 1000)
    name = random.choice(name)
    gender = random.choice(gender)
    age = random.choice(age)
    patientData[patientId] = {'name':name,'gender':gender,'age':age}
    patient = json.dumps(patientData)

    sensorData = {}
    sensorData[patientId] = {
	 		"pulse": random.randint(10, 200),
    		'pulseRange': {"lower": '50', "upper": '120'},
    		'bloodPressure': random.randint(10, 200),
    		'pressureRange': {'lower': '30', 'upper': '100'},
    		'bloodOx': random.randint(10, 200),
    		'oxRange': {'lower': '60', 'upper': '90'},
    		'time': time.ctime()
        }
    sensor = json.dumps(sensorData)

    return patient, sensor
