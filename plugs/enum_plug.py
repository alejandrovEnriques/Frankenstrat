from maya import cmds


class Enum:

    def __init__(self, node, name, value=None, options=None, source=None, writable=True):
        self._node = node
        self._name = name
        self._value = value
        self._stringvalue = None
        self._options = options
        if not self._options:
            self._options = []
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
            self._value = cmds.getAttr("{0}.{1}".format(self._node, self._name))
            self._stringvalue = self._options[self._value]

        return self._value

    @value.setter
    def value(self, the_value):

        if not self._writable:
            raise RuntimeError("The plug cannot be set because it is read-only.")

        if self._source:
            raise RuntimeError("The plug has an incoming connection from {0}.{1}".format(self._source.node,
                                                                                         self._source.name))
        if cmds.objExists(self._node):
            self._value = cmds.setAttr("{0}.{1}".format(self._node, self._name), the_value)

        self._value = the_value
        self._stringvalue = self._options[the_value]

    @property
    def stringvalue(self):
        if self._source:
            return self._source.value

        if cmds.objExists(self._node):
            self._value = cmds.getAttr("{0}.{1}".format(self._node, self._name))
            self._stringvalue = self._options[self._value]

        return self._stringvalue

    @stringvalue.setter
    def stringvalue(self, the_value):

        if not self._writable:
            raise RuntimeError("The plug cannot be set because it is read-only.")

        if self._source:
            raise RuntimeError("The plug has an incoming connection from {0}.{1}".format(self._source.node,
                                                                                         self._source.name))
        if cmds.objExists(self._node) and the_value in self._options:
            self._value = cmds.setAttr("{0}.{1}".format(self._node, self._name), self._options.index(the_value))

        self._stringvalue = the_value
        self._stringvalue = self._options.index(the_value)

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
        self._source = valuee

    def create(self, parent=None):
        if not cmds.objExists("{0}.{1}".format(self._node, self._name)):
            cmds.addAttr(self._node, at="enum", ln=self._name, en=':'.join(self._options), k=True)

        self.value = self._value

    def restore(self):
        self._source = None
        if self._writable:
            self.value = self._value

    def store(self):
        self._value = self.value
