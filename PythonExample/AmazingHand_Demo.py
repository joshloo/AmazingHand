import time
import numpy as np
import random
import math

from rustypot import Scs0009PyController

#Side
Side = 1 # 1=> Right Hand // 2=> Left Hand


#Speed
MaxSpeed = 7
CloseSpeed = 3

#Interpolation Mode
InterpolationMode = "sigmoid"  # Options: "linear" or "sigmoid"

#Fingers middle poses
# MiddlePos = [3, 0, -5, -8, -2, 5, -12, 0] # replace values by your calibration results
MiddlePos = [0, 0, 0, 0, 0, 0, 0, 0] # replace values by your calibration results

c = Scs0009PyController(
        serial_port="COM60",
        baudrate=1000000,
        timeout=0.5,
    )



def main():
    
    c.write_torque_enable(1, 1)  #1 = On / 2 = Off / 3 = Free
    t0 = time.time()

    while True:
        t = time.time() - t0

        # ===== PREVIOUS FLAVORS (COMMENTED OUT) =====
        # # Flavor 1: Max speed open and close
        # print("=== Flavor 1: Max Speed Open and Close ===")
        # for i in range(1):
        #     OpenHand_MaxSpeed()
        #     time.sleep(0.5)
        #     CloseHand_MaxSpeed()
        #     time.sleep(0.5)
        # 
        # print("Waiting 5 seconds before next flavor...")
        # time.sleep(5)

        # # Flavor 2: Variable speed - decrease, increase, decrease
        # print("=== Flavor 2: Variable Speed (Decrease -> Increase -> Decrease) ===")
        # OpenClose_VariableSpeed()
        # 
        # print("Waiting 5 seconds before next flavor...")
        # time.sleep(5)

        # # Flavor 3: Random fast and slow intensity
        # print("=== Flavor 3: Random Fast and Slow Intensity ===")
        # for i in range(3):
        #     OpenClose_RandomSpeed()
        #     time.sleep(0.3)
        # 
        # print("Waiting 5 seconds before next cycle...")
        # time.sleep(5)

        # ===== NEW FLAVOR: Open Hand with Configurable Interpolation (1 to 10 seconds) =====
        print(f"=== Open Hand ({InterpolationMode} interpolation) - Looping from 1 to 10 seconds ===")
        
        for duration in range(1, 11):
            print(f"\n--- Opening hand in {duration} second(s) ---")
            OpenHand_Linear_Duration(duration, mode=InterpolationMode)
            time.sleep(1)
            
            print("Closing hand...")
            CloseHand()
            time.sleep(1)

        ################################
        # Other gestures (commented out for now)
        # SpreadHand()
        # time.sleep(0.6)
        # ClenchHand()
        # time.sleep(0.6)

        # OpenHand()
        # time.sleep(0.2)

        # Index_Pointing()
        # time.sleep(0.4)
        # Nonono()
        # time.sleep(0.5)
        
        # OpenHand()
        # time.sleep(0.3)

        # Perfect()
        # time.sleep(0.8)

        # OpenHand()
        # time.sleep(0.4)

        # Victory()
        # time.sleep(1)
        # Scissors()
        # time.sleep(0.5)

        # OpenHand()
        # time.sleep(0.4)

        # Pinched()
        # time.sleep(1)

        # Fuck()
        # time.sleep(0.8)

        ################################
        #trials

        #c.sync_write_raw_goal_position([1,2], [50,50])
        #time.sleep(1)

        #a=c.read_present_position(1)
        #b=c.read_present_position(2)
        #a=np.rad2deg(a)
        #b=np.rad2deg(b)
        #print(f'{a} {b}')
        #time.sleep(0.001)



def OpenHand():
    Move_Index (-35,35, MaxSpeed)
    Move_Middle (-35,35, MaxSpeed)
    Move_Ring (-35,35, MaxSpeed)
    Move_Thumb (-35,35, MaxSpeed)

def CloseHand():
    Move_Index (90,-90, CloseSpeed)
    Move_Middle (90,-90, CloseSpeed)
    Move_Ring (90,-90, CloseSpeed)
    Move_Thumb (90,-90, CloseSpeed+1)

def OpenHand_Progressive():
    Move_Index (-35,35, MaxSpeed-2)
    time.sleep(0.2)
    Move_Middle (-35,35, MaxSpeed-2)
    time.sleep(0.2)
    Move_Ring (-35,35, MaxSpeed-2)
    time.sleep(0.2)
    Move_Thumb (-35,35, MaxSpeed-2)

