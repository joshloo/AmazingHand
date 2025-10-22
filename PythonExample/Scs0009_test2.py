import time
import numpy as np
from rustypot import Scs0009PyController

ID_1 = 4  # Servo ID
MiddlePos_1 = 0  # Middle position in degrees

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
            print(f"Read error: {e}")
        time.sleep(delay)
    return sum(readings) / len(readings) if readings else None

def main():
    c.write_torque_enable(ID_1, 1)  # Enable torque

    try:
        angle = MiddlePos_1
        direction = 1

        while True:
            angle += direction * 20
            if angle > 140 or angle < -140:
                direction *= -1

            pos_rad = np.deg2rad(angle)
            c.write_goal_speed(ID_1, 6)
            c.write_goal_position(ID_1, pos_rad)

            time.sleep(0.0001)  # Allow time for servo to move

            actual_deg = read_average_position(ID_1, samples=5, delay=0.02)
            if actual_deg is not None:
                delta = actual_deg - angle
                # print(f"Target: {angle:.2f}°, Actual: {actual_deg:.2f}°, Δ: {delta:.2f}°")
            else:
                print("Failed to read actual position.")

            time.sleep(0.0001)

    except KeyboardInterrupt:
        c.write_torque_enable(ID_1, 0)
        print("Stopped.")

if __name__ == '__main__':
    main()
