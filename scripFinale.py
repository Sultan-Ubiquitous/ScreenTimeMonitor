import subprocess
import time 

prev_window = ""
start_time = time.perf_counter()

# cmd is the bash command
# In output variable we run the command and capture the output
# In current_window we decode the output from bytes to string and strip any trailing newline characters
while True:
    cmd = 'xprop -id $(xprop -root _NET_ACTIVE_WINDOW | cut -d " " -f 5) WM_NAME | cut -d \'"\' -f 2'
    output = subprocess.check_output(cmd, shell=True)
    current_window = output.decode('utf-8').strip()

    print(current_window)
    subprocess.call(["sleep", "3"])
    # Your code here

    