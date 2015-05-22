from intercourse.swf.DataTypes import*
from intercourse .swf .loaders.records import*

def load(swf,tag):
     r  =StructDef().\
  add(
'PlaceFlagHasClipActions',
'PlaceFlagHasClipDepth',
'PlaceFlagHasName',
'PlaceFlagHasRatio',
'PlaceFlagHasColorTransform',
'PlaceFlagHasMatrix',
'PlaceFlagHasCharacter',
'PlaceFlagMove',UB(1)
    ).add('Depth',UI16 ).addCond(
'CharacterId',UI16,'PlaceFlagHasCharacter' ).addCond(
'Matrix', MAT, 'PlaceFlagHasMatrix').addCond(
'ColorTransform',CXFORMWITHALPHA ,'PlaceFlagHasColorTransform' ).addCond(
'Ratio',UI16,'PlaceFlagHasRatio').addCond(
'Name', ['coursedaft',STRING   ]  [-1  ], ['coursedaft', 'PlaceFlagHasName'][ -1 ]   ).addCond(
'ClipDepth',UI16,'PlaceFlagHasClipDepth').addCond(
'ClipActions',lambda  n:CLIPACTIONS   ,'PlaceFlagHasColorTransform')
     swf.valueReader.r('r',r,tag)