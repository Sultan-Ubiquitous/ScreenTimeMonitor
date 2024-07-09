#!/bin/bash

# Function to get the user-friendly name from WM_CLASS
get_friendly_name() {
    case "$1" in
        "Code") echo "Visual Studio Code";;
        
        "notion-snap") echo "Notion";;
        *) echo "$1";;
    esac
}

while true; do
    # Get the window ID of the active window
    WINDOW_ID=$(xdotool getactivewindow 2>/dev/null)

    # Only proceed if WINDOW_ID is not empty
    if [ -n "$WINDOW_ID" ]; then
        # Get the name of the application that owns the active window
        APP_NAME=$(xprop -id $WINDOW_ID 2>/dev/null | grep "WM_NAME(STRING)" | awk -F\" '{print $2}')

        # If WM_NAME is empty, fallback to WM_CLASS
        if [ -z "$APP_NAME" ]; then
            APP_CLASS=$(xprop -id $WINDOW_ID 2>/dev/null | grep "WM_CLASS(STRING)" | awk -F\" '{print $4}')
            APP_NAME=$(get_friendly_name "$APP_CLASS")
        fi

        # Display the name of the application
        echo $APP_NAME
    fi

    # Sleep for 3 seconds
    sleep 3
done
    