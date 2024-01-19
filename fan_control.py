import os
import gpiod
import time
from simple_pid import PID

# Constants
CHIP_NAME = 'gpiochip0'
LINE_NUMBER = 211
TARGET_TEMP = 50.0  # Target CPU temperature in Celsius
UPDATE_INTERVAL = 5  # Interval to update fan speed in seconds

# Initialize PID controller
pid = PID(1.0, 0.5, 2.0, setpoint=TARGET_TEMP)
pid.output_limits = (0, 1)  # Output value will be between 0 and 1

def get_cpu_temp():
    """Returns the current CPU temperature."""
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
            temp_str = file.read()
            # Convert the temperature to Celsius
            return float(temp_str) / 1000
    except Exception as e:
        print(f"Error reading temperature: {e}")
        return 0  # Return a safe value in case of error


def control_fan(chip_name, line_number, speed):
    """Controls the fan speed."""
    with gpiod.Chip(chip_name) as chip:
        line = chip.get_line(line_number)
        line.request(consumer='fan_control', type=gpiod.LINE_REQ_DIR_OUT)
        line.set_value(int(speed))

try:
    while True:
        temp = get_cpu_temp()
        control = pid(temp)
        control_fan(CHIP_NAME, LINE_NUMBER, control)
        
        time.sleep(UPDATE_INTERVAL)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    control_fan(CHIP_NAME, LINE_NUMBER, 0)  # Ensure fan is turned off
    print("Fan control script ended.")
