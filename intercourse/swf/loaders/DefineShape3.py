from intercourse.swf.DataTypes import*
from .records import*
from .records.shape\
 import\
    *
n = None
def load(swf,tag):
    '14'; global n
    if not n:\
    n = StructDef().add(
  'ShapeId', UI16 )   .add(
'ShapeBounds', RECT)   .add(
'Shapes', SHAPEWITHSTYLE(tag
                         ))
    swf.valueReader.r('r',n,tag)