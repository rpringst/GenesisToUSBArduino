#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  threebutton.py
#  
#  Copyright (c) 2018 Robert P. Ringstad
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import serial
from time import sleep
import sys
from pynput.keyboard import Key, Controller


class PressHandler:
    keyboard = Controller()

    def dummy_function(dummy_input):
        pass

    function_dict = {-1: keyboard.release,
              0: dummy_function,
              1: keyboard.press}

    def __init__(self, keylist):
        self.key_list = keylist
        self.old_state = [0 for i in range(len(self.key_list))]
        self.new_state = [0 for i in range(len(self.key_list))]

    def process_statechange(self, statechange):
        for change, key in zip(statechange, self.key_list):
            function_dict[change](key)

    def handleinput(self, serial_line):
        if serial_line == '':
            return
        self.new_state = [0 if x == '0' else
                          1 for x in serial_line[1:-4]]
        self.state_change = [j-i for i, j in zip(self.old_state,
                                                 self.new_state)]
        self.old_state = self.new_state
        self.process_statechange(self.state_change)


def main(args):
    ph = PressHandler(['u','d','l','r','s','a','b','c'])
    COM = 'COM4'
    BAUD = 9600

    print('Connecting to Arduino...')
    ser = serial.Serial(COM, BAUD, timeout = .1)
    sleep(3)
    print('Connected on Port: {}'.format(ser.name))

    while True:
        ph.handleinput(str(ser.readline().decode().strip('\r\n')))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