def SpreadHand():
    if (Side==1): # Right Hand
        Move_Index (4, 90, MaxSpeed)
        Move_Middle (-32, 32, MaxSpeed)
        Move_Ring (-90, -4, MaxSpeed)
        Move_Thumb (-90, -4, MaxSpeed)  
  
    if (Side==2): # Left Hand
        Move_Index (-60, 0, MaxSpeed)
        Move_Middle (-35, 35, MaxSpeed)
        Move_Ring (-4, 90, MaxSpeed)
        Move_Thumb (-4, 90, MaxSpeed)  
  
def ClenchHand():
    if (Side==1): # Right Hand
        Move_Index (-60, 0, MaxSpeed)
        Move_Middle (-35, 35, MaxSpeed)
        Move_Ring (0, 70, MaxSpeed)
        Move_Thumb (-4, 90, MaxSpeed)  
  
    if (Side==2): # Left Hand
        Move_Index (0, 60, MaxSpeed)
        Move_Middle (-35, 35, MaxSpeed)
        Move_Ring (-70, 0, MaxSpeed)
        Move_Thumb (-90, -4, MaxSpeed)
  
def Index_Pointing():
    Move_Index (-40, 40, MaxSpeed)
    Move_Middle (90, -90, MaxSpeed)
    Move_Ring (90, -90, MaxSpeed)
    Move_Thumb (90, -90, MaxSpeed)
  
def Nonono():
  Index_Pointing()
  for i in range(3) :
        time.sleep(0.2)
        Move_Index (-10, 80, MaxSpeed)
        time.sleep(0.2)
        Move_Index (-80, 10, MaxSpeed)
  
  Move_Index (-35, 35, MaxSpeed)
  time.sleep(0.4)
  
def Perfect():
  if (Side==1): #Right Hand
        Move_Index (50, -50, MaxSpeed)
        Move_Middle (0, -0, MaxSpeed)
        Move_Ring (-20, 20, MaxSpeed)
        Move_Thumb (65, 12, MaxSpeed)

  
  if (Side==2): #Left Hand
        Move_Index (50, -50, MaxSpeed)
        Move_Middle (0, -0, MaxSpeed)
        Move_Ring (-20, 20, MaxSpeed)
        Move_Thumb (-12, -65, MaxSpeed)
  
def Victory():
  if (Side==1): #Right Hand 
        Move_Index (-15, 65, MaxSpeed)
        Move_Middle (-65, 15, MaxSpeed)
        Move_Ring (90, -90, MaxSpeed)
        Move_Thumb (90, -90, MaxSpeed)

  
  if (Side==2): #Left Hand
        Move_Index (-65, 15, MaxSpeed)
        Move_Middle (-15, 65, MaxSpeed)
        Move_Ring (90, -90, MaxSpeed)
        Move_Thumb (90, -90, MaxSpeed)
  
def Pinched():
  if (Side==1): #Right Hand
        Move_Index (90, -90, MaxSpeed)
        Move_Middle (90, -90, MaxSpeed)
        Move_Ring (90, -90, MaxSpeed)
        Move_Thumb (0, -75, MaxSpeed)

  if (Side==2): #Left Hand
        Move_Index (90, -90, MaxSpeed)
        Move_Middle (90, -90, MaxSpeed)
        Move_Ring (90, -90, MaxSpeed)
        Move_Thumb (75, 5, MaxSpeed)

def Scissors():
  Victory();
  if (Side==1): #Right Hand
        for i in range(3):  
            time.sleep(0.2)
            Move_Index (-50, 20, MaxSpeed)
            Move_Middle (-20, 50, MaxSpeed)
            
            time.sleep(0.2)
            Move_Index (-15, 65, MaxSpeed)
            Move_Middle (-65, 15, MaxSpeed)
    

  if (Side==2): #Left Hand
        for i in range(3):
            time.sleep(0.2)
            Move_Index (-20, 50, MaxSpeed)
            Move_Middle (-50, 20, MaxSpeed)
            
            time.sleep(0.2)
            Move_Index (-65, 15, MaxSpeed)
            Move_Middle (-15, 65, MaxSpeed)

