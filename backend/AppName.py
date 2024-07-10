import subprocess

def get_friendly_name(class_name):
    # Mapping class names to user-friendly names
    mapping = {
        "Code": "Visual Studio Code",
        "notion-snap": "Notion",
    }
    return mapping.get(class_name, class_name)

def get_app_name(window_id):
    result = subprocess.run(['xprop', '-id', window_id], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    xprop_output = result.stdout
    
    app_name= None
    app_class = None
    
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
                    return(app_name)


