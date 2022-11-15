from maya import cmds


class Data(object):

    def __init__(self, node, name, value=None, source=None, writable=True):
        self._node = node
        self._name = name
        self._value = value
        self._source = source
        self._writable = writable

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
        if self._source:
            return self._source.value

        if cmds.objExists(self._node):
            try:
                self._value = cmds.getAttr("{0}.{1}".format(self._node, self._name))
            except Exception as e:
                print(e)

        return self._value

    @value.setter
    def value(self, the_value):
        raise NotImplementedError


    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        if value is None:
            cmds.disconnectAttr("{0}.{1}".format(self._source.node, self._source.name),
                                "{0}.{1}".format(self._node, self._name))
        else:
            cmds.connectAttr("{0}.{1}".format(value.node, value.name),
                             "{0}.{1}".format(self._node, self._name))
        self._source = value

    def restore(self):
        self._source = None
        if self._writable:
            self.value = self._value

    def store(self):
        self._value = self.value
