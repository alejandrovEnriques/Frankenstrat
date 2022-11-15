import importlib
from maya import cmds

from Frankenstrat.rig_parts import basepart
from Frankenstrat.nodes import joint, choice, decompose_matrix, plus_minus_average, vector_product
from Frankenstrat.systems import guides, chain
from Frankenstrat import constants
from Frankenstrat.plugs import double_plug, double3_plug, enum_plug

importlib.reload(vector_product)
importlib.reload(constants)
importlib.reload(plus_minus_average)


class Limb(basepart.BasePart):

    def __init__(self, name, side, parent):
        super(Limb, self).__init__(name, side, parent)

        self._jointA = joint.Joint(constants.get_name(self._name, constants.JOINT, None, self._side, 0),
                                   self._skeleton_group)
        self._jointB = joint.Joint(constants.get_name(self._name, constants.JOINT, None, self._side, 1),
                                   self._jointA)
        self._jointC = joint.Joint(constants.get_name(self._name, constants.JOINT, None, self._side, 2),
                                   self._jointB)

        self._jointA.translateX.value = 0
        self._jointB.translateX.value = 10
        self._jointC.translateX.value = 20

        self._masterguide = guides.Guide(constants.get_name(self._name, constants.GUIDE, constants.MASTER, self._side),
                                         self._guides_group)

        self._masterguide.color(constants.RED)
        self._masterguide.size([0, 3, 3])

        self._joints = [self._jointA, self._jointB, self._jointC]
        self._guides = []
        tmp_parent = self._masterguide
        for jnt in self._joints:
            gde = guides.Guide(jnt.name.replace(constants.JOINT, constants.GUIDE))

            gde.offset.parent = tmp_parent
            gde.color(constants.YELLOW)
            self._guides.append(gde)
            tmp_parent = gde

        self._constraints = []
        self._aim_constraints = []
        self._utilities = []

        self._chain = chain.FKChain(self._name, self._side, self._rig_group, self._joints, constants.BLU)

    def create(self):
        super(Limb, self).create()

        self._jointA.create()
        self._jointB.create()
        self._jointC.create()

    def setup(self):
        self._chain.delete()

        self._masterguide.create()

        aim_choice = choice.Choice(constants.get_name(self._name, constants.CHOICE, constants.AIM, self._side))
        aim_choice.create()
        self._utilities.append(aim_choice)
        up_choice = choice.Choice(constants.get_name(self._name, constants.CHOICE, constants.UPOBJECT, self._side))
        up_choice.create()
        self._utilities.append(up_choice)

        aim_attr = enum_plug.Enum(self._masterguide.name, "aimAxis", 0, ['x', 'y', 'z', '-x', '-y', '-z'])
        up_attr = enum_plug.Enum(self._masterguide.name, "upAxis", 1, ['x', 'y', 'z', '-x', '-y', '-z'])

        self._masterguide.add_attribute(aim_attr)
        self._masterguide.add_attribute(up_attr)

        aim_choice.selector.source = aim_attr
        up_choice.selector.source = up_attr

        values = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1],
                  [-1, 0, 0],
                  [0, -1, 0],
                  [0, 0, -1]]

        for uti in self._utilities:
            for i, vector in enumerate(values):
                attrs = []
                for v, a in zip(vector, ["X", "Y", "Z"]):
                    attr = double_plug.Double(uti.name, "vector{0}{1}".format(i, a), value=v)
                    attrs.append(attr)
                vector_attr = double3_plug.Double3(uti.name, "vector{0}".format(i), attrs)
                uti.add_attribute(vector_attr)
                vector_attr.value = vector
                uti.add_option(vector_attr)



        previous_jnt = None
        for gde, jnt in zip(self._guides, self._joints):
            gde.create()
            jnt.displayLocalAxis.value = True

            gde.snap_to(jnt)

            cnt = cmds.pointConstraint(gde.name, jnt.name, mo=True)[0]
            self._constraints.append(cnt)

            if previous_jnt:
                acnt = \
                    cmds.aimConstraint(gde.name, previous_jnt.name, aimVector=[1, 0, 0], upVector=[0, 1, 0],
                                       worldUpType="vector")[0]
                self._aim_constraints.append(acnt)

                cmds.connectAttr("{0}.{1}".format(aim_choice.name, aim_choice.output.name), "{0}.aimVector".format(acnt))
                cmds.connectAttr("{0}.{1}".format(up_choice.name, up_choice.output.name), "{0}.upVector".format(acnt))


            previous_jnt = jnt

        # Plane constraint setup
        decompose_matrices = []
        for gde, jnt in zip(self._guides, self._joints):
            dcm = decompose_matrix.DecomposeMatrix(jnt.name.replace(constants.JOINT, constants.DECOMPOSEMATRIX))
            dcm.create()
            dcm.set_input_matrix(gde.name)
            decompose_matrices.append(dcm)

        AB_vec = plus_minus_average.PlusMinusAverage(constants.get_name(self._name, constants.PLUSMINUSAVERAGE,
                                                                        "ABVector", self._side))
        AB_vec.create()
        #AB_vec.input3D0.source = decompose_matrices[1].outputTranslate
        #AB_vec.input3D1.source = decompose_matrices[0].outputTranslate
        cmds.connectAttr("{0}.outputTranslate".format(decompose_matrices[1].name), "{0}.input3D[0]".format(AB_vec.name))
        cmds.connectAttr("{0}.outputTranslate".format(decompose_matrices[0].name), "{0}.input3D[1]".format(AB_vec.name))

        AB_vec.operation.stringvalue = "Subtract"

        AC_vec = plus_minus_average.PlusMinusAverage(constants.get_name(self._name, constants.PLUSMINUSAVERAGE,
                                                                        "ACVector", self._side))
        AC_vec.create()
        #AC_vec.input3D0.source = decompose_matrices[2].outputTranslate
        #AC_vec.input3D1.source = decompose_matrices[0].outputTranslate

        cmds.connectAttr("{0}.outputTranslate".format(decompose_matrices[2].name), "{0}.input3D[0]".format(AC_vec.name))
        cmds.connectAttr("{0}.outputTranslate".format(decompose_matrices[0].name), "{0}.input3D[1]".format(AC_vec.name))

        AC_vec.operation.stringvalue = "Subtract"

        up_vec = vector_product.VectorProduct(constants.get_name(self._name, constants.VECTORPRODUCT,
                                                                 "UpVector", self._side))
        up_vec.create()
        up_vec.input1.source = AB_vec.output3D
        up_vec.input2.source = AC_vec.output3D

        #cmds.connectAttr("{0}.output3D".format(AB_vec.name), "{0}.input1".format(up_vec.name))
        #cmds.connectAttr("{0}.output3D".format(AB_vec.name), "{0}.input2".format(up_vec.name))

        up_vec.operation.stringvalue = "Cross Product"

        for cnt in self._aim_constraints:

            cmds.connectAttr("{0}.{1}".format(up_vec.name, up_choice.output.name), "{0}.worldUpVector".format(cnt))

    def build(self):
        for cnt, acn in zip(self._constraints, self._aim_constraints):
            cmds.delete(cnt)
            cmds.delete(acn)
        self._constraints = []
        self._masterguide.delete()

        for jnt in self._joints:
            jnt.rot_to_orient()
        self._masterguide.delete()

        self._chain.create()

    def guides_independent(self, independent=False):
        tmp_parent = self._guides_group
        for gde in self._guides:
            if gde.offset.parent != tmp_parent.name:
                gde.offset.parent = tmp_parent
            if not independent:
                tmp_parent = gde
