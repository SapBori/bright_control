#!/bin/bash

DISPLAY=:0 xrandr --output HDMI1 --brightness 0.2

current_brightness=$(xrandr --verbose | grep -A5 HDMI1 | grep Brightness | awk '{print $2}')
log_file="/home/barisbrew/bright_log.txt"
echo "$(date '+%Y-%m-%d %H:%M:%S') - Brightness set to: $current_brightness" >> "$log_file"

