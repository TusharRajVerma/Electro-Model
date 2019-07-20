import time
import math
from MCP3008 import MCP3008
from array import *
class ACS():
    ACS_PIN = 0                                                                           #sensor connected to the pin 0
    avgSamples = 10             
    sensorValue = 0
    sensitivity = 100.0 / 500.0
    Vref = 2500
    RL_VALUE = 5 
    
    def __init__(self, Co=0, analogPin=0):
        
        self.ACS_PIN = analogPin
        self.adc = MCP3008()
        print("Calibrating...")
        self.Co = self.ACSCalibration(self.ACS_PIN)
        print("Calibration is done...\n")
        print("Co=%f A % self.Co)                                                    #current calculated by the sensor 
        return 0
     
    def ACSResistanceCalculation(self, raw_adc):
        return float(self.RL_VALUE*(1023.0-raw_adc)/float(0.000000000001+raw_adc));
     
    def ACSCalibration(self, acs_pin):
        val = 0.0
        for i in range(self.avgSamples):          # take multiple samples
            sensorValue += ACSResistanceCalculation(self.adc.read(acs_pin))
            delay(2)
          
        sensorValue = sensorValue / avgSamples
        voltage = 4.88 * sensorValue
        current = (voltage - Vref) * sensitivity
        return current;
      
      
 