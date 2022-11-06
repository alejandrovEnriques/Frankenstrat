GROUP = "grp"
GUIDEGROUP = "grpGuide"
JOINT = "jnt"
GUIDE = "gde"
CONTROL = "ctl"
MASTER = "Master"

LEFT = "Lf"
RIGHT = "Rt"
CENTER = "Ct"


#TAGS
FK = "Fk"
IK = "Ik"

# Colors
RED = 13
BLU = 14
GREEN = 14
YELLOW = 17



def get_name(name, prefix, tag=None, side=None, index=None):
    fside = side or ""
    findex = str(index).zfill(2) if index is not None else ""
    ftag = tag or ""

    return "{0}{1}{2}{3}{4}".format(prefix, name, ftag, findex, fside)
