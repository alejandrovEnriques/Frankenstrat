from maya import cmds


class DependNode:
    _maya_type = None

    def __init__(self, name):
        self._name = name

        self._attributes = []

        self._custom_attributes = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("The name of a depend node should be a basestring. Got {0}(type: {1})".format(value,
                                                                                                          type(value)))
        if cmds.objExists(self._name):
            cmds.rename(self._name, value)

        self._name = value

    def create(self):
        if self._maya_type is None:
            raise NotImplementedError
        if not cmds.objExists(self._name):
            cmds.createNode(self._maya_type, n=self._name)
        else:
            cmds.warning("A {0}node called {1} already Exist. Creation skipped".format(self._maya_type, self._name))

        for attr in self._attributes:
            attr.restore()

    def delete(self):
        if cmds.objExists(self._name):
            cmds.delete(self._name)

        for attr in self._attributes:
            attr.store()

    def get_custom_attribute(self, attribute_name):
        for attribute in self._custom_attributes:
            if attribute.name == attribute_name:
                return attribute

    def add_attribute(self, attribute):
        attribute.create()
        self._custom_attributes.append(attribute)
        if hasattr(attribute, "children"):
            for plug in attribute.children:
                self._custom_attributes.append(plug)
