import maya.cmds as mc


def snap_from_to(snapeur, snaped):
    con = mc.parentConstraint(snapeur, snaped, maintainOffset=False)
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
        bonename = '{}_ctrl'.format(inter)
        origname = '{}_orig'.format(inter)
        mc.createNode('joint', n=bonename)
        mc.setAttr(bonename+'.radius', 0.1)
        mc.createNode('transform', n=origname)
        snap_from_to(bonename, origname)
        mc.parent(bonename, origname, relative=False)
        create_shape(bonename, 0.1)
        sysList.append((bonename, origname))

    return sysList



def bound_to_center_box():
    gnrSel = mc.ls( sl = True)
    prems = gnrSel[0]
    deuz = gnrSel[1]
    keeper = list()
    keeper.append(prems)
    keeper.append(deuz)
    bbox = mc.exactWorldBoundingBox(keeper[0])


    center = [(bbox[0] + bbox[3]) / 2, (bbox[1] + bbox[4]) / 2, (bbox[2] + bbox[5]) / 2]
    mc.spaceLocator( a=True, n = 'locatoreuh')
    mc.setAttr( 'locatoreuh.translate', center[0], center[1], center[2] ,type= 'double3')
    deucontrainte = mc.parentConstraint( 'locatoreuh', keeper[1], n = 'deucontrainte')
    mc.delete('deucontrainte')
    mc.delete('locatoreuh')



def bound_to_bottom_box():
    gnrSel = mc.ls(sl=True)
    prems = gnrSel[0]
    deuz = gnrSel[1]
    keeper = list()
    keeper.append(prems)
    keeper.append(deuz)
    bbox = mc.exactWorldBoundingBox(keeper[0])

    bottom = [(bbox[0] + bbox[3]) / 2, bbox[1], (bbox[2] + bbox[5]) / 2]
    mc.spaceLocator(a=True, n='locatoreuh')
    mc.setAttr('locatoreuh.translate', bottom[0], bottom[1], bottom[2], type='double3')
    deucontrainte = mc.parentConstraint('locatoreuh', keeper[1], n='deucontrainte')
    mc.delete('deucontrainte')
    mc.delete('locatoreuh')