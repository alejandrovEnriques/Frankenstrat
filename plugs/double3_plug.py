from maya import cmds


class Double3(object):

    def __init__(self, node, name, plugs):
        self._node = node
        self._name = name
        self._plugs = plugs

    @property
    def node(self):
        return self._node

    @node.setter
    def node(self, value):
        self._node = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

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
        for plug, value in zip(self._plugs, values.children):
            plug.source = value

    @property
    def children(self):
        return self._plugs

    def create(self):
        if not cmds.objExists("{0}.{1}".format(self._node, self._name)):
            cmds.addAttr(self._node, at="double3", ln=self._name, k=True)

        for plug in self._plugs:
            cmds.addAttr(self._node, at="double", ln=plug.name, k=True, p=self._name)
            #plug.value = plug._value

    def restore(self):
        self._source = None
        self.value = self._value

    def store(self):
        self._value = self.value
