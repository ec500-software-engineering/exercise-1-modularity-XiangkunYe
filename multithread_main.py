"""
Created on 02/12/2019
@author: Xiangkun Ye
"""

from input_simulator import simulator
from storage import insert
from alert_system import alertCheck
from output import patient
import threading
import time
import random

def run(PatientInfo, SensorData):
    insert(PatientInfo, SensorData)
    alert, PInfo = alertCheck(PatientInfo, SensorData)
    patient1 = patient()
    patient1.recieveFromAlert(alert)
    patient1.send_alert_to_UI(PInfo)
    print('\n')

while True:
    PatientInfo, SensorData = simulator()
    # Every time we receive a new data, we open a  new thread to deal with it
    # Since it would end fast, I believe even a normal laptop can handle
    # lots of concurrent input.
    t = threading.Thread(target=run, args=(PatientInfo, SensorData))
    t.start()
    time.sleep(random.randint(1, 5))
