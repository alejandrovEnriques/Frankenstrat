import importlib

from maya import cmds
from Frankenstrat.nodes import depend_node
from Frankenstrat.plugs import double_plug, double3_plug

importlib.reload(depend_node)
importlib.reload(double_plug)
importlib.reload(double3_plug)


class DecomposeMatrix(depend_node.DependNode):
    _maya_type = "decomposeMatrix"

    def __init__(self, name):
        super(DecomposeMatrix, self).__init__(name)

        self._outputTranslateX = double_plug.Double(self._name, "outputTranslateX", 0)
        self._outputTranslateY = double_plug.Double(self._name, "outputTranslateY", 0)
        self._outputTranslateZ = double_plug.Double(self._name, "outputTranslateZ", 0)

        self._outputTranslate = double3_plug.Double3(self._name, "outputTranslate",
                                                     [self._outputTranslateX, self._outputTranslateY,
                                                      self._outputTranslateZ])

        self._outputRotateX = double_plug.Double(self._name, "outputRotateX", 0)
        self._outputRotateY = double_plug.Double(self._name, "outputRotateY", 0)
        self._outputRotateZ = double_plug.Double(self._name, "outputRotateZ", 0)

        self._outputRotate = double3_plug.Double3(self._name, "outputRotate",
                                                  [self._outputRotateX, self._outputRotateY, self._outputRotateZ])

        self._outputScaleX = double_plug.Double(self._name, "outputScaleX", 0)
        self._outputScaleY = double_plug.Double(self._name, "outputScaleY", 0)
        self._outputScaleZ = double_plug.Double(self._name, "outputScaleZ", 0)

        self._outputScale = double3_plug.Double3(self._name, "outputScale",
                                                 [self._outputScaleX, self._outputScaleY, self._outputScaleZ])

        self._outputShearX = double_plug.Double(self._name, "outputShearX", 0)
        self._outputShearY = double_plug.Double(self._name, "outputShearY", 0)
        self._outputShearZ = double_plug.Double(self._name, "outputShearZ", 0)

        self._outputShear = double3_plug.Double3(self._name, "outputShear",
                                                 [self._outputShearX, self._outputShearY,
                                                  self._outputShearZ])

        self._attributes = [self._outputTranslateX, self._outputTranslateY, self._outputTranslateZ,
                            self._outputRotateX, self._outputRotateY, self._outputRotateZ,
                            self._outputScaleX, self._outputScaleY, self._outputScaleZ,
                            self._outputShearX, self._outputShearY, self._outputShearZ
                            ]

    @property
    def outputTranslate(self):
        return self._outputTranslate

    @property
    def outputTranslateX(self):
        return self._outputTranslateX

    @property
    def outputTranslateY(self):
        return self._outputTranslateY

    @property
    def outputTranslateZ(self):
        return self._outputTranslateZ

    @property
    def outputRotate(self):
        return self._outputRotate

    @property
    def outputRotateX(self):
        return self._outputRotateX

    @property
    def outputRotateY(self):
        return self._outputRotateY

    @property
    def outputRotateZ(self):
        return self._outputRotateZ

    @property
    def outputScale(self):
        return self._outputScale

    @property
    def outputScaleX(self):
        return self._outputScaleX

    @property
    def outputScaleY(self):
        return self._outputScaleY

    @property
    def outputScaleZ(self):
        return self._outputScaleZ

    @property
    def outputShear(self):
        return self._outputShear

    @property
    def outputShearX(self):
        return self._outputShearX

    @property
    def outputShearY(self):
        return self._outputShearY

    @property
    def outputShearZ(self):
        return self._outputShearZ

    def set_input_matrix(self, transform):
        cmds.connectAttr("{0}.worldMatrix[0]".format(transform), "{0}.inputMatrix".format(self._name))

