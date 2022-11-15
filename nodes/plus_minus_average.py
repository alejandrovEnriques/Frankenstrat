import importlib

from maya import cmds

from Frankenstrat.nodes import depend_node
from Frankenstrat.plugs import double_plug, double3_plug, data_plug, enum_plug

importlib.reload(depend_node)
importlib.reload(data_plug)
importlib.reload(double3_plug)


class PlusMinusAverage(depend_node.DependNode):
    _maya_type = "plusMinusAverage"

    def __init__(self, name):
        super(PlusMinusAverage, self).__init__(name)

        self._operation = enum_plug.Enum(self._name, "operation", 1, ['No operation', 'Sum', 'Subtract', 'Average'])
        self._output = data_plug.Data(self._name, "output")

        self._input3Dx0 = double_plug.Double(self._name, "input3D[0].input3Dx", 0)
        self._input3Dy0 = double_plug.Double(self._name, "input3D[0].input3Dy", 0)
        self._input3Dz0 = double_plug.Double(self._name, "input3D[0].input3Dz", 0)
        self._input3D0 = double3_plug.Double3(self.name, "input3D[0]",
                                              [self._input3Dx0, self._input3Dy0, self._input3Dz0])

        self._input3Dx1 = double_plug.Double(self._name, "input3D[1].input3Dx", 0)
        self._input3Dy1 = double_plug.Double(self._name, "input3D[1].input3Dy", 0)
        self._input3Dz1 = double_plug.Double(self._name, "input3D[1].input3Dz", 0)
        self._input3D1 = double3_plug.Double3(self.name, "input3D[1]",
                                              [self._input3Dx1, self._input3Dy1, self._input3Dz1])

        self._output3Dx = double_plug.Double(self._name, "output3D.output3Dx", 0)
        self._output3Dy = double_plug.Double(self._name, "output3D.output3Dy", 0)
        self._output3Dz = double_plug.Double(self._name, "output3D.output3Dz", 0)
        self._output3D = double3_plug.Double3(self.name, "output3D",
                                              [self._output3Dx, self._output3Dy, self._output3Dz])

        self._attributes = [self._operation,
                            self._input3Dx0, self._input3Dy0, self._input3Dz0,
                            self._input3Dx1, self._input3Dy1, self._input3Dz1,
                            self._output3Dx, self._output3Dy, self._output3Dz,
                            ]

        self._options = []

    @property
    def operation(self):
        return self._operation

    @property
    def input3D0(self):
        return self._input3D0

    @property
    def input3Dx0(self):
        return self._input3Dx0

    @property
    def input3Dy0(self):
        return self._input3Dy0

    @property
    def input3Dz0(self):
        return self._input3Dz0

    @property
    def input3D1(self):
        return self._input3D1

    @property
    def input3Dx1(self):
        return self._input3Dx1

    @property
    def input3Dy1(self):
        return self._input3Dy1

    @property
    def input3Dz1(self):
        return self._input3Dz1

    @property
    def output3D(self):
        return self._output3D

    @property
    def output3Dx(self):
        return self._output3Dx

    @property
    def output3Dy(self):
        return self._output3Dy

    @property
    def output3Dz(self):
        return self._output3Dz

    def add_option(self, attribute):
        self._options.append(attribute)
        cmds.connectAttr("{0}.{1}".format(attribute.node, attribute.name),
                         "{0}.input[{1}]".format(self._name, len(self._options) - 1))
