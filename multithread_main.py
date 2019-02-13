"""
Created on 02/12/2019
@author: Xiangkun Ye
"""

from input_simulator import *
from storage import *
from alert_system import *
from output import *
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
    t = threading.Thread(target=run, args=(PatientInfo, SensorData))
    t.start()
    time.sleep(random.randint(1, 5))