import importlib

from Frankenstrat.nodes import depend_node
from Frankenstrat.nodes import plugdata

importlib.reload(depend_node)
importlib.reload(plugdata)


class BlendColors(depend_node.DependNode):
    _maya_type = "blendColors"

    def __init__(self, name):
        super(BlendColors, self).__init__(name)

        self._color1R = plugdata.PlugData(self._name, "color1R", 0)
        self._color1G = plugdata.PlugData(self._name, "color1G", 0)
        self._color1B = plugdata.PlugData(self._name, "color1B", 0)
        self._color1 = plugdata.PlugData3(self.name, "color1",
                                          [self._color1R, self._color1G, self._color1B])

        self._color2R = plugdata.PlugData(self._name, "color2R", 0)
        self._color2G = plugdata.PlugData(self._name, "color2G", 0)
        self._color2B = plugdata.PlugData(self._name, "color2B", 0)
        self._color2 = plugdata.PlugData3(self.name, "color2",
                                          [self._color2R, self._color2G, self._color2B])

        self._blender = plugdata.PlugData(self._name, "blender", 0)

        self._outputR = plugdata.PlugData(self._name, "outputR", 0, writable=False)
        self._outputG = plugdata.PlugData(self._name, "outputG", 0, writable=False)
        self._outputB = plugdata.PlugData(self._name, "outputB", 0, writable=False)
        self._output = plugdata.PlugData3(self.name, "output",
                                          [self._outputR, self._outputG, self._outputB])

        self._attributes = [self._color1R,
                            self._color1G,
                            self._color1B,
                            self._color2R,
                            self._color2G,
                            self._color2B,
                            self._outputR,
                            self._outputG,
                            self._outputB]

    @property
    def color1R(self):
        return self._color1R

    @property
    def color1G(self):
        return self._color1G

    @property
    def color1B(self):
        return self._color1B

    @property
    def color2R(self):
        return self._color1R

    @property
    def color2G(self):
        return self._color1G

    @property
    def color2B(self):
        return self._color1B

    @property
    def blender(self):
        return self._blender

    @property
    def outputR(self):
        return self._outputR

    @property
    def outputG(self):
        return self._outputG

    @property
    def outputB(self):
        return self._outputB
