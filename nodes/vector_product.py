import importlib

from maya import cmds

from Frankenstrat.nodes import depend_node
from Frankenstrat.plugs import double_plug, double3_plug, data_plug, enum_plug

importlib.reload(depend_node)
importlib.reload(data_plug)
importlib.reload(double3_plug)


class VectorProduct(depend_node.DependNode):
    _maya_type = "vectorProduct"

    def __init__(self, name):
        super(VectorProduct, self).__init__(name)

        self._operation = enum_plug.Enum(self._name, "operation", 1, ['No operation', 'Dot Product', 'Cross Product',
                                                                      'Vector Matrix Product', 'Point Matrix Product'])
        self._output = data_plug.Data(self._name, "output")

        self._input1X = double_plug.Double(self._name, "input1X", 0)
        self._input1Y = double_plug.Double(self._name, "input1Y", 0)
        self._input1Z = double_plug.Double(self._name, "input1Z", 0)
        self._input1 = double3_plug.Double3(self.name, "input1",
                                              [self._input1X, self._input1Y, self._input1Z])

        self._input2X = double_plug.Double(self._name, "input2X", 0)
        self._input2Y = double_plug.Double(self._name, "input2Y", 0)
        self._input2Z = double_plug.Double(self._name, "input2Z", 0)
        self._input2 = double3_plug.Double3(self.name, "input2",
                                              [self._input2X, self._input2Y, self._input2Z])

        self._outputX = double_plug.Double(self._name, "outputX", 0)
        self._outputY = double_plug.Double(self._name, "outputY", 0)
        self._outputZ = double_plug.Double(self._name, "outputZ", 0)
        self._output = double3_plug.Double3(self.name, "output",
                                              [self._outputX, self._outputY, self._outputZ])

        self._attributes = [self._operation,
                            self._input1X,
                            self._input1Y,
                            self._input1Z,
                            self._input2X,
                            self._input2Y,
                            self._input2Z,
                            self._outputX,
                            self._outputY,
                            self._outputZ
                            ]

        self._options = []

    @property
    def operation(self):
        return self._operation
    @property
    def input1(self):
        return self._input1

    @property
    def input1X(self):
        return self._input1X

    @property
    def input1Y(self):
        return self._input1Y

    @property
    def input1Z(self):
        return self._input1Z

    @property
    def input2(self):
        return self._input2

    @property
    def input2X(self):
        return self._input2X

    @property
    def input2Y(self):
        return self._input2Y

    @property
    def input2Z(self):
        return self._input2Z

    @property
    def output(self):
        return self._output
    @property
    def outputX(self):
        return self._outputX

    @property
    def outputY(self):
        return self._outputY

    @property
    def outputZ(self):
        return self._outputZ

    def add_option(self, attribute):
        self._options.append(attribute)
        cmds.connectAttr("{0}.{1}".format(attribute.node, attribute.name),
                         "{0}.input[{1}]".format(self._name, len(self._options) - 1))
