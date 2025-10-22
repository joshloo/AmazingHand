import time
import numpy as np
from rustypot import Scs0009PyController

SERVO_IDS = [4, 5, 6, 7]  # List of servo IDs
MiddlePos = 0  # Middle position in degrees

# Initialize controller
c = Scs0009PyController(
    serial_port="COM60",
    baudrate=1000000,
    timeout=0.5,
)

def read_average_position(servo_id, samples=5, delay=0.05):
    """Read the present position multiple times and return the average in degrees."""
    readings = []
    for _ in range(samples):
        try:
            pos_rad = c.read_present_position(servo_id)
            pos_deg = float(np.rad2deg(pos_rad))
            readings.append(pos_deg)
        except Exception as e:
            print(f"Read error on ID {servo_id}: {e}")
        time.sleep(delay)
    return sum(readings) / len(readings) if readings else None

def main():
    # Enable torque for all servos
    for servo_id in SERVO_IDS:
        c.write_torque_enable(servo_id, 1)

    try:
        angle = MiddlePos
        direction = 1

        while True:
            angle += direction * 20
            if angle > 140 or angle < -140:
                direction *= -1

            pos_rad = np.deg2rad(angle)

            for servo_id in SERVO_IDS:
                c.write_goal_speed(servo_id, 6)
                c.write_goal_position(servo_id, pos_rad)

            time.sleep(0.0001)  # Allow time for servos to move

            for servo_id in SERVO_IDS:
                actual_deg = read_average_position(servo_id, samples=5, delay=0.02)
                if actual_deg is not None:
                    delta = actual_deg - angle
                    print(f"ID {servo_id} → Target: {angle:.2f}°, Actual: {actual_deg:.2f}°, Δ: {delta:.2f}°")
                else:
                    print(f"Failed to read actual position for ID {servo_id}.")

            time.sleep(0.0001)

    except KeyboardInterrupt:
        for servo_id in SERVO_IDS:
            # reset to position degree 0
            pos_rad = np.deg2rad(0)
            c.write_goal_speed(servo_id, 6)
            c.write_goal_position(servo_id, pos_rad)
            time.sleep(0.0001)  # Allow time for servos to move
            #c.write_torque_enable(servo_id, 0)
            #print(servo_id)
        print("Stopped.")

if __name__ == '__main__':
    main()
