import importlib

from Frankenstrat.nodes import depend_node
from Frankenstrat.nodes import plugdata

importlib.reload(depend_node)
importlib.reload(plugdata)


class RemapValue(depend_node.DependNode):
    _maya_type = "remapValue"

    def __init__(self, name):
        super(RemapValue, self).__init__(name)

        self._inputMax = plugdata.PlugData(self._name, "inputMax", 0)
        self._inputMin = plugdata.PlugData(self._name, "inputMin", 0)
        self._inputValue = plugdata.PlugData(self._name, "inputValue", 0)
        self._outputMax = plugdata.PlugData(self._name, "outputMax", 0)
        self._outputMin = plugdata.PlugData(self._name, "outputMin", 0)

        self._value_Position = plugdata.PlugData(self._name, "value_Position", 0.0)
        self._value_FloatValue = plugdata.PlugData(self._name, "value_FloatValue", 0.0)
        self._value_Interp = plugdata.PlugData(self._name, "value_Interp", 0.0)

        self._outValue = plugdata.PlugData(self._name, "outValue", 0, writable=False)

        self._outColorR = plugdata.PlugData(self._name, "outColorR", 0, writable=False)
        self._outColorG = plugdata.PlugData(self._name, "outColorG", 0, writable=False)
        self._outColorB = plugdata.PlugData(self._name, "outColorB", 0, writable=False)

        self._outColor = plugdata.PlugData3(self.name, "outColor",
                                            [self._outColorR, self._outColorG, self._outColorB])

        self._attributes = [self._inputMax,
                            self._inputMin,
                            self._inputValue,
                            self._outputMax,
                            self._outputMin,
                            self._value_Position,
                            self._value_FloatValue,
                            self._value_Interp,
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
