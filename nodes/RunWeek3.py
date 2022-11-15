from maya import cmds
import sys
import importlib

new_path = r"C:\Users\Aleja\Documents\maya\scripts\frankenstrat"
if new_path not in sys.path:
    sys.path.append(new_path)

from Frankenstrat.rig_parts import finger
from Frankenstrat.rig_parts import limb
importlib.reload(finger)
importlib.reload(limb)

arm = limb.Limb("Arm", "Lf", None)
arm.create()
arm.setup()

arm.build()

s = finger.Finger("MyFing00", "Lf", None)
s.create()

s.setup()
s.build()

from maya import cmds
from maya import OpenMaya as om


import os
import json
import re
import functools

from maya import cmds as mc, OpenMaya as om


SHAPE_LIBRARY_PATH = r"C:\Users\Aleja\OneDrive\Documentos\maya\scripts\Frankenstrat\controls"
SHELF_NAME = "Custom"
ICON_PATH = "C:/PATH_TO_ICONS"

def validatePath(path=None):
    '''Checks if the file already exists and provides a dialog to overwrite or not'''
    if os.path.isfile(path):
        confirm = mc.confirmDialog(title='Overwrite file?',
                                   message='The file ' + path + ' already exists.Do you want to overwrite it?',
                                   button=['Yes', 'No'],
                                   defaultButton='Yes',
                                   cancelButton='No',
                                   dismissString='No')
        if confirm == "No":
            mc.warning("The file " + path + " was not saved")
            return 0
    return 1



def saveData(path=None,
             data=None):
    '''Saves a dictionary as JSON in a file'''
    if validatePath(path):
        f = open(path, "w")
        f.write(json.dumps(data, sort_keys=1, indent=4, separators=(",", ":")))
        f.close()
        return 1
    return 0
def getKnots(crvShape=None):
    mObj = om.MObject()
    sel = om.MSelectionList()
    sel.add(crvShape)
    sel.getDependNode(0, mObj)

    fnCurve = om.MFnNurbsCurve(mObj)
    tmpKnots = om.MDoubleArray()
    fnCurve.getKnots(tmpKnots)

    return [tmpKnots[i] for i in range(tmpKnots.length())]


def getShape(crv=None):
    '''Returns a dictionary containing all the necessery information for rebuilding the passed in crv.'''
    crvShapes = validateCurve(crv)

    crvShapeList = []

    for crvShape in crvShapes:
        crvShapeDict = {
            "points": [],
            "knots": [],
            "form": mc.getAttr(crvShape + ".form"),
            "degree": mc.getAttr(crvShape + ".degree"),
            "colour": mc.getAttr(crvShape + ".overrideColor")
        }
        points = []

        for i in range(mc.getAttr(crvShape + ".controlPoints", s=1)):
        	points.append(mc.getAttr(crvShape + ".controlPoints[%i]" % i)[0])

        crvShapeDict["points"] = points
        crvShapeDict["knots"] = getKnots(crvShape)

        crvShapeList.append(crvShapeDict)

    return crvShapeList
def saveToLib(crv=None,
              shapeName=None):
    '''Saves the shape data to a shape file in the SHAPE_LIBRARY_PATH directory'''
    crvShape = getShape(crv=crv)
    path = os.path.join(SHAPE_LIBRARY_PATH, re.sub("\s", "", shapeName) + ".json")
    for shapeDict in crvShape:
        shapeDict.pop("colour", None)
    saveData(path, crvShape)

cruve = getShape(cmds.ls(sl=True)[0])
saveToLib(cmds.ls(sl=True)[0], "square")
#saveData(SHAPE_LIBRARY_PATH,cruve)