import serial
from time import sleep
import sys
from pynput.keyboard import Key, Controller

keyboard = Controller()

def dummy(ipt):
    pass

dictionary = {-1: keyboard.release,
              0: dummy,
              1: keyboard.press}

class PressHandler:
    def __init__(self, keylist):
        self.old_state = [0 for i in range(8)]
        self.new_state = [0 for i in range(8)]
        self.key_list = keylist

    def process_statechange(self, statechange):
        for change, key in zip(statechange, self.key_list):
            dictionary[change](key)

    def handleinput(self, serial_line):
        if serial_line =='':
            return
        self.new_state = [0 if x == '0' else 1 for x in serial_line[1:-4]]
        self.state_change = [j-i for i, j in zip(self.old_state, self.new_state)]
        self.old_state = self.new_state
        self.process_statechange(self.state_change)


ph = PressHandler(['u','d','l','r','s','a','b','c'])
COM = 'COM4'
BAUD = 9600

ser = serial.Serial(COM, BAUD, timeout = .1)

print('Waiting for device');
sleep(3)
print(ser.name)

while True:
    ph.handleinput(str(ser.readline().decode().strip('\r\n')))
