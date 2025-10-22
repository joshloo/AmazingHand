import time
import numpy as np
from rustypot import Scs0009PyController

ID_1 = 1  # Change to your servo's actual ID
serial_port = "COM60"
baudrate = 1000000
timeout = 0.5

# Initialize controller
c = Scs0009PyController(
    serial_port=serial_port,
    baudrate=baudrate,
    timeout=timeout,
)

def deg_to_raw(deg):
    """Convert degrees to raw position (0–1023 for 0°–300°)."""
    return int((deg / 300.0) * 1023)

def read_position_deg(servo_id):
    """Read the current position in degrees."""
    try:
        pos_rad = c.read_present_position(servo_id)
        return float(np.rad2deg(pos_rad))
    except Exception as e:
        print(f"Read error: {e}")
        return None

def set_angle_limits(servo_id):
    """Attempt to set min/max angle limits safely."""
    try:
        print("Disabling torque to set angle limits...")
        c.write_torque_enable(servo_id, 0)

        print("Setting min angle limit to 0...")
        c.write_raw_min_angle_limit(servo_id, 0)

        print("Setting max angle limit to 1023 (300°)...")
        c.write_raw_max_angle_limit(servo_id, 1023)

        print("Re-enabling torque...")
        c.write_torque_enable(servo_id, 1)

        print("Angle limits set successfully.")
    except Exception as e:
        print(f"Failed to set angle limits: {e}")
        print("Continuing with default limits...")

def main():
    mode = c.read_mode(ID_1)
    print(f"Servo mode: {mode}")

    # set_angle_limits(ID_1)

    print("Sweeping servo from 0° to 300° in 30° steps...")
    for target_deg in range(0, 301, 30):
        raw_pos = deg_to_raw(target_deg)
        c.write_goal_speed(ID_1, 6)
        c.write_raw_goal_position(ID_1, raw_pos)

        time.sleep(1.5)

        actual_deg = read_position_deg(ID_1)
        if actual_deg is not None:
            delta = actual_deg - target_deg
            print(f"Target: {target_deg:.1f}°, Actual: {actual_deg:.1f}°, Δ: {delta:.1f}°")
        else:
            print("Failed to read actual position.")

    c.write_torque_enable(ID_1, 0)
    print("Sweep complete.")

if __name__ == '__main__':
    main()
