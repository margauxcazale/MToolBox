#!/usr/bin/env python
# coding:utf-8
""":mod:`facial_lucky_cats`
===================================

.. module:: builder_eye_lucky_cats
   :platform: Unix
   :synopsis: build rig system for lucky cats eyes
    + snap by same words Option between meshes and ctrls
   :author: lcm
   :date: 2017.02

"""

import maya.cmds as mc
import inTools as tool

reload(tool)


def lucky_facial(body):
    # body est le mesh de base sur lequel on va mettre les plaques
    plaques = mc.ls(sl=True)
    recup_plaques = []
    recup_locators = []

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

    # skin and shrinkwrap
    for ind, mesh in enumerate(plaques):
        mc.skinCluster(mesh, ctrl_tuple[ind][0], tsb=True, rui=True)
        deform = mc.deformer('shrinkWrap_facial', e=True, g=mesh)
        deform = 'shrinkWrap_facial'
        if not mc.objExists(deform):
            deform = mc.deformer(mesh, n='shrinkWrap_facial', type='shrinkWrap')[0]
            mc.setAttr(deform + '.projection', 3)
            mc.setAttr(deform + '.bidirectional', 1)
            mc.connectAttr(body + '.worldMesh[0]', deform + '.targetGeom')
        mc.polyMoveFacet(ltz=float(ind + 1) / 1000)


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

    for plane in ajout:
        mc.skinCluster(plane, bone, tsb=True, rui=True)
        deform = mc.deformer('shrinkWrap_facial', e=True, g=plane)


# -------------------------------------------------
def add_emotions(expressions=[]):
    expressions = []
    masters = mc.ls(sl=True)
    names_enum = ':'.join(expressions)
    print names_enum
    for master in masters:
        mc.addAttr(master, ln='expressions', nn='Expressions', at='enum', keyable=True)
        mc.setAttr(master + '.expressions', e=True, en=names_enum)


#def prout(**kwargs):
#     print kwargs
#
# prout(toto=1, margouette='colouette')


