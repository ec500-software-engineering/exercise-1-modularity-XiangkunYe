'''
Created on 02/10/2019
@author: Xiangkun Ye
Source code copied from https://github.com/alexlin0625/EC500_Spring19/blob/alert-system/alert_system.py.
With lots of modifications to make it work.
Basically I rewrited the whole file.
The original one by mohitbeniwal is bullshit.
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 09:29:32 2019

@author: mohitbeniwal
"""
import json

def alertCheck(PatientInfo, SensorData):
    j=json.loads(SensorData)
    alert_message = ''
    for value in j.values():
        val = value
    if(int(val["bloodPressure"])<int(val["pressureRange"]["lower"])):
        alert_message+="BloodPressure is Too low, "
    elif(int(val["bloodPressure"])>int(val["pressureRange"]["upper"])):
        alert_message="BloodPressure is Too high, "
    if(int(val["pulse"])<int(val["pulseRange"]["lower"])):
        alert_message+="Pulse is Too low, "
    elif(int(val["pulse"])>int(val["pulseRange"]["upper"])):
        alert_message+="Pulse is Too high, "
    if(int(val["bloodOx"])<int(val["oxRange"]["lower"])):
        alert_message+="BloodOx is Too low, "
    elif(int(val["bloodOx"])>int(val["oxRange"]["upper"])):
        alert_message+="BloodOx is Too high, "
    if alert_message == '':
        alert_message = 'Normal'
    ui_dict={"alert_message":alert_message, "bloodPressure":val["bloodPressure"], "pulse":val["pulse"], "bloodOx":val["bloodOx"]}
    ui_json=json.dumps(ui_dict)
    return ui_json, PatientInfo
