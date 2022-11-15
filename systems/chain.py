import importlib
from maya import cmds
from Frankenstrat import constants
from Frankenstrat.nodes import transform
from Frankenstrat.systems import control

importlib.reload(control)


class FKChain:

    def __init__(self, name, side, parent, joints, color):
        self._name = name
        self._joints = joints
        self._side = side
        self._parent = parent
        self._group = transform.Transform(constants.get_name(self._name, constants.GROUP, constants.FK,
                                                             self._side, None), self._parent)
        self._color = color

        self._controls = []
        self._constraints = []

        tmp_parent = self._group
        for jnt in self._joints:
            ctl = control.Control(jnt.name.replace(constants.JOINT, constants.CONTROL))
            ctl.offset.parent = tmp_parent
            ctl.color(self._color)
            self._controls.append(ctl)
            tmp_parent = ctl

    def create(self):
        self._group.create()

        for ctl, jnt in zip(self._controls, self._joints):
            ctl.create()

            ctl.snap_to(jnt)

            pcnt = cmds.parentConstraint(ctl.name, jnt.name)
            scnt = cmds.scaleConstraint(ctl.name, jnt.name)

            self._constraints.append(pcnt)
            self._constraints.append(scnt)

    def delete(self):

        for cnt in self._constraints:
            cmds.delete(cnt)
        self._constraints = []

        # for ctl in self._controls:
        #    cmds.delete()
        self._group.delete()
