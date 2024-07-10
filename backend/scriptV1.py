import subprocess
import time

def get_friendly_name(class_name):
    # Mapping class names to user-friendly names
    mapping = {
        "Code": "Visual Studio Code",
        "notion-snap": "Notion",
    }
    return mapping.get(class_name, class_name)

while True:
    try:
        # Get the window ID of the active window
        result = subprocess.run(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        window_id = result.stdout.strip()

        # Only proceed if window_id is not empty
        if window_id:
            # Get the name of the application that owns the active window
            result = subprocess.run(['xprop', '-id', window_id], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
            xprop_output = result.stdout

            # Initialize variables
            app_name = None
            app_class = None

            # Parse the output for WM_NAME and WM_CLASS
            for line in xprop_output.split('\n'):
                if 'WM_NAME(STRING)' in line:
                    app_name = line.split('"')[1]
                if 'WM_CLASS(STRING)' in line:
                    app_class = line.split('"')[3]
            
            # Fallback to class name if WM_NAME is not found
            if not app_name and app_class:
                app_name = get_friendly_name(app_class)
            
            # Display the name of the application
            if app_name:
                print(app_name)
    except Exception as e:
        print(f"An error occurred: {e}")

    # Sleep for 3 seconds
    time.sleep(2)
