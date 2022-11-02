GROUP = "grp"
JOINT = "jnt"
LEFT = "Lf"
RIGHT = "Rt"
CENTER = "Ct"


def get_name(name, prefix, tag=None, side=None, index=None):
    fside = side or ""
    findex = str(index).zfill(2) if index else ""
    ftag = tag or ""

    return "{0}{1}{2}{3}{4}".format(prefix, name, ftag, findex, fside)
