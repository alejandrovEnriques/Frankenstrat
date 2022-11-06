from maya import cmds
import sys
import importlib

new_path = r"C:\Users\Aleja\Documents\maya\scripts\frankenstrat"
if new_path not in sys.path:
    sys.path.append(new_path)


from Frankenstrat.rig_parts import finger

importlib.reload(finger)

s = finger.Finger("MyFing00", "Lf", None)
s.create()

s.setup()
s.build()