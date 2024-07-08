#!/bin/bash

# Initialize variables
last_window=""
start_time=0

# Infinite loop
while true; do
    # Get the ID of the current main window
    window_id=$(xprop -root _NET_ACTIVE_WINDOW | awk '{print $5}' | tr -d '\n')

    # Get the name of the current main window
    current_window=$(wmctrl -l -p | grep " $window_id " | awk '{print $5}')

    # If the window has changed
    if [[ "$current_window" != "$last_window" ]]; then
        # If this is not the first iteration
        if [[ "$last_window" != "" ]]; then
            # Calculate the duration
            end_time=$(date +%s)
            duration=$((end_time - start_time))

            # Print the result
            echo "Application: $last_window, Duration: $duration seconds"
        fi

        # Update the last window and start time
        last_window="$current_window"
        start_time=$(date +%s)
    fi

    # Sleep for a short period to reduce CPU usage
    sleep 1
done

