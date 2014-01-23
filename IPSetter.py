import pifacecad
import subprocess

# Used by the scripts to select the octet for changes
octetselect = 1

#Different octet selection
oct1 = 0
oct2 = 0
oct3 = 0
oct4 = 0

# Setting function to run commands 
def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8')

# Functions to set the octet for editing 
def input0(event):
    global octetselect
    octetselect = 1

def input1(event):
    global octetselect
    octetselect = 2

def input2(event):
    global octetselect
    octetselect = 3

def input3(event):
    global octetselect
    octetselect = 4


# Functions to add or minus 1 from the octet selected
def left(event):
    global octetselect
    if octetselect == 1:
        event.chip.lcd.set_cursor(0, 0)
        global oct1
        oct1 = oct1 - 1
        oct1print = '{0:03}'.format(oct1)
        event.chip.lcd.write(str(oct1print))
        if oct1 < 0:
            oct1 = 255
    elif octetselect == 2:
        event.chip.lcd.set_cursor(4, 0)
        global oct2
        oct2 = oct2 - 1
        oct2print = '{0:03}'.format(oct2)
        event.chip.lcd.write(str(oct2print))
        if oct2 < 0:
            oct2 = 255
    elif octetselect == 3:
        event.chip.lcd.set_cursor(8, 0)
        global oct3
        oct3 = oct3 - 1
        oct3print = '{0:03}'.format(oct3)
        event.chip.lcd.write(str(oct3print))
        if oct3 < 0:
            oct3 = 255
    elif octetselect == 4:
        event.chip.lcd.set_cursor(12, 0)
        global oct4
        oct4 = oct4 - 1
        oct4print = '{0:03}'.format(oct4)
        event.chip.lcd.write(str(oct4print))
        if oct4 < 0:
            oct4 = 255

def right(event):
    global octetselect
    if octetselect == 1:
        event.chip.lcd.set_cursor(0, 0)
        global oct1
        oct1 = oct1 + 1
        oct1print = '{0:03}'.format(oct1)
        event.chip.lcd.write(str(oct1print))
        if oct1 == 255:
            oct1 = 0
    elif octetselect == 2:
        event.chip.lcd.set_cursor(4, 0)
        global oct2
        oct2 = oct2 + 1
        oct2print = '{0:03}'.format(oct2)
        event.chip.lcd.write(str(oct2print))
        if oct2 == 255:
            oct2 = 0
    elif octetselect == 3:
        event.chip.lcd.set_cursor(8, 0)
        global oct3
        oct3 = oct3 + 1
        oct3print = '{0:03}'.format(oct3)
        event.chip.lcd.write(str(oct3print))
        if oct3 == 255:
            oct3 = 0
    elif octetselect == 4:
        event.chip.lcd.set_cursor(12, 0)
        global oct4
        oct4 = oct4 + 1
        oct4print = '{0:03}'.format(oct4)
        event.chip.lcd.write(str(oct4print))
        if oct4 == 255:
            oct4 = 0
    
    
# Function to set the IP address on button press 
def setip(event):
        event.chip.lcd.clear()
        event.chip.lcd.write("IP Address Set")
        global oct1
        global oct2
        global oct3
        global oct4 
        event.chip.lcd.set_cursor(0, 1)
        IPAddress = str(oct1) + "." + str(oct2) + "." + str(oct3) + "." + str(oct4)
        setip = "sudo ifconfig eth0 %s netmask 255.255.255.0 up" % IPAddress
        run_cmd(setip)
        event.chip.lcd.write(IPAddress)

# Function to reset the octets
def reset(event):
        global oct1
        global oct2
        global oct3
        global oct4
        oct1 = 0
        oct2 = 0
        oct3 = 0
        oct4 = 0
        event.chip.lcd.clear()
        event.chip.lcd.write("000.000.000.000")


# Making the piface libarys easier to use
cad = pifacecad.PiFaceCAD()

# Basics for styling
cad.lcd.backlight_on()
cad.lcd.blink_off()
cad.lcd.cursor_off()

# Writes details to screen to be used by changing numbers
cad.lcd.write("000.000.000.000")
listener = pifacecad.SwitchEventListener(chip=cad)

# Setting the inputs for use
listener.register(0, pifacecad.IODIR_FALLING_EDGE, input0)
listener.register(1, pifacecad.IODIR_FALLING_EDGE, input1)
listener.register(2, pifacecad.IODIR_FALLING_EDGE, input2)
listener.register(3, pifacecad.IODIR_FALLING_EDGE, input3)
listener.register(4, pifacecad.IODIR_FALLING_EDGE, setip)
listener.register(5, pifacecad.IODIR_FALLING_EDGE, reset)
listener.register(6, pifacecad.IODIR_FALLING_EDGE, left)
listener.register(7, pifacecad.IODIR_FALLING_EDGE, right)
listener.activate()
