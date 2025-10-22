import time
import numpy as np
from rustypot import Scs0009PyController


ID_1 = 4 #Change to servo ID you want to calibrate
MiddlePos_1 = 0 #Middle position for servo ID_1 


c = Scs0009PyController(
        serial_port="COM60",
        baudrate=1000000,
        timeout=0.5,
    )

def main():
    c.write_torque_enable(ID_1, 1) 
    #1 = On / 2 = Off / 3 = Free
    
    while True:
        CloseFinger()
        time.sleep(3)

        OpenFinger()
        time.sleep(1)

def CloseFinger ():
    c.write_goal_speed(ID_1, 6) # Set speed for ID_1 to 6 => Max Speed
    Pos_1 = np.deg2rad(MiddlePos_1+90)
    c.write_goal_position(ID_1, Pos_1)
    time.sleep(0.01)

def OpenFinger():
    c.write_goal_speed(ID_1, 6) # Set speed for ID_1 to 6 => Max Speed
    Pos_1 = np.deg2rad(MiddlePos_1-30)
    c.write_goal_position(ID_1, Pos_1)
    time.sleep(0.01)

if __name__ == '__main__':
    main()


