#!/usr/bin/env python
# coding:utf-8
""":mod:`inTools`
===================================

.. module:: inTools
   :platform: Unix
   :synopsis: tools needed in facial tool def
   :author: lcm
   :date: 2017.02

"""
import maya.cmds as mc


def snap_from_to(snapeur, snaped):
    con = mc.pointConstraint(snapeur, snaped, maintainOffset=False)
    mc.delete(con)


def create_shape(control, size):
    cercle = mc.circle(nr=(0, 1, 0), r=size)
    mc.delete(cercle, constructionHistory=True)
    shape = mc.listRelatives(cercle[0], s=True)
    mc.parent(shape[0], control, s=True, r=True)
    mc.rename(shape, '{}Shape'.format(control))
    mc.delete(cercle[0])


def more_ctrl(names=None):
    sysList = []
    if names is None:
        names = mc.ls(sl=True)

    for i, inter in enumerate(names):
        bonename = '{}_{}_ctrl'.format(inter, i + 1)
        origname = '{}_{}_orig'.format(inter, i + 1)
        mc.createNode('joint', n=bonename)
        mc.createNode('transform', n=origname)
        snap_from_to(bonename, origname)
        mc.parent(bonename, origname, relative=False)
        create_shape(bonename, 1)
        sysList.append((bonename, origname))

    return sysList