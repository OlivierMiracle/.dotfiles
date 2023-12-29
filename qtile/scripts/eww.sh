#!/bin/bash

close_eww() {
    eww close profile    &
    eww close system     &
    eww close clock      &
    eww close uptime     &
    eww close music      &
    eww close network    &
    eww close bluetooth  &
    eww close logout     &
    eww close sleep      &
    eww close reboot     &
    eww close poweroff   &
    eww close folders    &
}

open_eww() {
    eww open profile     &
    eww open system      &
    eww open clock       &
    eww open uptime      &
    eww open music       &
    eww open network     &
    eww open bluetooth   &
    eww open logout      &
    eww open sleep       &
    eww open reboot      &
    eww open poweroff    &
    eww open folders     &
}

if [[ "$1" == "--close" ]]; then
    close_eww
elif [[ "$1" == "--open" ]]; then
    open_eww
fi