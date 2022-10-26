# from maya impot cmds
import importlib

from Frankenstrat.nodes import depend_node

importlib.reload(depend_node)


class Reverse(depend_node.DependNode):
    _maya_type = "reverse"

    def __init__(self, name):
        super(Reverse, self).__init__(name)
