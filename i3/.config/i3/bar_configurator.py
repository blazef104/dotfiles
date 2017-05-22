#i3bar customization script (c)Blaze, requires - pip install netifaces basiciw colour psutil
from i3pystatus import Status, get_module
import os
import netifaces

status = Status(standalone=True, click_events=True)
@get_module
def ban(self):
    self.output["color"] = "red"
    os.system("xset -dpms & xset s noblank & xset s off")
    #cazzo capire perchè questa merda non funziona
status.register("text", text= "", color= "white")
status.register("text", text= "", on_rightclick=ban)

def sp():
    os.system("shutdown now")
status.register("text", text= "", color= "red", on_rightclick=sp)

def rb():
    os.system("reboot")
status.register("text", text= "", color= "red", on_rightclick=rb)

# Date and time
#info about formatting time and date with man strftime

status.register("clock", format = " %a %-d %b %T")

# Shows your CPU temperature, if you have a Intel CPU
status.register("temp", format="{temp:.0f}°C")

# The battery monitor has many formatting options, see README for details
# This would also display a desktop notification (via D-Bus) if the percentage
# goes below 5 percent while discharging. The block will also color RED.
# If you don't have a desktop notification demon yet, take a look at dunst:
#   http://www.knopwob.org/dunst/
@get_module
def bt(module):
    if module.format == "{bar_design}":
        module.format = "{status} {consumption:.2f}W"

    elif module.format == "{status} {consumption:.2f}W":
        module.format = "{status} {remaining:%E%hh:%Mm}"

    elif module.format == "{status} {remaining:%E%hh:%Mm}":
        module.format = "{status} {percentage:.2f}%"

    else:
        module.format = "{bar_design}"

status.register("battery", format="{bar_design}", alert=True, on_rightclick=bt, alert_percentage=15,
    status={
        "DIS": "↓",
        "CHR": "⚡",
        "FULL": "",
    })

#Show the status of active interfaces
#i want to see only the iterfaces that are connected so: NOTE this is very machine specific,
#i have to implement a way to discover the active connection on an iface

#helper
def is_interface_up(interface):
    addr = netifaces.ifaddresses(interface)
    return netifaces.AF_INET in addr
@get_module
def ip(module):
    if module.format_up == "{v4}":
        module.format_up = "{essid}"
    else:
        module.format_up = "{v4}"

lo = set("lo")
wifi = set("wlp3s0")
eth = set("enp2s0") #check
for i in netifaces.interfaces() :
    if is_interface_up(i):
        set1 = set(i)
        if set1 != lo :
            if set1 == wifi :
                status.register("network", interface= i , format_up= "{essid}" , on_leftclick = ["nm-connection-editor"] , on_rightclick = ip)
            elif set1 == eth :
                status.register("network", interface= i , format_up="{v4}")

# Shows disk usage of /
@get_module
def pt(module):
    if module.path == "/":
        module.path = "/home"
        module.format = " {avail}Gb"
    else:
        module.path = "/"
        module.format = " {avail}Gb"
status.register("disk", path="/", format=" {avail}Gb", on_rightclick=pt )

# Shows pulseaudio default sink volume
status.register("pulseaudio", format="♪ {volume}")


status.run()
