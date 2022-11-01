from maya import cmds
import sys
import importlib

new_path = r"C:\Users\Aleja\Documents\maya\scripts\frankenstrat"
if new_path not in sys.path:
    sys.path.append(new_path)

from Frankenstrat.nodes import reverse

importlib.reload(reverse)

from Frankenstrat.nodes import multiplydivide
from Frankenstrat.nodes import blendcolors
from Frankenstrat.nodes import remapvalue
from Frankenstrat.nodes import clamp
from Frankenstrat.nodes import transform

importlib.reload(multiplydivide)
importlib.reload(blendcolors)
importlib.reload(remapvalue)
importlib.reload(clamp)
importlib.reload(transform)

print("Test")
myrev = reverse.Reverse("gf")
myrev.create()

myrev2 = reverse.Reverse("vd")
myrev2.create()

myrev.inputX.value = 5

new_bc1 = blendcolors.BlendColors("Brand_New_BlendColors")
new_bc1.create()

# new_bc1.blender.value(0.5)

new_bc1.color1.value = [50, 75, 23]
new_bc1.color2.value = [54, 40, 20]

new_md = multiplydivide.MultiplyDivide("name")
new_md.create()

new_rmv = remapvalue.RemapValue("Brand_New_RemapValue")
new_rmv.create()
new_rmv.inputMax.value = 5

new_clamp = clamp.Clamp("Brand_new_Clamp")
new_clamp.create()
new_clamp.renderPassMode.value = 1
new_clamp.input.value = [40,780, 45]
new_clamp.max.value = [45, 12, 5]
#new_clamp.input.source =new_bc1.color1
aenriques@roartydigital.com

dag1 = transform.Transform("dag1", None)
dag1.create()

dag2 = transform.Transform("dag2", dag1)
dag2.create()

dag3 = transform.Transform("dag3", None)
dag3.create()
dag3.parent = dag2
