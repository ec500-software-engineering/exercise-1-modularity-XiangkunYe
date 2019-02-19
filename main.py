"""
Created on 02/10/2019
@author: Xiangkun Ye
"""

from input import getPatientInfo, readSensorData
from storage import insert, searchPerson, searchTime, update, deletePerson
from alert_system import alertCheck
from output import patient

PatientInfo = getPatientInfo()
SensorData = readSensorData()
insert(PatientInfo, SensorData)
alert, PInfo = alertCheck(PatientInfo, SensorData)
patient1 = patient()
patient1.recieveFromAlert(alert)
print("Here's the final output that would display on UI: ")
patient1.send_alert_to_UI(PInfo)
print("\nLet's search a person with PatientID 1234: ")
print(searchPerson('1234'))
print("\nLet's search a person with PatientID 1234 and in time 12:05:20pm-18/01/2019: ")
print(searchTime('1234', '12:05:20pm-18/01/2019'))
print("\nLet's update this table to set pulse = 100: ")
update('1234', '12:05:20pm-18/01/2019', 'pulse', '100')
print(searchPerson('1234'), '\n')
deletePerson('1234')
deletePerson('1234')
