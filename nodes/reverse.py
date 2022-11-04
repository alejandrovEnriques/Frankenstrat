import importlib

from Frankenstrat.nodes import depend_node
from Frankenstrat.plugs import double_plug, double3_plug

importlib.reload(depend_node)
importlib.reload(double_plug)
importlib.reload(double3_plug)


class Reverse(depend_node.DependNode):
    _maya_type = "reverse"

    def __init__(self, name):
        super(Reverse, self).__init__(name)

        self._inputX = double_plug.Double(self._name, "inputX", 0)
        self._inputY = double_plug.Double(self._name, "inputY", 0)
        self._inputZ = double_plug.Double(self._name, "inputZ", 0)

        self._input = double3_plug.Double3(self._name, "input",
                                           [self._inputX, self._inputY, self._inputZ])

        self._outputX = double_plug.Double(self._name, "outputX", 0, writable=False)
        self._outputY = double_plug.Double(self._name, "outputY", 0, writable=False)
        self._outputZ = double_plug.Double(self._name, "outputZ", 0, writable=False)

        self._output = double3_plug.Double3(self._name, "output",
                                            [self._outputX, self._outputY, self._outputZ])

        self._attributes = [self._inputX, self._inputY, self._inputZ,
                            self._outputX, self._outputY, self._outputZ]

    @property
    def input(self):
        return self._input

    @property
    def inputX(self):
        return self._inputX

    @property
    def inputY(self):
        return self._inputY

    @property
    def inputZ(self):
        return self._inputZ

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
