import importlib
from maya import cmds
from Frankenstrat.nodes import transform
from Frankenstrat import constants

importlib.reload(constants)


class BasePart:

    def __init__(self, name, side=None, parent=None):
        self._name = name
        self._side = side or ""
        self._parent = parent

        self._created = False

        self._group = None
        self._skeleton_group = None
        self._rig_group = None
        self._guides_group = None
        self._group = transform.Transform(constants.get_name(self._name, constants.GROUP, None, self._side, None),
                                          self._parent)

        self._skeleton_group = transform.Transform(constants.get_name(self._name, constants.GROUP, "Skeleton",
                                                                      self._side, None),
                                                   self._group)

        self._rig_group = transform.Transform(constants.get_name(self._name, constants.GROUP, "Rig",
                                                                 self._side, None),
                                              self._group)

        self._guides_group = transform.Transform(constants.get_name(self._name, constants.GROUP, "Guides",
                                                                    self._side, None),
                                                 self._group)

    def create(self):
        if self._created:
            raise RuntimeError("Part already created")

        self._group.create()
        self._skeleton_group.create()
        self._rig_group.create()
        self._guides_group.create()
        self._created = True

    def setup(self):
        pass

    def build(self):
        pass
