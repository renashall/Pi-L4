import time
from SmartCarModules.Motor import *
import RPi.GPIO as GPIO

class Line_Tracking:
    def __init__(self):
        self.IR01 = 14
        self.IR02 = 15
        self.IR03 = 23
    
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IR01,GPIO.IN)
        GPIO.setup(self.IR02,GPIO.IN)
        GPIO.setup(self.IR03,GPIO.IN)
        
    def run(self):
        while True:
            L = GPIO.input(self.IR01)
            M = GPIO.input(self.IR02)
            R = GPIO.input(self.IR03)
            
            self.LMR= 0 #create the LMR expression
            
            if self.LMR == 0b001: #Right activated, left turn
                continue 
            
            elif self.LMR == 0b010: #Middle activated, go forward
                continue 
            
            elif self.LMR == 0b011: #Middle and right activated, left turn
                continue 
            
            elif self.LMR == 0b100: #left, right turn
                continue 
            
            elif self.LMR == 0b101: #The sides are activated
                #Could be used as a special condition
                continue 
            
            elif self.LMR == 0b110: #left and middle, right turn
                continue 
            
            elif self.LMR == 0b111: #All activated, stop line
                continue 
                
            elif self.LMR == 0b000: #None Activated: Car fell off the track
                continue 
            
infrared=Line_Tracking()

if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        infrared.run()
    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)