def Fuck():

  if (Side==1): #Right Hand
        Move_Index (90, -90, MaxSpeed)
        Move_Middle (-35, 35, MaxSpeed)
        Move_Ring (90, -90, MaxSpeed)
        Move_Thumb (0, -75, MaxSpeed)

  if (Side==2): #Left Hand
        Move_Index (90, -90, MaxSpeed)
        Move_Middle (-35, 35, MaxSpeed)
        Move_Ring (90, -90, MaxSpeed)
        Move_Thumb (75, 0, MaxSpeed)
  
def Move_Index (Angle_1,Angle_2,Speed):
    
    c.write_goal_speed(1, Speed)
    time.sleep(0.0002)
    c.write_goal_speed(2, Speed)
    time.sleep(0.0002)
    Pos_1 = np.deg2rad(MiddlePos[0]+Angle_1)
    Pos_2 = np.deg2rad(MiddlePos[1]+Angle_2)
    c.write_goal_position(1, Pos_1)
    c.write_goal_position(2, Pos_2)
    time.sleep(0.005)

def Move_Middle(Angle_1,Angle_2,Speed):    
    c.write_goal_speed(3, Speed)
    time.sleep(0.0002)
    c.write_goal_speed(4, Speed)
    time.sleep(0.0002)
    Pos_1 = np.deg2rad(MiddlePos[2]+Angle_1)
    Pos_2 = np.deg2rad(MiddlePos[3]+Angle_2)
    c.write_goal_position(3, Pos_1)
    c.write_goal_position(4, Pos_2)
    time.sleep(0.005)

def Move_Ring(Angle_1,Angle_2,Speed):    
    c.write_goal_speed(5, Speed)
    time.sleep(0.0002)
    c.write_goal_speed(6, Speed)
    time.sleep(0.0002)
    Pos_1 = np.deg2rad(MiddlePos[4]+Angle_1)
    Pos_2 = np.deg2rad(MiddlePos[5]+Angle_2)
    c.write_goal_position(5, Pos_1)
    c.write_goal_position(6, Pos_2)
    time.sleep(0.005)

def Move_Thumb(Angle_1,Angle_2,Speed):    
    c.write_goal_speed(7, Speed)
    time.sleep(0.0002)
    c.write_goal_speed(8, Speed)
    time.sleep(0.0002)
    Pos_1 = np.deg2rad(MiddlePos[6]+Angle_1)
    Pos_2 = np.deg2rad(MiddlePos[7]+Angle_2)
    c.write_goal_position(7, Pos_1)
    c.write_goal_position(8, Pos_2)
    time.sleep(0.005)


# Flavor 1: Max speed open and close
def OpenHand_MaxSpeed():
    Move_Index(-35, 35, MaxSpeed)
    Move_Middle(-35, 35, MaxSpeed)
    Move_Ring(-35, 35, MaxSpeed)
    Move_Thumb(-35, 35, MaxSpeed)

def CloseHand_MaxSpeed():
    Move_Index(90, -90, MaxSpeed)
    Move_Middle(90, -90, MaxSpeed)
    Move_Ring(90, -90, MaxSpeed)
    Move_Thumb(90, -90, MaxSpeed)


# Flavor 2: Variable speed - decrease, increase, decrease
def OpenClose_VariableSpeed():
    speeds = [7, 6, 5, 4, 3, 4, 5, 6, 7, 6, 5, 4]  # decrease -> increase -> decrease
    
    for speed in speeds:
        # Open hand with current speed
        Move_Index(-35, 35, speed)
        Move_Middle(-35, 35, speed)
        Move_Ring(-35, 35, speed)
        Move_Thumb(-35, 35, speed)
        time.sleep(0.4)
        
        # Close hand with current speed
        Move_Index(90, -90, speed)
        Move_Middle(90, -90, speed)
        Move_Ring(90, -90, speed)
        Move_Thumb(90, -90, speed)
        time.sleep(0.4)


# Flavor 3: Random fast and slow intensity
def OpenClose_RandomSpeed():
    # Random speed between 2 and 7
    open_speed = random.randint(2, MaxSpeed)
    close_speed = random.randint(2, MaxSpeed)
    
    print(f"  Open speed: {open_speed}, Close speed: {close_speed}")
    
    # Open hand with random speed
    Move_Index(-35, 35, open_speed)
    Move_Middle(-35, 35, open_speed)
    Move_Ring(-35, 35, open_speed)
    Move_Thumb(-35, 35, open_speed)
    time.sleep(0.4)
    
    # Close hand with random speed
    Move_Index(90, -90, close_speed)
    Move_Middle(90, -90, close_speed)
    Move_Ring(90, -90, close_speed)
    Move_Thumb(90, -90, close_speed)
    time.sleep(0.4)


