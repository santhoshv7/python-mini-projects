
import time

current_time = time.strftime("%H:%M")

print (f"The current time is {current_time}")

alarm_time = input("Enter the alarm time(HH:MM):")

while (time.strftime("%H:%M")!= alarm_time):
    time.sleep(1)

print("Wake up! Alarming")