import importlib
from maya import cmds

from Frankenstrat.nodes import depend_node
from Frankenstrat.plugs import double_plug, double3_plug, bool_plug


class Transform(depend_node.DependNode):
    _maya_type = "transform"

    def __init__(self, name, parent=None):
        super(Transform, self).__init__(name)

        self._parent = parent

        self._translateX = double_plug.Double(self._name, "translateX", 0)
        self._translateY = double_plug.Double(self._name, "translateY", 0)
        self._translateZ = double_plug.Double(self._name, "translateZ", 0)
        self._translate = double3_plug.Double3(self.name, "translate",
                                               [self._translateX, self._translateY, self._translateZ])

        self._rotateX = double_plug.Double(self._name, "rotateX", 0)
        self._rotateY = double_plug.Double(self._name, "rotateY", 0)
        self._rotateZ = double_plug.Double(self._name, "rotateZ", 0)
        self._rotate = double3_plug.Double3(self.name, "rotate",
                                            [self._rotateX, self._rotateY, self._rotateZ])

        self._scaleX = double_plug.Double(self._name, "scaleX", 1)
        self._scaleY = double_plug.Double(self._name, "scaleY", 1)
        self._scaleZ = double_plug.Double(self._name, "scaleZ", 1)
        self._scale = double3_plug.Double3(self.name, "scale",
                                           [self._scaleX, self._scaleY, self._scaleZ])

        self._visibility = double_plug.Double(self._name, "visibility", 1)
        self._inheritsTransform = bool_plug.Bool(self.name, "inheritsTransform", True)
        self._displayLocalAxis = bool_plug.Bool(self.name, "displayLocalAxis", False)
        

        self._attributes = [self._translateX,
                            self._translateY,
                            self._translateZ,
                            self._rotateX,
                            self._rotateY,
                            self._rotateZ,
                            self._scaleX,
                            self._scaleY,
                            self._scaleZ,
                            self._visibility,
                            self._inheritsTransform,
                            self._displayLocalAxis]

    @property
    def parent(self):
        if cmds.objExists(self._name):
            parent = cmds.listRelatives(self._name, p=True)
            if parent and parent[0] != self._parent:
                self._parent = parent[0]
        return self._parent

    @parent.setter
    def parent(self, value):
        if cmds.objExists(self._name):
            parent = cmds.listRelatives(self._name, p=True)
            if not value and parent:
                cmds.parent(self._name, w=True)
            elif not value:
                pass
            elif cmds.objExists(self._name) and cmds.objExists(value.name):
                if parent and parent[0] != self._parent:
                    self._parent = parent[0]
                if value != parent:
                    cmds.parent(self._name, value.name)
        self._parent = value

    def create(self):
        super(Transform, self).create()
        self.parent = self._parent

    @property
    def translate(self):
        return self._translate

    @property
    def translateX(self):
        return self._translateX

    @property
    def translateY(self):
        return self._translateY

    @property
    def translateZ(self):
        return self._translateZ

    @property
    def rotate(self):
        return self._rotate

    @property
    def rotateX(self):
        return self._rotateX

    @property
    def rotateY(self):
        return self._rotateY

    @property
    def rotateZ(self):
        return self._rotateZ

    @property
    def scale(self):
        return self._scale

    @property
    def scaleX(self):
        return self._scaleX

    @property
    def scaleY(self):
        return self._scaleY

    @property
    def scaleZ(self):
        return self._scaleZ

    @property
    def visibility(self):
        return self._visibility

    @property
    def inheritsTransform(self):
        return self._inheritsTransform

    @property
    def displayLocalAxis(self):
        return self._displayLocalAxis

    def snap_to(self, target):
        matrix = cmds.xform(target.name, q=True, m=True, ws=True)
        cmds.xform(self._name, m=matrix, ws=True)
