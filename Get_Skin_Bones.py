import maya.cmds as mc

getBones= []
chosenSkin= 'skinClusterX'
bones= mc.listConnections(chosenSkin, s=True, d=False, t= 'joint')
getBones.append(bones)
mc.select(getBones)
print getBones
print('Got it.')