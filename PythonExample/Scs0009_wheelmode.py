import time
from rustypot import Scs0009PyController

ID_1 = 1  # Your servo ID
serial_port = "COM60"
baudrate = 1000000
timeout = 0.5

# Initialize controller
c = Scs0009PyController(
    serial_port=serial_port,
    baudrate=baudrate,
    timeout=timeout,
)

def set_wheel_mode(servo_id):
    """Set the servo to wheel (continuous rotation) mode using API."""
    try:
        print("Disabling torque...")
        c.write_torque_enable(servo_id, 0)

        print("Setting mode to wheel (continuous rotation)...")
        c.write_mode(servo_id, 1)  # 1 = Wheel Mode

        print("Re-enabling torque...")
        c.write_torque_enable(servo_id, 1)

        print("Wheel mode set successfully.")
    except Exception as e:
        print(f"Failed to set wheel mode: {e}")

def run_wheel_mode(servo_id):
    """Run the servo in both directions."""
    try:
        print("Running clockwise at speed 6...")
        c.write_goal_speed(servo_id, 6)
        time.sleep(2)

        print("Stopping...")
        c.write_goal_speed(servo_id, 0)
        time.sleep(1)

        print("Running counter-clockwise at speed -6...")
        c.write_goal_speed(servo_id, -6)
        time.sleep(2)

        print("Stopping...")
        c.write_goal_speed(servo_id, 0)
    except Exception as e:
        print(f"Error during wheel mode run: {e}")

def main():
    set_wheel_mode(ID_1)
    run_wheel_mode(ID_1)

if __name__ == '__main__':
    main()
