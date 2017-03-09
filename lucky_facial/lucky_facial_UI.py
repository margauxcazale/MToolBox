""":mod:`lucky_facial_UI`
===================================
.. module:: moduleName
   :platform: Unix
   :synopsis: module idea
   :author: lcm
   :date: 2017.02
import mayaRigTools_sk.sandBox.lcm.facial2D.facial_lucky_cats as flc
import mayaRigTools_sk.sandBox.lcm.facial2D.lucky_facial_UI as uI
reload(flc)
reload(uI)
uI.show_facial_UI()
"""


import maya.cmds as mc
import facial_lucky_cats as flc
reload(flc)

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
    mc.text(label='Name of the deformer')
    mc.textField('tell_deform')
    mc.button(w=100, label='Build first pass', command='flc.lucky_facial(mc.textField("tell_body", q=True, text=True), mc.textField("tell_deform", q=True, text=True))')
    mc.separator(h=10, style='in')
    mc.text(label='Select ctrl and mesh you want to add')
    mc.button(w=100, label='Add to system', command='flc.add_to_system()')
    mc.separator(h=10, style='in')
    mc.button(w=100, label='Remove from system', command='flc.remove_from_system()')
    mc.separator(h=10, style='in')
    mc.text(label='Expressions')
    mc.text(label='Enter name of face part')
    mc.text(label='If none, it writes "expressions" ')
    mc.textField('tell_part')
    mc.text(label='Select controls you want to add attr to')
    mc.text(label='Must be exp01:exp02:exp03 type')
    mc.textField('tell_enum_names')
    mc.button(w=100, label='Expressions to control', command='flc.add_expressions(mc.textField("tell_part", q=True, text=True), mc.textField("tell_enum_names", q=True, text=True))')
    mc.showWindow(sWindow)

show_facial_UI()