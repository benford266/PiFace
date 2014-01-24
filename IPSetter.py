import pifacecad
import subprocess

# Used by the scripts to select the octet for changes
octetselect = 1

#Different octet selection
oct1 = 0
oct2 = 0
oct3 = 0
oct4 = 0

#Used to set screen
screen = 0

# Used to choose program
program = 0

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

# Used to re-edit the IP address
def updatescreenip(event):
    global screen
    if screen == 1:
        global oct1
        global oct2
        global oct3
        global oct4
        event.chip.lcd.clear()
        oct1print = '{0:03}'.format(oct1)
        oct2print = '{0:03}'.format(oct2)
        oct3print = '{0:03}'.format(oct3)
        oct4print = '{0:03}'.format(oct4)
        stringprint = str(oct1print) + "." + str(oct2print) + "." + str(oct3print) + "." + str(oct4print)
        event.chip.lcd.write(stringprint)
        screen = 0

# USed to set ip address
def setip(event):
        global screen 
        screen = 1
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

# Functions to add or minus 1 from the octet selected
def left(event):
    updatescreenip(event)
    global octetselect
    if octetselect == 1:
        event.chip.lcd.set_cursor(0, 0)
        global oct1
        oct1 = oct1 - 1
        if oct1 < 1:
            oct1 = 255
        oct1print = '{0:03}'.format(oct1)
        event.chip.lcd.write(str(oct1print))
    elif octetselect == 2:
        event.chip.lcd.set_cursor(4, 0)
        global oct2
        oct2 = oct2 - 1
        if oct2 < 1:
            oct2 = 255
        oct2print = '{0:03}'.format(oct2)
        event.chip.lcd.write(str(oct2print))
    elif octetselect == 3:
        event.chip.lcd.set_cursor(8, 0)
        global oct3
        oct3 = oct3 - 1
        if oct3 < 1:
            oct3 = 255
        oct3print = '{0:03}'.format(oct3)
        event.chip.lcd.write(str(oct3print))
    elif octetselect == 4:
        event.chip.lcd.set_cursor(12, 0)
        global oct4
        oct4 = oct4 - 1
        if oct4 < 1:
            oct4 = 255
        oct4print = '{0:03}'.format(oct4)
        event.chip.lcd.write(str(oct4print))

def right(event):
    updatescreenip(event)
    global octetselect
    if octetselect == 1:
        event.chip.lcd.set_cursor(0, 0)
        global oct1
        oct1 = oct1 + 1
        if oct1 > 255:
            oct1 = 0
        oct1print = '{0:03}'.format(oct1)
        event.chip.lcd.write(str(oct1print))
    elif octetselect == 2:
        event.chip.lcd.set_cursor(4, 0)
        global oct2
        oct2 = oct2 + 1
        if oct2 > 255:
            oct2 = 0
        oct2print = '{0:03}'.format(oct2)
        event.chip.lcd.write(str(oct2print))
    elif octetselect == 3:
        event.chip.lcd.set_cursor(8, 0)
        global oct3
        oct3 = oct3 + 1
        if oct3 > 255:
            oct3 = 0
        oct3print = '{0:03}'.format(oct3)
        event.chip.lcd.write(str(oct3print))
    elif octetselect == 4:
        event.chip.lcd.set_cursor(12, 0)
        global oct4
        oct4 = oct4 + 1
        if oct4 > 255:
            oct4 = 0
        oct4print = '{0:03}'.format(oct4)
        event.chip.lcd.write(str(oct4print))
    
    
# Function to ping the IP address on button press 
def ping(event):
        global screen 
        screen = 1
        global oct1
        global oct2
        global oct3
        global oct4
        event.chip.lcd.clear()
        event.chip.lcd.write("Host:")
        event.chip.lcd.set_cursor(6, 1)
        IPAddress = str(oct1) + "." + str(oct2) + "." + str(oct3) + "." + str(oct4)
        event.chip.lcd.clear()
        event.chip.lcd.write("Ping: %s\nHost:" % IPAddress)
        event.chip.lcd.set_cursor(6, 1)
        ping = subprocess.call(['ping', '-c', '1', IPAddress])
        if ping == 0:
            event.chip.lcd.write("UP!")
        elif ping == 2:
            event.chip.lcd.write("Unreachable")
        else:
            event.chip.lcd.write("Down!")

# Function to reset the octets
def reset(event):
        global oct1
        global oct2
        global oct3
        global oct4
        global screen
        screen = 0
        oct1 = 0
        oct2 = 0
        oct3 = 0
        oct4 = 0
        event.chip.lcd.clear()
        event.chip.lcd.write("000.000.000.000")

def ipsetprogram(event):
    global program
    event.chip.lcd.clear()
    event.chip.lcd.write("IP Setter \n Press 4")
    program = 1

def pingprogram(event):
    global program
    event.chip.lcd.clear()
    event.chip.lcd.write("Pinger \n Press 4")
    program = 2

def chooseprogram(event):
    global program
    global listenermenu
    global listenerping
    global listenersetip
    if program == 0:
        event.chip.lcd.clear()
        event.chip.lcd.write("Please select \n program")
    elif program == 1:
        event.chip.lcd.clear()
        event.chip.lcd.write("000.000.000.000")
        listenersetip.activate()
        listenermenu.deactivate()
    elif program == 2:
        event.chip.lcd.clear()
        cad.lcd.write("000.000.000.000")
        listenerping.activate()
        listenermenu.deactivate()




# Making the piface libarys easier to use
cad = pifacecad.PiFaceCAD()

# Basics for styling
cad.lcd.backlight_on()
cad.lcd.blink_off()
cad.lcd.cursor_off()

# Writes details to screen to be used by changing numbers
cad.lcd.write("Please Select \n program")

#Listeners

listenermenu = pifacecad.SwitchEventListener(chip=cad)
listenermenu.register(0, pifacecad.IODIR_FALLING_EDGE, ipsetprogram)
listenermenu.register(1, pifacecad.IODIR_FALLING_EDGE, pingprogram)
listenermenu.register(4, pifacecad.IODIR_FALLING_EDGE, chooseprogram)
listenermenu.activate()


listenerping = pifacecad.SwitchEventListener(chip=cad)
listenerping.register(0, pifacecad.IODIR_FALLING_EDGE, input0)
listenerping.register(1, pifacecad.IODIR_FALLING_EDGE, input1)
listenerping.register(2, pifacecad.IODIR_FALLING_EDGE, input2)
listenerping.register(3, pifacecad.IODIR_FALLING_EDGE, input3)
listenerping.register(4, pifacecad.IODIR_FALLING_EDGE, ping)
listenerping.register(5, pifacecad.IODIR_FALLING_EDGE, reset)
listenerping.register(6, pifacecad.IODIR_FALLING_EDGE, left)
listenerping.register(7, pifacecad.IODIR_FALLING_EDGE, right)


listenersetip = pifacecad.SwitchEventListener(chip=cad)
listenersetip.register(0, pifacecad.IODIR_FALLING_EDGE, input0)
listenersetip.register(1, pifacecad.IODIR_FALLING_EDGE, input1)
listenersetip.register(2, pifacecad.IODIR_FALLING_EDGE, input2)
listenersetip.register(3, pifacecad.IODIR_FALLING_EDGE, input3)
listenersetip.register(4, pifacecad.IODIR_FALLING_EDGE, setip)
listenersetip.register(5, pifacecad.IODIR_FALLING_EDGE, reset)
listenersetip.register(6, pifacecad.IODIR_FALLING_EDGE, left)
listenersetip.register(7, pifacecad.IODIR_FALLING_EDGE, right)
