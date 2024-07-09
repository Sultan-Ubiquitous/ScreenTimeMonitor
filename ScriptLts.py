import subprocess
import time 
from AppName import get_app_name
from Formater import format_time



prev_window = None
start_time = time.time()

while True:
    try:
        result = subprocess.run(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        window_id = result.stdout.strip()
        current_window = get_app_name(window_id)
        
        if current_window != prev_window:
            end_time = time.time()
            duration = format_time(end_time - start_time)
            
            if prev_window is not None:
                print(f"Window: {prev_window}, Duration: {duration}")
            prev_window = current_window
            start_time = end_time
        
        time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {e}")