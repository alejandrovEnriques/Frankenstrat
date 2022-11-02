import importlib

from Frankenstrat.rig_parts import base_part
from Frankenstrat.nodes import joint
from Frankenstrat import constants

importlib.reload(base_part)
importlib.reload(joint)
importlib.reload(constants)


class Finger(base_part.Base_Part):

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

    def create(self):
        super(Finger, self).create()

        self._jointA.create()
        self._jointB.create()
        self._jointC.create()
        self._jointD.create()
        self._jointE.create()
