import importlib

from Frankenstrat.nodes import depend_node
from Frankenstrat.nodes import plugdata
from Frankenstrat.nodes import plugdata3

importlib.reload(depend_node)
importlib.reload(plugdata)
importlib.reload(plugdata3)


class MultiplyDivide(depend_node.DependNode):
    _maya_type = "multiplyDivide"

    def __init__(self, name):
        super(MultiplyDivide, self).__init__(name)

        self._input1X = plugdata.PlugData(self._name, "input1X", 0)
        self._input1Y = plugdata.PlugData(self._name, "input1Y", 0)
        self._input1Z = plugdata.PlugData(self._name, "input1Z", 0)
        self._input1 = plugdata3.PlugData3(self.name, "input1",
                                           [self._input1X, self._input1Y, self._input1Z])

        self._input2X = plugdata.PlugData(self._name, "input2X", 0)
        self._input2Y = plugdata.PlugData(self._name, "input2Y", 0)
        self._input2Z = plugdata.PlugData(self._name, "input2Z", 0)
        self._input2 = plugdata3.PlugData3(self.name, "input2",
                                           [self._input2X, self._input2Y, self._input2Z])

        self._operation = plugdata.PlugData(self._name, "operation", 0)

        self._outputX = plugdata.PlugData(self._name, "outputX", 0, writable=False)
        self._outputY = plugdata.PlugData(self._name, "outputY", 0, writable=False)
        self._outputZ = plugdata.PlugData(self._name, "outputZ", 0, writable=False)
        self._output = plugdata3.PlugData3(self.name, "output",
                                           [self._outputX, self._outputY, self._outputZ])

        self._attributes = [self._input1X,
                            self._input1Y,
                            self._input1Z,
                            self._input2X,
                            self._input2Y,
                            self._input2Z,
                            self._outputX,
                            self._outputY,
                            self._outputZ]

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
        return self._input1X

    @property
    def input2Y(self):
        return self._input1Y

    @property
    def input2Z(self):
        return self._input1Z

    @property
    def operation(self):
        return self._operation

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
