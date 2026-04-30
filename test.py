import sys
import uselect
from machine import Pin, PWM
import time

# --- 1. Motor Setup ---
stby = Pin(22, Pin.OUT)
stby.value(1) # Enable driver

pwma = PWM(Pin(18))
pwma.freq(1000)
ain1 = Pin(20, Pin.OUT)
ain2 = Pin(19, Pin.OUT)

pwmb = PWM(Pin(27))
pwmb.freq(1000)
bin1 = Pin(24, Pin.OUT)
bin2 = Pin(25, Pin.OUT)

# Default speed (0 to 65535). 40000 is about 60% speed.
SPEED = 40000 

# --- 2. Movement Functions ---
def move_forward():
    ain1.value(1); ain2.value(0); pwma.duty_u16(SPEED)
    bin1.value(1); bin2.value(0); pwmb.duty_u16(SPEED)
    print("Moving: FORWARD")

def move_backward():
    ain1.value(0); ain2.value(1); pwma.duty_u16(SPEED)
    bin1.value(0); bin2.value(1); pwmb.duty_u16(SPEED)
    print("Moving: BACKWARD")

def turn_left():
    # Motor A backwards, Motor B forwards (Tank turn)
    ain1.value(0); ain2.value(1); pwma.duty_u16(SPEED)
    bin1.value(1); bin2.value(0); pwmb.duty_u16(SPEED)
    print("Turning: LEFT")

def turn_right():
    # Motor A forwards, Motor B backwards
    ain1.value(1); ain2.value(0); pwma.duty_u16(SPEED)
    bin1.value(0); bin2.value(1); pwmb.duty_u16(SPEED)
    print("Turning: RIGHT")

def stop_motors():
    ain1.value(0); ain2.value(0); pwma.duty_u16(0)
    bin1.value(0); bin2.value(0); pwmb.duty_u16(0)
    print("Motors: STOPPED")

# --- 3. Keyboard Input Setup ---
# We use 'uselect' to read keystrokes instantly without needing to press "Enter"
poll_obj = uselect.poll()
poll_obj.register(sys.stdin, uselect.POLLIN)

print("\n" + "="*30)
print("🚀 LIVE DEMO MODE ACTIVE 🚀")
print("="*30)
print("IMPORTANT: Click your mouse inside this Shell/Console window first!")
print("Controls:")
print("  [W] = Forward")
print("  [S] = Backward")
print("  [A] = Turn Left")
print("  [D] = Turn Right")
print("  [Space] = Stop")
print("  [Q] = Quit Demo")
print("Waiting for input...\n")

try:
    while True:
        # Check if a key was pressed
        poll_results = poll_obj.poll(10) # check every 10ms
        
        if poll_results:
            # Read exactly one character
            char = sys.stdin.read(1).lower()
            
            if char == 'w':
                print("going forward")
                move_forward()
            elif char == 's':
                move_backward()
            elif char == 'a':
                turn_left()
            elif char == 'd':
                turn_right()
            elif char == ' ':
                stop_motors()
            elif char == 'q':
                print("\nExiting demo...")
                break # Break the loop and finish

except KeyboardInterrupt:
    print("\nDemo interrupted.")

finally:
    # Always shut down safely when exiting
    stop_motors()
    stby.value(0)
    print("Power off. Safe to disconnect.")