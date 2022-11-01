import importlib
from maya import cmds

from Frankenstrat.nodes import depend_node
from Frankenstrat.nodes import plugdata
from Frankenstrat.nodes import plugdata3

importlib.reload(depend_node)
importlib.reload(plugdata)
importlib.reload(plugdata3)


class Reverse(depend_node.DependNode):
    _maya_type = "reverse"

    def __init__(self, name):
        super(Reverse, self).__init__(name)

        self._inputX = plugdata.PlugData(self._name, "inputX", 0)
        self._inputY = plugdata.PlugData(self._name, "inputY", 0)
        self._inputZ = plugdata.PlugData(self._name, "inputZ", 0)

        self._input = plugdata3.PlugData3(self._name, "input",
                                          [self._inputX, self._inputY, self._inputZ])

        self._outputX = plugdata.PlugData(self._name, "outputX", 0, writable=False)
        self._outputY = plugdata.PlugData(self._name, "outputY", 0, writable=False)
        self._outputZ = plugdata.PlugData(self._name, "outputZ", 0, writable=False)

        self._output = plugdata3.PlugData3(self._name, "output",
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
