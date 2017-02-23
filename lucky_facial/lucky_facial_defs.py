#!/usr/bin/env python
# coding:utf-8


import maya.cmds as mc
import inTools as tool

reload(tool)


def lucky_facial(body):
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
        no_ns = mesh.split(':')[1]
        recup = no_ns.split('_')[-2]
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
        deform = 'shrinkWrap_facial'
        if not mc.objExists(deform):
            deform = mc.deformer(mesh, n='shrinkWrap_facial', type='shrinkWrap')[0]
            mc.setAttr(deform + '.projection', 3)
            mc.setAttr(deform + '.bidirectional', 1)
            mc.connectAttr(body + '.worldMesh[0]', deform + '.targetGeom')
        deform = mc.deformer('shrinkWrap_facial', e=True, g=mesh)
        mc.polyMoveFacet(mesh, ltz=float(ind + 2) / 1000)

    print('First pass successfully done ! ROGER')


# -------------------------------------------------
def add_to_system():
    # on selectionne un mesh et un joint. A priori le joint
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
        deform = mc.deformer('shrinkWrap_facial', e=True, g=plane)
        mc.polyMoveFacet(plane, ltz=float(ind + 2) / 1000)


    print('bravo')

# -------------------------------------------------
def add_emotions(expressions):
    masters = mc.ls(sl=True)
    for master in masters:
        mc.addAttr(master, ln='expressions', nn='Expressions', at='enum', keyable=True, enumName= expressions)