# New Flavor: Configurable Interpolation Duration Open Hand Movement
def OpenHand_Linear_Duration(duration_seconds, mode="sigmoid"):
    """
    Opens the hand in exactly the specified duration with configurable interpolation.
    The movement can be linear or sigmoid-style (smooth acceleration/deceleration).
    
    Args:
        duration_seconds: The duration in seconds for the opening movement (1-10 seconds)
        mode: Interpolation mode - "linear" or "sigmoid" (default: "sigmoid")
    """
    # Starting angles (closed hand position)
    start_angles = {
        'index': (90, -90),
        'middle': (90, -90),
        'ring': (90, -90),
        'thumb': (90, -90)
    }
    
    # Target angles (open hand position)
    target_angles = {
        'index': (-35, 35),
        'middle': (-35, 35),
        'ring': (-35, 35),
        'thumb': (-35, 35)
    }
    
    # Time parameters
    total_duration = float(duration_seconds)  # seconds
    time_step = 0.05  # update every 50ms for smooth motion
    num_steps = int(total_duration / time_step)
    
    print(f"Starting {mode} movement over {total_duration} seconds with {num_steps} steps")
    
    # Use a moderate speed for smooth transitions
    speed = 5
    
    start_time = time.time()
    
    for step in range(num_steps + 1):
        # Calculate raw interpolation factor (0.0 to 1.0)
        t_raw = step / num_steps
        
        # Apply interpolation mode
        if mode == "sigmoid":
            # Sigmoid interpolation for smooth start and end
            # Using logistic function: 1 / (1 + e^(-k*(x-0.5)))
            # k=10 gives a nice smooth curve
            k = 10
            sigmoid_raw = 1 / (1 + math.exp(-k * (t_raw - 0.5)))
            sigmoid_min = 1 / (1 + math.exp(k * 0.5))  # value at t=0
            sigmoid_max = 1 / (1 + math.exp(-k * 0.5))  # value at t=1
            # Normalize to 0-1 range
            t = (sigmoid_raw - sigmoid_min) / (sigmoid_max - sigmoid_min)
        else:
            # Linear interpolation
            t = t_raw
        
        # Interpolate angles for each finger
        # Index finger
        index_angle1 = start_angles['index'][0] + t * (target_angles['index'][0] - start_angles['index'][0])
        index_angle2 = start_angles['index'][1] + t * (target_angles['index'][1] - start_angles['index'][1])
        
        # Middle finger
        middle_angle1 = start_angles['middle'][0] + t * (target_angles['middle'][0] - start_angles['middle'][0])
        middle_angle2 = start_angles['middle'][1] + t * (target_angles['middle'][1] - start_angles['middle'][1])
        
        # Ring finger
        ring_angle1 = start_angles['ring'][0] + t * (target_angles['ring'][0] - start_angles['ring'][0])
        ring_angle2 = start_angles['ring'][1] + t * (target_angles['ring'][1] - start_angles['ring'][1])
        
        # Thumb
        thumb_angle1 = start_angles['thumb'][0] + t * (target_angles['thumb'][0] - start_angles['thumb'][0])
        thumb_angle2 = start_angles['thumb'][1] + t * (target_angles['thumb'][1] - start_angles['thumb'][1])
        
        # Apply positions to all fingers
        Move_Index(index_angle1, index_angle2, speed)
        Move_Middle(middle_angle1, middle_angle2, speed)
        Move_Ring(ring_angle1, ring_angle2, speed)
        Move_Thumb(thumb_angle1, thumb_angle2, speed)
        
        # Progress indicator (show every 10 steps or at key milestones)
        if step % 10 == 0 or step == num_steps:
            elapsed = time.time() - start_time
            print(f"  Progress: {int(t_raw * 100)}% | Elapsed: {elapsed:.2f}s | Interpolation: {t:.3f}")
        
        # Wait for next step (compensate for execution time)
        elapsed = time.time() - start_time
        target_time = step * time_step
        if elapsed < target_time:
            time.sleep(target_time - elapsed)
    
    actual_duration = time.time() - start_time
    print(f"Movement complete! Actual duration: {actual_duration:.3f} seconds")


if __name__ == '__main__':
    main()



