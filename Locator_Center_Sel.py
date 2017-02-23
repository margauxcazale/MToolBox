'''
-maya
-createlocator on center of components selection
-margie
'''

import maya.cmds as mc

def locator_center(components)
components=mc.ls(sl=True, fl=True)
longueur= len(components)

totx= 0
toty= 0
totz= 0

for vtx in components:
    position= mc.xform(vtx, q=True, t=True, ws=True)
    print position
    totx= totx + position[0]
    toty= toty + position[1]
    totz= totz + position[2]

placementX= totx / longueur
placementY= toty / longueur
placementZ= totz / longueur

loc= mc.spaceLocatore(n='centered_locator')
mc.move(placementX, placementY, placementZ, loc)

locator_center()