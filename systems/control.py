import importlib
from maya import cmds
from Frankenstrat import constants
from Frankenstrat.nodes import transform
import os
import json


importlib.reload(constants)


class Control(transform.Transform):
    SHAPE_LIBRARY_PATH = r"C:\Users\Aleja\OneDrive\Documentos\maya"

    def __init__(self, name, parent=None, ctrl_shape="test"):
        """
        :param name: get the name of the control and use constants to make the nomenclature
        :param parent: get the parent of the control
        :param shape: get the string to create the shape of the control
        """
        super(Control, self).__init__(name, parent)
        self._offset = transform.Transform(self._name.replace(constants.CONTROL, constants.GROUP), parent=parent)
        self.parent = self._offset
        self.ctrl_shape = ctrl_shape

    def create(self):
        self._offset.create()
        super(Control, self).create()

        self.set_shape(self.ctrl_shape)

    def delete(self):
        super(Control, self).delete()
        self._offset.delete()

    def set_shape(self, value):
        if value == "test":
            shape_transform = cmds.circle()[0]
            print("newwww: "  + shape_transform)
            #shape = cmds.listRelatives(shape_transform, c=True, s=True)[0]
            #print("new: " + shape)
            shape_crv = self.load_data(r"C:\Users\Aleja\OneDrive\Documentos\maya\scripts\Frankenstrat\controls\circle"
                                       r".json")
            print(shape_crv)
            print(self.name)
            new_shape = self.set_shape_json(shape_transform, shape_crv, self.name)
            print(new_shape)

        elif value == "square":
            shape_transform = cmds.circle()[0]
            print("newwww: "  + shape_transform)
            #shape = cmds.listRelatives(shape_transform, c=True, s=True)[0]
            #print("new: " + shape)
            shape_crv = self.load_data(r"C:\Users\Aleja\OneDrive\Documentos\maya\scripts\Frankenstrat\controls\square"
                                       r".json")
            print(shape_crv)
            print(self.name)
            new_shape = self.set_shape_json(shape_transform, shape_crv, self.name)
            print(new_shape)

        if value == "circle":
            shape_transform = cmds.circle()[0]

            #shape = cmds.listRelatives(shape_transform, c=True, s=True)[0]

        cmds.parent(new_shape, self.name, s=True, r=True)
        cmds.delete(shape_transform)

    @property
    def offset(self):
        return self._offset

    def load_data(self, path=None):
        '''Loads raw JSON data from a file and returns it as a dict'''
        if os.path.isfile(path):
            f = open(path, "r")
            data = json.loads(f.read())
            f.close()
            return data
        else:
            cmds.error("The file {0} doesn't exist".format(path))

    def validate_curve(self, crv=None):

        '''Checks whether the transform we are working with is actually a curve and returns it's shapes'''

        if cmds.nodeType(crv) == "transform" and cmds.nodeType(cmds.listRelatives(crv, c=1, s=1)[0]) == "nurbsCurve":
            crv_shapes = cmds.listRelatives(crv, c=1, s=1)
        elif cmds.nodeType(crv) == "nurbsCurve":
            crv_shapes = cmds.listRelatives(cmds.listRelatives(crv, p=1)[0], c=1, s=1)
        else:
            cmds.error("The object {0} is not a curve".format(crv))
        return crv_shapes

    def set_shape_json(self, crv, crv_shape_list, name):
        '''Creates a new shape on the crv transform, using the properties in the crvShapeDict.'''
        crv_shapes = self.validate_curve(crv)

        old_colour = cmds.getAttr("{0}.overrideColor".format(crv_shapes[0]))
        cmds.delete(crv_shapes)

        for i, crvShapeDict in enumerate(crv_shape_list):
            tmp_crv = cmds.curve(p=crvShapeDict["points"], k=crvShapeDict["knots"], d=crvShapeDict["degree"],
                                 per=bool(crvShapeDict["form"]))
            new_shape = cmds.listRelatives(tmp_crv, s=1)[0]
            cmds.parent(new_shape, crv, r=1, s=1)

            cmds.delete(tmp_crv)
            new_shape = cmds.rename(new_shape, "{0}Shape{1}".format(name, str(i + 1).zfill(2)))

            cmds.setAttr("{0}.overrideEnabled".format(new_shape), 1)

            if "colour" in crvShapeDict.keys():
                self.setColour(new_shape, crvShapeDict["colour"])
            else:
                self.setColour(new_shape, old_colour)
        return new_shape

    def setColour(self, crv, colour):

        """Sets the overrideColor of a curve"""

        if cmds.nodeType(crv) == "transform":
            crv_shapes = cmds.listRelatives(crv)
        else:
            crv_shapes = [crv]
        for crv in crv_shapes:
            cmds.setAttr("{0}.overrideColor".format(crv), colour)


