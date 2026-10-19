# arduino_robot_arm


## Episode 1

[![Watch the video](/Part_1/ep1.jpg)](https://youtu.be/c6mrcNEFBoA?si=2KJQS0jbuTS4Maua)

#### Hardware 
- [x] Connect two 9g motors and the potentiometers to the Arduino board to control movement

### Robot structure
- [x] First prototypes attempt for arms (carton, small lego + scotch tape)

#### Software
- [x] Simple control for the motors through potentiometers (each potentionmeter controls one motor in real time)

## Episode 2

[![Watch the video](/Part_2/ep2thumb.png)](https://www.youtube.com/watch?v=xB-Buinw3lE&)


#### Hardware

- [x] Add some buttons for different saved positions (pre-configure angle values for each potentiometer to define a position)



#### Robot structure
- [X] More prototyping for arms with plastic, LEGO, other
- [X] Better "arm" structure and interconnection - with ~three~ two motors standing on table and all supported / able to stand and move

#### Software
- [X] Make some functions for assigning a fixed position and triggering this with a button 
- [ ] ~~Refactor code with the Python module for Arduino~~ (Arduino Uno does not support micropython - try this with a future board!)
- [X] Add dynamic movement from the potentiometer rathar than direct position-to-angle mapping to integrate with the pre-saved positions in the buttons


## Episode 3

[![Watch the video](/Part_3/ep3thumb.png)](https://www.youtube.com/watch?v=xILy-UI7aAQ)

#### Hardware
- [X] Add a battery for more power - figure out needed voltage, resistors, power distribution, etc

#### Robot structure
- [X] Use a [3D printed model](https://www.youtube.com/watch?v=xILy-UI7aAQ)

#### Software 
- [X] Refactor to micropython (using Raspberry Pico)
- [X] Control movement with code instead of potentiometer

## Episode 4

[![Watch the video](/Part_4/ep4thumb.png)](https://youtu.be/aqYN7jCgId0)

#### Software
- [X] Use Copilot to generate more complex movement code

## Episode 5
[![Watch the video](/Part_5/ep5thumb.png)](https://www.youtube.com/watch?v=2hYSKIdKS9w)

- [X] Go from the simple 3D printed POC to the LeRobot SO101 3D printed arms
- [X] Upgrade to the Feetech motors
- [X] Use the LeRobot code for callibration, teleoperation.


## Episode 6

### Software
- [X] Refactor the Copilot-generated code into actually good Python code for the Pico-controlled Arm movements
- [X] Implement logging for the movement and export into a JSON file for future exploration
- [X] Simple POC implementation of Rerun to visualize the movements based on the collected logs

## Episode 7

- [X] Record own dataset with LeRobot SDK into huggingface and train a custom policy to pick up dog toy


