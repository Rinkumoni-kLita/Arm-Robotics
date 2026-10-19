from machine import Pin, PWM, ADC #import libraries for Pin, PWM, ADC
from time import sleep
    
    
servoPin0 = PWM(Pin(14)) # rotating base
servoPin0.freq(50)
servoPin1 = PWM(Pin(17)) # first joiny
servoPin1.freq(50)
servoPin2 = PWM(Pin(16)) # second joint
servoPin2.freq(50)       
servoPin3 = PWM(Pin(15)) #3rd joint
servoPin3.freq(50)
servoPin4 = PWM(Pin(18)) # claw
servoPin4.freq(50)



servos = [servoPin0, servoPin1, servoPin2, servoPin3]

def interval_mapping(x, in_min, in_max, out_min, out_max):
    """
    Maps a value from one range to another.
    This function is useful for converting servo angle to pulse width.
    """
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def servo_write(pin, angle):
    """
    Moves the servo to a specific angle.
    The angle is converted to a suitable duty cycle for the PWM signal.
    """
    pulse_width = interval_mapping(
        angle, 0, 180, 0.5, 2.5
    )  # Map angle to pulse width in ms
    duty = int(
        interval_mapping(pulse_width, 0, 20, 0, 65535)
    )  # Map pulse width to duty cycle
    pin.duty_u16(duty)  # Set PWM duty cycle


def straight_up():
    servo_write(servoPin1, 110)
    servo_write(servoPin2, 100)
    servo_write(servoPin3, 80)
    

def down():
    servo_write(servoPin1, 60)
    servo_write(servoPin2, 40)
    servo_write(servoPin3, 30)


straight_up()
sleep(0.3)
down()

logf = open("logfile.csv","a")
try:
    logf.write("hello!")
    logf.write(",")
except OSError:
    print("Disk full?")
logf.close()