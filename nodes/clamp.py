import importlib

from Frankenstrat.nodes import depend_node
from Frankenstrat.nodes import plugdata
from Frankenstrat.nodes import plugdata3

importlib.reload(depend_node)
importlib.reload(plugdata)
importlib.reload(plugdata3)


class Clamp(depend_node.DependNode):
    _maya_type = "clamp"

    def __init__(self, name):
        super(Clamp, self).__init__(name)

        self._inputR = plugdata.PlugData(self._name, "inputR", 0)
        self._inputG = plugdata.PlugData(self._name, "inputG", 0)
        self._inputB = plugdata.PlugData(self._name, "inputB", 0)
        self._input = plugdata3.PlugData3(self.name, "input",
                                          [self._inputR, self._inputG, self._inputB])

        self._maxR = plugdata.PlugData(self._name, "maxR", 0)
        self._maxG = plugdata.PlugData(self._name, "maxG", 0)
        self._maxB = plugdata.PlugData(self._name, "maxB", 0)
        self._max = plugdata3.PlugData3(self.name, "max",
                                        [self._maxR, self._maxG, self._maxB])

        self._minR = plugdata.PlugData(self._name, "minR", 0)
        self._minG = plugdata.PlugData(self._name, "minG", 0)
        self._minB = plugdata.PlugData(self._name, "minB", 0)
        self._min = plugdata3.PlugData3(self.name, "min",
                                        [self._minR, self._minG, self._minB])

        self._renderPassMode = plugdata.PlugData(self._name, "renderPassMode", 0)

        self._outputR = plugdata.PlugData(self._name, "outputR", 0, writable=False)
        self._outputG = plugdata.PlugData(self._name, "outputG", 0, writable=False)
        self._outputB = plugdata.PlugData(self._name, "outputB", 0, writable=False)
        self._output = plugdata3.PlugData3(self.name, "output",
                                           [self._outputR, self._outputG, self._outputB])

        self._attributes = [self._inputR, self._inputG, self._inputB,
                            self._maxR, self._maxG, self._maxB,
                            self._minR, self._minG, self._minB,
                            self._outputR, self._outputG, self._outputB,
                            self._renderPassMode]

    @property
    def input(self):
        return self._input

    @property
    def inputR(self):
        return self._inputR

    @property
    def inputG(self):
        return self._inputG

    @property
    def inputB(self):
        return self._inputB

    @property
    def max(self):
        return self._max

    @property
    def maxR(self):
        return self._maxR

    @property
    def maxG(self):
        return self._maxG

    @property
    def maxB(self):
        return self._maxB

    @property
    def min(self):
        return self._min

    @property
    def minR(self):
        return self._minR

    @property
    def minG(self):
        return self._minG

    @property
    def minB(self):
        return self._minB

    @property
    def renderPassMode(self):
        return self._renderPassMode

    @property
    def output(self):
        return self._output

    @property
    def outputR(self):
        return self._outputR

    @property
    def outputG(self):
        return self._outputG

    @property
    def outputB(self):
        return self._outputB
