This is a Python 3.6 Script to enable the usage of a Sega Genesis Controller as keyboard input.

Arduino Library can be found here, courtesy of jonthysell:
https://github.com/jonthysell/SegaController

Tested using an Elegoo Uno R3 and a Three Button official Sega Genesis Controller.

Usage:
1) Acquire the needed dependancies for the Python script. This usually entails running the command 'pip install pynput', to install the pynput library.
2) Setup jonthysell's Arduino library and connect your Controller to your Arduino. Controller port pinout and default Arduino pins are detailed in his github repo, as well as the arduino libraries and example sketches themselves.
3) Confirm the Arduino is sending serial data, and take note of which port the connection is made on.
4) Open threebutton.py in your favorite text editor, and change the string COM to whatever port your Arduino is communicatting on. In addition, you may change the key mappings at this time, too. By default, the script only handles 3 button controllers, but support for 6 button only requires a change in one line of code. Can you find it? Hint: How long is the keylist passed into PressHandler's constructor?
5) Open your favorite game, map the controls to the keys you chose in step 4.
6) Execute the python script, and enjoy!
