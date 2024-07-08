#!/bin/bash

while true; do
    # Get the window ID of the active window
    WINDOW_ID=$(xdotool getactivewindow)

    # Get the name of the application that owns the active window
    APP_NAME=$(wmctrl -l -p | grep $WINDOW_ID | awk '{print $3}')

    # Display the name of the application
    echo $APP_NAME

    # Sleep for 2 seconds
    sleep 2
done
