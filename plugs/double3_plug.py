from maya import cmds


class Double3(object):

    def __init__(self, node, attribute, plugs):
        self._node = node
        self._attribute = attribute
        self._plugs = plugs

    @property
    def node(self):
        return self._node

    @node.setter
    def node(self, value):
        self._node = value

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = value

    @property
    def value(self):
        return [plug.value for plug in self._plugs]

    @value.setter
    def value(self, the_value):
        for plug, value in zip(self._plugs, the_value):
            plug.value = value

    @property
    def source(self):
        return [plug.source for plug in self._plugs]

    @source.setter
    def source(self, values):
        for plug, value in zip(self._plugs, values):
            plug.value = value

    def restore(self):
        self._source = None
        self.value = self._value

    def store(self):
        self._value = self.value
