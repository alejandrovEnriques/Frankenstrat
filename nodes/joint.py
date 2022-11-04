import importlib

from maya import cmds

from Frankenstrat.nodes import depend_node
from Frankenstrat.nodes import transform
from Frankenstrat.plugs import double_plug, double3_plug


class Joint(transform.Transform):
    _maya_type = "joint"

    def __init__(self, name, parent=None):
        super(Joint, self).__init__(name, parent)

        self._jointOrientX = double_plug.Double(self._name, "jointOrientX", 0)
        self._jointOrientY = double_plug.Double(self._name, "jointOrientY", 0)
        self._jointOrientZ = double_plug.Double(self._name, "jointOrientZ", 0)
        self._jointOrient = double3_plug.Double3(self.name, "jointOrient",
                                                 [self._jointOrientX, self._jointOrientY, self._jointOrientZ])

        self._rotateOrder = double_plug.Double(self._name, "rotateOrder", 0)

        self._attributes.extend([self._jointOrientX,
                                 self._jointOrientY,
                                 self._jointOrientZ,
                                 self._rotateOrder])

    @property
    def jointOrientX(self):
        return self._jointOrientX

    @property
    def jointOrientY(self):
        return self._jointOrientY

    @property
    def jointOrientZ(self):
        return self._jointOrientZ

    @property
    def rotateOrder(self):
        return self._rotateOrder

    def rot_to_orient(self):
        world_rot = cmds.xform(self._name, q=True, ro=True, ws=True)
        cmds.xform(self._name, ro=[0, 0, 0], ws=False)
        self._jointOrient.value = world_rot

    def orient_to_rot(self):
        world_rot = cmds.xform(self._name, q=True, ro=True, ws=True)
        self._jointOrient.value = [0, 0, 0]
        cmds.xform(self._name, ro=world_rot, ws=True)
