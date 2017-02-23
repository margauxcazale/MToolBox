import maya.cmds as mc

sel = mc.ls(sl=True)
for control in sel:
    if not 'ctrl' in control:
        break

    if sel == 0:
        recupC= mc.sets('anim_set',q=True, im=True, s=True, fl=True)
        sel =mc.ls(recupC, s=True)

    mc.setAttr(control + '.tx', 0)
    mc.setAttr(control + '.ty', 0)
    mc.setAttr(control + '.tz', 0)
    mc.setAttr(control + '.rx', 0)
    mc.setAttr(control + '.ry', 0)
    mc.setAttr(control + '.rz', 0)
    mc.setAttr(control + '.sx', 1)
    mc.setAttr(control + '.sy', 1)
    mc.setAttr(control + '.sz', 1)