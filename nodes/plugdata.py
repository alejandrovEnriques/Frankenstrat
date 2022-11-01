from maya import cmds


class PlugData(object):

    def __init__(self, node, attribute, value=None, source=None, writable=True):
        self._node = node
        self._attribute = attribute
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
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = value

    @property
    def value(self):
        if self._source:
            return self._source.value

        if cmds.objExists(self._node):
            self._value = cmds.getAttr("{0}.{1}".format(self._node, self._attribute))

        return self._value

    @value.setter
    def value(self, the_value):

        if not self._writable:
            raise RuntimeError("The plug cannot be set because it is read-only.")

        if self._source:
            raise RuntimeError("The plug has an incoming connection from {0}.{1}".format(self._source.node,
                                                                                         self._source.attribute))
        if cmds.objExists(self._node):
            self._value = cmds.setAttr("{0}.{1}".format(self._node, self._attribute), the_value)

        self._value = the_value

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        if value is None:
            cmds.disconnectAttr("{0}.{1}".format(self._source.node, self._source.attribute),
                                "{0}.{1}".format(self._node, self._attribute))
        else:
            cmds.connectAttr("{0}.{1}".format(value.node, value.attribute),
                             "{0}.{1}".format(self._node, self._attribute))
        self._source = value

    def restore(self):
        self._source = None
        if self._writable:
            self.value = self._value

    def store(self):
        self._value = self.value
