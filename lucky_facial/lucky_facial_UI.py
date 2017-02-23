#!/usr/bin/env python
# coding:utf-8


import maya.cmds as mc
import lucky_facial_defs as lfd
reload(lfd)

# -------------------------------------------------
def show_facial_UI():
    sWindow = 'facial_2D'
    if mc.window(sWindow, q=True, ex=True):
        mc.deleteUI(sWindow)

    mc.window(sWindow, t='Build 2D rig on face')
    mc.columnLayout(columnAttach=('both', 5), rowSpacing=10, columnWidth=200)
    mc.separator(h=25)
    mc.text(label='Base')
    mc.text(label='Enter name of base mesh for facial rig')
    mc.textField('tell_body')
    mc.button(w=100, label='Build first pass', command='lfd.lucky_facial(mc.textField("tell_body", q=True, text=True))')
    mc.separator(h=10, style='in')
    mc.text(label='Select ctrl and mesh you want to add')
    mc.button(w=100, label='Add to system', command='lfd.add_to_system()')
    mc.separator(h=10, style='in')
    mc.text(label='Emotions')
    mc.text(label='Select controls you want to add attr to')
    mc.text(label='Must be  happy:sad:etc  type')
    mc.textField('enum_names')
    mc.button(w=100, label='Emotions to control', c='lfd.add_emotions(mc.textField("enum_names", q=True, text=True))')
    mc.showWindow(sWindow)

show_facial_UI()