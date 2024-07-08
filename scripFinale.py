import subprocess
import time 

def format_time(duration):

  if duration < 60:
    unit = "seconds"
  elif duration < 3600:
    duration /= 60  # Convert to minutes
    unit = "minutes"
  else:
    duration /= 3600  # Convert to hours
    unit = "hours"

  formatted_time = f"{duration:.2f}"

  return f"{formatted_time} {unit}"


prev_window = None
start_time = time.time()

# cmd is the bash command
# In output variable we run the command and capture the output
# In current_window we decode the output from bytes to string and strip any trailing newline characters
while True:
    cmd = 'xprop -id $(xprop -root _NET_ACTIVE_WINDOW | cut -d " " -f 5) WM_NAME | cut -d \'"\' -f 2'
    output = subprocess.check_output(cmd, shell=True)
    current_window = output.decode('utf-8').strip()
    
    if current_window != prev_window:
        end_time = time.time()
        duration = format_time(end_time - start_time)
        
        if prev_window is not None:
            print(f"Window: {prev_window}, Duration: {duration}")
        prev_window = current_window
        start_time = end_time
        
    subprocess.call(["sleep", "1"])
    

    