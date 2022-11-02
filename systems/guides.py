import importlib

from maya import cmds

from Frankenstrat.nodes import transform

#from Frankenstrat.nodes import locator
from Frankenstrat import constants

#importlib.reload(locator)
importlib.reload(transform)
importlib.reload(constants)


class Guide(transform.Transform):

    def __init__(self, name, side=None, parent=None):
        name = constants.get_name(name, constants.GUIDE, None, side, None)

        super(Guide, self).__init__(name, parent)
        self._offset = transform.Transform(self._name.replace(constants.GUIDE, constants.GROUP), parent=parent)
        self.parent = self._offset

    def create(self):
        self._offset.create()
        super(Guide, self).create()
