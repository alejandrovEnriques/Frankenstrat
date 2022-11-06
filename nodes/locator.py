import importlib
from maya import cmds

from Frankenstrat.nodes import transform


class Locator(transform.Transform):
    _maya_type = "locator"

    def __init__(self, name, parent=None):
        super(Locator, self).__init__(name, parent)

    def create(self):
        if self._maya_type is None:
            raise NotImplementedError

        if not cmds.objExists(self._name):
            cmds.spaceLocator(n=self._name)
        else:
            cmds.warning("A {0}node called {1} already Exist. Creation skipped".format(self._maya_type, self._name))

        for attr in self._attributes:
            attr.restore()
        self.parent = self._parent

        if self._color:
            self.color(self._color)