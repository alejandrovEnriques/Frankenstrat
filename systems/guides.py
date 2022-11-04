import importlib

from Frankenstrat import constants
from Frankenstrat.nodes import locator
from Frankenstrat.nodes import transform


class Guide(locator.Locator):

    def __init__(self, name, parent=None):
        super(Guide, self).__init__(name, parent)
        self._offset = transform.Transform(self._name.replace(constants.GUIDE, constants.GROUP), parent=parent)
        self.parent = self._offset

    def create(self):
        self._offset.create()
        super(Guide, self).create()

    @property
    def offset(self):
        return self._offset
