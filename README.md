# Component-tester
This is going to be my project for week 4 of Hack Club halflife. It is a custom board for testing different components. I built this to have a quick way to test circuits, and components. It has 3 modes, continuity testing, analog voltage reading, and digital high/low reading.

## Usage, limitations:
This circuit is designed to handle inputs of no more than 5V, so it is only for testing 5V, and 3.3V logic, nothing higher. uses the RP2040s analog pins for voltage detection, so accuracy also might not be perfect. There are also 3.3V, 5V, and GND output pins, those are for quickly powering breadboard circuits, and components in need of testing. For continuity testing make sure that the circuit is fully unpowered, otherwise, it might fry the pin. To navigate the UI, you need to use the 2 buttons on the side. When in the menu, you can scroll through the options, and select a mode with the bottom button. When in one of the modes, to return to the menu you need to press the top button.

## Assembly:
To assemble, you need to first solder on the resistors, they are designed so you should be able to hand solder them. After that you can solder on the XIAO either SMD or through hole, both should work. For the buttons, you shuld solder them up to their place labeled SW1, and SW2. For the OLED, yo just need to solder it on with a header to the 4 I2C pins up top. On the sides for the headers, you can use either male, or female headers, whichever you like to connect the jumper wires to more.

## Firmware
The latest CircuitPython will need to be downloaded to the XIAO for the code to work. it can be downloaded ![here](https://circuitpython.org/board/seeeduino_xiao_rp2040/). The libraries are from the ![CircuitPython library bundle](https://circuitpython.org/libraries)

Copy everything from the firmware folder onto the board, and it should run.

## Images:
![Render](https://github.com/jivespark/Component-tester/blob/main/Images/Render.png?raw=true)

![PCB](https://github.com/jivespark/Component-tester/blob/main/Images/PCB.png?raw=true)

![Schematic](https://github.com/jivespark/Component-tester/blob/main/Images/Schematic.png?raw=true)

## BOM:
