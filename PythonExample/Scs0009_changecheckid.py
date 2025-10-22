import time
from rustypot import Scs0009PyController

# Setup controller
c = Scs0009PyController(
    serial_port="COM60",
    baudrate=1000000,
    timeout=0.5,
)

def scan_servos(id_range=range(1, 20)):
    """Scan for connected servos by reading position instead of pinging."""
    active_ids = []
    print("Scanning for active servo IDs...")
    for servo_id in id_range:
        try:
            pos_rad = c.read_present_position(servo_id)
            if pos_rad is not None:
                print(f"✅ Confirmed servo at ID {servo_id}")
                active_ids.append(servo_id)
        except Exception:
            pass  # No valid response
        time.sleep(0.05)
    if not active_ids:
        print("⚠️ No servos found.")
    return active_ids

def change_servo_id(old_id, new_id):
    """Change the ID of a servo."""
    try:
        print(f"Changing ID from {old_id} to {new_id}...")
        c.write_id(old_id, new_id)
        time.sleep(0.5)
        print(f"✅ ID changed successfully.")
    except Exception as e:
        print(f"❌ Failed to change ID: {e}")

def main():
    active_ids = scan_servos()

    if active_ids:
        try:
            old_id = int(input("Enter the current ID of the servo to change: "))
            new_id = int(input("Enter the new ID you want to assign: "))
            if old_id in active_ids:
                change_servo_id(old_id, new_id)
            else:
                print(f"ID {old_id} not found in scanned devices.")
        except ValueError:
            print("⚠️ Invalid input. Please enter numeric IDs.")

if __name__ == '__main__':
    main()
