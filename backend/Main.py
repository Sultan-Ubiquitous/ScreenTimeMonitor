import subprocess
import time 
from modules.AppName import get_app_name
from modules.Formater import format_time
from modules.DataBase import postAppData



prev_window = None
start_time = time.time()

while True:
    try:
        result = subprocess.run(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        window_id = result.stdout.strip()
        current_window = get_app_name(window_id)
        
        if current_window != prev_window:
            end_time = time.time()
            duration = end_time - start_time
            
            if prev_window is not None:
                postAppData(prev_window, duration)
                # print(f"Window: {prev_window}, Duration: {format_time(duration)}")
            prev_window = current_window
            start_time = end_time
    
    except Exception as e:
        print(f"An error occurred: {e}")

