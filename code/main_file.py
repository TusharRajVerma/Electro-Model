import os
import numpy as np
import pandas as pd
from sklearn import preprocessing
from ACS import *
from MCP3008 import *
import sys, time
from array import *

print("Press CTRL+C to abort.")
t = 0
while True:                                          #while values coming on the pin 
      acs = ACS();
      t = t+1                                        
print(t)                                             #total time the appliance is in running state
      