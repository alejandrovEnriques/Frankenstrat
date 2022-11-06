import importlib
from maya import cmds
from Frankenstrat import constants
from Frankenstrat.nodes import transform

importlib.reload(constants)


class Control(transform.Transform):

    def __init__(self, name, parent=None):
        super(Control, self).__init__(name, parent)
        self._offset = transform.Transform(self._name.replace(constants.CONTROL, constants.GROUP), parent=parent)
        self.parent = self._offset

    def create(self):
        self._offset.create()
        super(Control, self).create()

        self.set_shape("circle")

    def delete(self):
        super(Control, self).delete()
        self._offset.delete()

    def set_shape(self, value):
        if value == "circle":
            shape_transform = cmds.circle()[0]
            print("GETTHIS" + shape_transform)
            shape = cmds.listRelatives(shape_transform, c=True, s=True)[0]
            print(shape)

        cmds.parent(shape, self.name, s=True, r=True)
        cmds.delete(shape_transform)

    @property
    def offset(self):
        return self._offset
