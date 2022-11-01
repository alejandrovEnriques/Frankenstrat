import importlib
from maya import cmds

from Frankenstrat.nodes import depend_node
from Frankenstrat.nodes import plugdata
from Frankenstrat.nodes import plugdata3

importlib.reload(depend_node)
importlib.reload(plugdata)
importlib.reload(plugdata3)


class Transform(depend_node.DependNode):
    _maya_type = "transform"

    def __init__(self, name, parent=None):
        super(Transform, self).__init__(name)

        self._parent = parent

        self._translateX = plugdata.PlugData(self._name, "translateX", 0)
        self._translateY = plugdata.PlugData(self._name, "translateY", 0)
        self._translateZ = plugdata.PlugData(self._name, "translateZ", 0)
        self._translate = plugdata3.PlugData3(self.name, "translate",
                                              [self._translateX, self._translateY, self._translateZ])

        self._rotateX = plugdata.PlugData(self._name, "rotateX", 0)
        self._rotateY = plugdata.PlugData(self._name, "rotateY", 0)
        self._rotateZ = plugdata.PlugData(self._name, "rotateZ", 0)
        self._rotate = plugdata3.PlugData3(self.name, "rotate",
                                           [self._rotateX, self._rotateY, self._rotateZ])

        self._scaleX = plugdata.PlugData(self._name, "scaleX", 0)
        self._scaleY = plugdata.PlugData(self._name, "scaleY", 0)
        self._scaleZ = plugdata.PlugData(self._name, "scaleZ", 0)
        self._scale = plugdata3.PlugData3(self.name, "scale",
                                          [self._scaleX, self._scaleY, self._scaleZ])

        self._visibility = plugdata.PlugData(self._name, "visibility", 0)

        self._attributes = [self._translateX,
                            self._translateY,
                            self._translateZ,
                            self._rotateX,
                            self._rotateY,
                            self._rotateZ,
                            self._scaleX,
                            self._scaleY,
                            self._scaleZ,
                            self._visibility]

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
