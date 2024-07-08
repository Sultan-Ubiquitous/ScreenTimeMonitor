#!/bin/bash

prev_window=""
start_time=$(date +%s)

while true; do
    current_window=$(xprop -id $(xprop -root _NET_ACTIVE_WINDOW | cut -d ' ' -f 5) WM_NAME | cut -d '"' -f 2)

    if [ "$current_window" != "$prev_window" ]; then
        end_time=$(date +%s)
        duration=$((end_time - start_time))

        if [ -n "$prev_window" ]; then
            echo "Window: $prev_window, Duration: $duration seconds"
        fi

        prev_window="$current_window"
        start_time=$end_time
    fi

    sleep 1
done

