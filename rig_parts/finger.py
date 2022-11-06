import importlib
from maya import cmds

from Frankenstrat.rig_parts import basepart
from Frankenstrat.nodes import joint
from Frankenstrat.systems import guides, chain
from Frankenstrat import constants

importlib.reload(constants)


class Finger(basepart.BasePart):

    def __init__(self, name, side, parent):
        super(Finger, self).__init__(name, side, parent)

        self._jointA = joint.Joint(constants.get_name(self._name, constants.JOINT, None, self._side, 0),
                                   self._skeleton_group)
        self._jointB = joint.Joint(constants.get_name(self._name, constants.JOINT, None, self._side, 1),
                                   self._jointA)
        self._jointC = joint.Joint(constants.get_name(self._name, constants.JOINT, None, self._side, 2),
                                   self._jointB)
        self._jointD = joint.Joint(constants.get_name(self._name, constants.JOINT, None, self._side, 3),
                                   self._jointC)
        self._jointE = joint.Joint(constants.get_name(self._name, constants.JOINT, None, self._side, 4),
                                   self._jointD)

        self._jointA.translateX.value = 0
        self._jointB.translateX.value = 5
        self._jointC.translateX.value = 10
        self._jointD.translateX.value = 15
        self._jointE.translateX.value = 20

        self._masterguide = guides.Guide(constants.get_name(self._name, constants.GUIDE, constants.MASTER, self._side),
                                         self._guides_group)

        self._masterguide.color(constants.RED)

        self._joints = [self._jointA, self._jointB, self._jointC, self._jointD, self._jointE]
        self._guides = []
        tmp_parent = self._masterguide
        for jnt in self._joints:
            gde = guides.Guide(jnt.name.replace(constants.JOINT, constants.GUIDE))

            gde.offset.parent = tmp_parent
            gde.color(constants.YELLOW)
            self._guides.append(gde)
            tmp_parent = gde

        self._constraints = []

        self._chain = chain.FKChain(self._name, self._side, self._rig_group, self._joints, constants.BLU)

    def create(self):
        super(Finger, self).create()

        self._jointA.create()
        self._jointB.create()
        self._jointC.create()
        self._jointD.create()
        self._jointE.create()

    def setup(self):
        self._chain.delete()

        self._masterguide.create()

        previous_jnt = None
        for gde, jnt in zip(self._guides, self._joints):
            gde.create()
            jnt.displayLocalAxis.value = True

            gde.snap_to(jnt)

            cnt = cmds.pointConstraint(gde.name, jnt.name, mo=True)[0]
            self._constraints.append(cnt)

            if previous_jnt:
                cnt = cmds.aimConstraint(gde.name, previous_jnt.name, aimVector=[1, 0, 0], upVector=[0, 1, 0])[0]
                self._constraints.append(cnt)

            previous_jnt = jnt

    def build(self):
        for cnt in self._constraints:
            cmds.delete(cnt)
        self._constraints = []
        self._masterguide.delete()

        for jnt in self._joints:
            jnt.rot_to_orient()

        self._chain.create()

    def guides_independent(self, independent=False):
        tmp_parent = self._guides_group
        for gde in self._guides:
            print(gde.offset)
            if gde.offset.parent != tmp_parent.name:
                gde.offset.parent = tmp_parent
            if not independent:
                tmp_parent = gde
