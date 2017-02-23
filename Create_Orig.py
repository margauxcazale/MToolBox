# -------------------------------------
# Create orig on selected objects
# by Felix le cha
# -------------------------------------
import maya.cmds as mc


def create_orig_on_selected():
    ''''''
    # Get Current selection
    cSelection = mc.ls(sl=True)

    for sSel in cSelection:
        # Get Parent
        s_parent = mc.listRelatives(sSel, p=True)
        if s_parent:
            s_parent = s_parent[0]

        # Get current Obj Transform
        lPos_Sel = mc.xform(sSel, q=True, t=True, ws=True)
        lRot_Sel = mc.xform(sSel, q=True, ro=True, ws=True)

        # Create a group
        sGroup = mc.group(em=True, name=sSel + '_orig')

        # Set in place
        mc.xform(sGroup, a=True, t=lPos_Sel, ro=lRot_Sel, s=[1, 1, 1])

        # Parent current to orig Group
        mc.parent(sSel, sGroup, relative=False)

        # reParent group to original parent
        if s_parent:
            mc.parent(sGroup, s_parent, relative=False)


create_orig_on_selected()