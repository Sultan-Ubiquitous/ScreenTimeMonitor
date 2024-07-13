import subprocess
import time 
from modules.AppName import get_app_name
from modules.Formater import format_time
from modules.DataBase import postAppData
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib


#this ain't wokring but gave me an lead to follow.
# I know an doesn't go infront of lead but I do not care and it sounds cool.

DBusGMainLoop(set_as_default=True)


prev_window = None
start_time = time.time()
paused = False


def on_screen_changed(message):
    global paused
    if isinstance(message, dbus.Boolean):
        active = message
    else:
        active = message.get_args()[0]
    if active:
        paused = False
        print("Screen unlocked, Resuming the script")
    else:
        paused = True
        print("Screen locked, Pausing the script")
    print("active:", active)

            
bus = dbus.SessionBus()
bus.add_signal_receiver(on_screen_changed,
                        dbus_interface='org.gnome.ScreenSaver',
                        signal_name='ActiveChanged')



while True:
    
    if not paused:        
        
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
    
    GLib.MainContext.default().iteration(True)