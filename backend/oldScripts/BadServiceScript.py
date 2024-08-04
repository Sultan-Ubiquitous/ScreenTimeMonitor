import subprocess
import psycopg2
import time
import signal 



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



host = 'urmumshouse.com'
dbname = 'postgres'
user = 'someUser'
password = 'passwordOfcNotReal'
port = 1234

# Schema:
# CREATE TABLE IF NOT EXISTS screen_time(
#     id SERIAL PRIMARY KEY,
#     app_name VARCHAR(255) NOT NULL,
#     duration INTEGER NOT NULL,
#     timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP


def connect():
    conn = None
    try:
        conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
        return conn
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
        return None
        
        
def postAppData(app_name, duration):
    conn = connect()
    if conn is None:
        return
    
    try:
        cur = conn.cursor()
        cur.execute("""
                    SELECT * FROM screen_time
                    WHERE app_name = %s AND DATE(timestamp) = CURRENT_DATE;
                    """, (app_name,))
        row = cur.fetchone()
        if row:
            cur.execute("""
                        UPDATE screen_time
                        SET duration = duration + %s
                        WHERE id = %s;
                        """, (duration, row[0]))
            
        else:
            cur.execute("""
                        INSERT INTO screen_time (app_name, duration)
                        VALUES(%s, %s) RETURNING id;
                        """, (app_name, duration))
    
        conn.commit()
        
        cur.close()
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            

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

def signal_handler(signum, frame):
    # Handle cleanup when the script is interrupted
    if prev_window is not None:
        end_time = time.time()
        duration = end_time - start_time
        postAppData(prev_window, duration)
    print("Exiting gracefully")
    exit(0)

# Register the signal handler
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

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
                print(f"Window: {prev_window}, Duration: {format_time(duration)}")
            prev_window = current_window
            start_time = end_time
    
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(5)

