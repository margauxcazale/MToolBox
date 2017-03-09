

import maya.cmds as mc
import inTools as tool
import maya.mel as mel
reload(tool)
reload(mel)


def lucky_facial(body, deformname):
    # body est le mesh de base sur lequel on va mettre les plaques
    plaques = mc.ls(sl=True)
    recup_plaques = []
    recup_locators = []
    if len(plaques) == 0:
        return

    for ind, mesh in enumerate(plaques):
        # create locator and snap it to mesh
        locator = mc.spaceLocator(n=mesh + '_loc', p=(0, 0, 0))
        tool.snap_from_to(mesh, locator)
        recup_locators.append(locator)
        # recup name part to name ctrl
        nohi = mesh.split('_')[1:-1]
        recup = '_'.join(nohi)
        recup_plaques.append(recup)

    # ctrlTuple est une liste de tuples
    ctrl_tuple = tool.more_ctrl(recup_plaques)
    # snap aux locs
    for i, locator in enumerate(recup_locators):
        tool.snap_from_to(locator, ctrl_tuple[i][1])
        mc.delete(locator)

    # skin and shrinkwrap
    for ind, mesh in enumerate(plaques):
        mc.skinCluster(mesh, ctrl_tuple[ind][0], tsb=True, rui=True)

        deform = deformname
        if not mc.objExists(deform):
            deform = mc.deformer(mesh, n=deformname, type='shrinkWrap')[0]
            mc.setAttr(deform + '.projection', 3)
            mc.setAttr(deform + '.closestIfNoIntersection', 1)
            mc.setAttr(deform + '.bidirectional', 1)
            mc.connectAttr(body + '.worldMesh[0]', deform + '.targetGeom')

        deform = mc.deformer(deformname, e=True, g=mesh)
        mc.polyMoveFacet(mesh, ltz=float(ind + 2) / 1000)

    print('First pass successfully done ! ROGER')


# -------------------------------------------------
def add_to_system():
    # on selectionne des mesh et un joint.
    depart = mc.ls(sl=True)
    bone = []
    ajout = []
    for i in depart:
        if mc.objectType(i, i='joint') == 1:
            bone.append(i)
        else:
            ajout.append(i)

    if len(bone) >= 1:
        bone = bone[0]

    for ind, plane in enumerate(ajout):
        mc.skinCluster(plane, bone, tsb=True, rui=True)
        swName= mc.listHistory(plane)[2]
        deform = mc.deformer(swName, e=True, g=plane)
        mc.polyMoveFacet(plane, ltz=float(ind + 2) / 1000)

# -------------------------------------------------
def remove_from_system():
    # on selectionne une liste de mesh.
    depart = mc.ls(sl=True)
    if len(depart) == 0:
        return
    for mesh in depart:
        swName= mc.listHistory(mesh)[2]
        if mc.getAttr(swName+'.envelope') == 1:
            mc.setAttr(swName+'.envelope',0)
            mc.deformer(e=True, rm=True, g=mesh, swName)
            #cmd =str('deformer -e -rm -g "{}" "shrinkWrap_facial"'.format(mesh))
            #mel.eval(cmd)
            mc.skinCluster(mesh, e=True, ub=True)
            cleanM ='{}.output'.format(mc.listHistory(mesh)[1])
            mc.disconnectAttr(cleanM, mesh + '.inMesh')
        mc.setAttr(swName+'.envelope', 1)

# -------------------------------------------------
def add_expressions(part_name, expressions):

    masters = mc.ls(sl=True)

    for master in masters:
        if part_name == '':
            part_name = "Expressions"
            mc.addAttr(master, ln=part_name, nn=part_name, at='enum', keyable=False, enumName=expressions)
        else:
            mc.addAttr(master, ln=part_name, nn=part_name, at='enum', keyable=True, enumName= expressions)
