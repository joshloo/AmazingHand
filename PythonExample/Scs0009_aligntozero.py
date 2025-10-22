import time
import numpy as np
from rustypot import Scs0009PyController

ID_1 = 1  # Servo ID
TARGET_DEGREE = 0
serial_port = "COM60"
baudrate = 1000000
timeout = 0.5

# Initialize controller
c = Scs0009PyController(
    serial_port=serial_port,
    baudrate=baudrate,
    timeout=timeout,
)

def read_position_deg(servo_id):
    """Read the current position in degrees."""
    try:
        pos_rad = c.read_present_position(servo_id)
        return float(np.rad2deg(pos_rad))
    except Exception as e:
        print(f"Read error: {e}")
        return None

def main():
    c.write_torque_enable(ID_1, 1)  # Enable torque

    # Set desired angle
    target_deg = TARGET_DEGREE
    target_rad = np.deg2rad(target_deg)

    # Set speed and position
    c.write_goal_speed(ID_1, 6)
    c.write_goal_position(ID_1, target_rad)

    # Wait long enough for servo to reach position
    time.sleep(1.0)  # Adjust based on speed and distance

    # Read back actual position
    actual_deg = read_position_deg(ID_1)
    if actual_deg is not None:
        delta = actual_deg - target_deg
        print(f"Target: {target_deg:.2f}°, Actual: {actual_deg:.2f}°, Δ: {delta:.2f}°")
    else:
        print("Failed to read actual position.")

    c.write_torque_enable(ID_1, 0)  # Disable torque

if __name__ == '__main__':
    main()
