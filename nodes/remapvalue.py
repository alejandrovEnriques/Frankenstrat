import importlib

from Frankenstrat.nodes import depend_node
from Frankenstrat.plugs import double_plug, double3_plug

importlib.reload(depend_node)
importlib.reload(double_plug)
importlib.reload(double3_plug)


class RemapValue(depend_node.DependNode):
    _maya_type = "remapValue"

    def __init__(self, name):
        super(RemapValue, self).__init__(name)

        self._inputMax = double_plug.Double(self._name, "inputMax", 0)
        self._inputMin = double_plug.Double(self._name, "inputMin", 0)
        self._inputValue = double_plug.Double(self._name, "inputValue", 0)
        self._outputMax = double_plug.Double(self._name, "outputMax", 0)
        self._outputMin = double_plug.Double(self._name, "outputMin", 0)

        self._outValue = double_plug.Double(self._name, "outValue", 0, writable=False)

        self._outColorR = double_plug.Double(self._name, "outColorR", 0, writable=False)
        self._outColorG = double_plug.Double(self._name, "outColorG", 0, writable=False)
        self._outColorB = double_plug.Double(self._name, "outColorB", 0, writable=False)

        self._outColor = double3_plug.Double3(self.name, "outColor",
                                              [self._outColorR, self._outColorG, self._outColorB])

        self._attributes = [self._inputMax,
                            self._inputMin,
                            self._inputValue,
                            self._outputMax,
                            self._outputMin,

                            self._outValue,
                            self._outColorR,
                            self._outColorG,
                            self._outColorB]

    @property
    def inputMax(self):
        return self._inputMax

    @property
    def inputMin(self):
        return self._inputMin

    @property
    def inputValue(self):
        return self._inputValue

    @property
    def outputMax(self):
        return self._outputMax

    @property
    def outputMin(self):
        return self._outputMin

    @property
    def outValue(self):
        return self._outValue

    @property
    def outColorR(self):
        return self._outColorR

    @property
    def outColorG(self):
        return self._outColorG

    @property
    def outColorB(self):
        return self._outColorB

    @property
    def outColor(self):
        return self._outColor
