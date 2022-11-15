import importlib

from maya import cmds

from Frankenstrat.nodes import depend_node
from Frankenstrat.plugs import double_plug, double3_plug, data_plug

importlib.reload(depend_node)
importlib.reload(data_plug)
importlib.reload(double3_plug)


class Choice(depend_node.DependNode):
    _maya_type = "choice"

    def __init__(self, name):
        super(Choice, self).__init__(name)

        self._selector = double_plug.Double(self._name, "selector", 0)
        self._output = data_plug.Data(self._name, "output")

        self._attributes = [self._selector]

        self._options = []

    @property
    def selector(self):
        return self._selector

    @property
    def output(self):
        return self._output

    def add_option(self, attribute):
        self._options.append(attribute)
        cmds.connectAttr("{0}.{1}".format(attribute.node, attribute.name),
                         "{0}.input[{1}]".format(self._name, len(self._options)-1))
