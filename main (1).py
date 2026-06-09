from machine import Pin
import time
green_led = Pin(4, Pin.OUT, value=0)
yellow_led = Pin(5, Pin.OUT, value=0)
red_led = Pin(2, Pin.OUT, value=0)


button = Pin(15, Pin.IN, Pin.PULL_UP)


emergency_trigger = False
last_interrupt_time = 0


def all_leds_off():
    green_led.value(0)
    yellow_led.value(0)
    red_led.value(0)


def button_handler(pin):
    global emergency_trigger, last_interrupt_time
    current_time = time.ticks_ms()
    
    if time.ticks_diff(current_time, last_interrupt_time) > 200:
        emergency_trigger = True
        last_interrupt_time = current_time

button.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)


def run_state(state_name, led_to_turn_on, duration_seconds):
    global emergency_trigger
    
    all_leds_off()
    led_to_turn_on.value(1)
    print(f"STATE: {state_name}")

    steps = int(duration_seconds * 10)
    for _ in range(steps):
        if emergency_trigger:
            return True
        time.sleep(0.1)
        
    return False

print("Traffic Light System Started...")

while True:

    if emergency_trigger:
        print("STATE: EMERGENCY OVERRIDE")
        emergency_trigger = False 
  
        run_state("GREEN (EMERGENCY)", green_led, 5)
        
       
    if not emergency_trigger:
        run_state("GREEN", green_led, 5)
    
    if not emergency_trigger:
        run_state("YELLOW", yellow_led, 2)
        
 
    if not emergency_trigger:
        run_state("RED", red_led, 5)
