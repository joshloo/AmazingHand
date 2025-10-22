import time
import numpy as np

from rustypot import Scs0009PyController


ID_1 = 1 #Change to servo ID you want to calibrate 
ID_2 = 2 #Change to servo ID you want to calibrate 
ID_3 = 3 #Change to servo ID you want to calibrate 
ID_4 = 4 #Change to servo ID you want to calibrate 

MiddlePos_1 = 0 #Middle position for servo ID_1 
MiddlePos_2 = 0 #Middle position for servo ID_2
MiddlePos_3 = 5 #Middle position for servo ID_3 
MiddlePos_4 = -10 #Middle position for servo ID_4


c = Scs0009PyController(
        serial_port="COM60",
        baudrate=1000000,
        timeout=0.5,
    )

def main():
    

    c.write_torque_enable(1, 1) # change to ID
    c.write_torque_enable(2, 1) # change to ID
    c.write_torque_enable(3, 1) # change to ID
    c.write_torque_enable(4, 1) # change to ID

    #1 = On / 2 = Off / 3 = Free
    c.write_goal_speed(ID_1, 100) # Set speed for ID_1 to 6 => Max Speed
    c.write_goal_speed(ID_2, 100) # Set speed for ID_1 to 6 => Max Speed
    c.write_goal_speed(ID_3, 100) # Set speed for ID_1 to 6 => Max Speed
    c.write_goal_speed(ID_4, 100) # Set speed for ID_1 to 6 => Max Speed
    while True:
        

        CloseFinger()
        time.sleep(3)


        OpenFinger()
        time.sleep(3)

        #c.sync_write_raw_goal_position([1,2], [50,50])
        #time.sleep(1)

        #a=c.read_present_position(1)
        #b=c.read_present_position(2)
        #a=np.rad2deg(a)
        #b=np.rad2deg(b)
        #print(f'{a} {b}')
        #time.sleep(0.001)



def CloseFinger ():
    
    # c.write_goal_speed(ID_1, 6) # Set speed for ID_1 to 6 => Max Speed
    # c.write_goal_speed(ID_2, 6) # Set speed for ID_1 to 6 => Max Speed
    Pos_1 = np.deg2rad(MiddlePos_1+90)
    Pos_2 = np.deg2rad(MiddlePos_2-90)
    
    Pos_3 = np.deg2rad(MiddlePos_3+90)
    Pos_4 = np.deg2rad(MiddlePos_4-90)
    
    c.write_goal_position(ID_1, Pos_1)
    c.write_goal_position(ID_2, Pos_2)
    c.write_goal_position(ID_3, Pos_3)
    c.write_goal_position(ID_4, Pos_4)
    time.sleep(0.01)


def OpenFinger():
    # c.write_goal_speed(ID_1, 6) # Set speed for ID_1 to 6 => Max Speed
    # c.write_goal_speed(ID_2, 6) # Set speed for ID_1 to 6 => Max Speed
    Pos_1 = np.deg2rad(MiddlePos_1-30)
    Pos_2 = np.deg2rad(MiddlePos_2+30)
    Pos_3 = np.deg2rad(MiddlePos_3-30)
    Pos_4 = np.deg2rad(MiddlePos_4+30)

    c.write_goal_position(ID_1, Pos_1)
    c.write_goal_position(ID_2, Pos_2)    
    c.write_goal_position(ID_3, Pos_3)
    c.write_goal_position(ID_4, Pos_4)

    time.sleep(0.01)






if __name__ == '__main__':
    main()


