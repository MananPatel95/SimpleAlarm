# A Simple Alarm clock for a practise project

import datetime
import time
import random
import os


def set_time():
    print("    What time would you like to set your alarm?:")
    hour = int(input("       HOUR (1-24):"))
    minute = int(input("       MINUTE (0-59):"))
    while hour not in range(1, 25) or minute not in range(0, 60):
        print("    The hour or minute format is wrong. Try again:")
        hour = int(input("        HOUR (1-24):"))
        minute = int(input("        MINUTE (0-59):"))
    else:
        print("    Your time was successfully set !")
        return [hour, minute]


def get_time():
    now = datetime.datetime.now()
    return [int(now.hour), int(now.minute)]


def display(trigger):
    print("    Alarm set for %s:%s" % (trigger[0], trigger[1]))
    print("    Time remaining :")
    hour = 1
    minute = 1
    blink = 1
    while hour != 0 or minute != 0:
        minute_trig = trigger[0] * 60 + trigger[1]
        minute_now = get_time()[0] * 60 + get_time()[1]
        if minute_now > minute_trig:
            minute_remain = (24 * 60) - (minute_now - minute_trig)
        else:
            minute_remain = minute_trig - minute_now
        minute = int(minute_remain % 60)
        hour = int((minute_remain - minute) / 60)
        if hour == 1:
            h = "hour"
        else:
            h = "hours"
        if minute == 1:
            m = "minute"
        else:
            m = "minutes"
        if blink == 1:
            dots = "."
            blink = 2
        elif blink == 2:
            dots = ".."
            blink = 3
        else:
            dots = "..."
            blink = 1
        print("\r    %s %s %s %s %s" % (str(hour), h, str(minute), m, dots), end=" ")
        time.sleep(1)
    else:
        print("\r")


def execute():
    data = open("playlist.txt", "r")
    collect = []
    for line in data:
        if len(line) != 0:
            collect.append(str(line))
    data.close()
    return collect

display(set_time())
os.system("start %s" % execute()[random.randint(0, len(execute()) - 1)])