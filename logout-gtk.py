#!/usr/bin/env python3

# sudo dnf install python3-gobject
# python file.py

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import os
import subprocess

def show_keys(eventKey):
    eventType = eventKey.type
    maybeString = eventKey.string
    modifiers = eventKey.state
    len = eventKey.length
    keyval = eventKey.keyval
    isMod = eventKey.is_modifier
    keycode = eventKey.hardware_keycode
    print("key press event:\n")

    return True

def main():
    home = os.path.expanduser("~")
    user = os.getlogin()

    win = Gtk.Window(title="logout-gtk")
    win.set_border_width(10)
    win.set_resizable(False)
    win.set_default_size(750, 225)
    win.set_position(Gtk.WindowPosition.CENTER)
    win.set_decorated(False)

    img1 = Gtk.Image.new_from_file(f"{home}/.local/img/cancel.png")
    img2 = Gtk.Image.new_from_file(f"{home}/.local/img/logout.png")
    img3 = Gtk.Image.new_from_file(f"{home}/.local/img/reboot.png")
    img4 = Gtk.Image.new_from_file(f"{home}/.local/img/shutdown.png")

    label1 = Gtk.Label(label="<b>Cancel</b>")
    label1.set_use_markup(True)
    label2 = Gtk.Label(label="<b>Logout</b>")
    label2.set_use_markup(True)
    label3 = Gtk.Label(label="<b>Reboot</b>")
    label3.set_use_markup(True)
    label4 = Gtk.Label(label="<b>Shutdown</b>")
    label4.set_use_markup(True)

    btn1 = Gtk.Button()
    btn1.set_relief(Gtk.ReliefStyle.NONE)
    btn1.set_image(img1)
    btn1.set_hexpand(False)
    btn1.connect("clicked", lambda w: (print("User choose: Cancel"), win.destroy()))

    btn2 = Gtk.Button()
    btn2.set_relief(Gtk.ReliefStyle.NONE)
    btn2.set_image(img2)
    btn2.set_hexpand(False)
    btn2.connect("clicked", lambda w: (print("User choose: Logout"), subprocess.call(f"pkill -u {user}", shell=True), win.destroy()))

    btn3 = Gtk.Button()
    btn3.set_relief(Gtk.ReliefStyle.NONE)
    btn3.set_image(img3)
    btn3.set_hexpand(False)
    btn3.connect("clicked", lambda w: (print("User choose: Reboot"), subprocess.call("sudo shutdown -r now", shell=True), win.destroy()))

    # Add buttons and labels to a box
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    box.pack_start(label1, False, False, 0)
    box.pack_start(btn1, False, False, 0)
    box.pack_start(label2, False, False, 0)
    box.pack_start(btn2, False, False, 0)
    box.pack_start(label3, False, False, 0)
    box.pack_start(btn3, False, False, 0)

    # Add the box to the window
    win.add(box)

    # Show all widgets and start main loop
    win.show_all()
    print("Gtk main started")
    Gtk.main()
    print("Gtk main ended")

if __name__ == '__main__':
    main()
