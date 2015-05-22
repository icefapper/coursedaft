from intercourse.swf.DataTypes import*
from .records.txt import *
from intercourse.swf.loaders.records import*
def load(swf,tag):
  n= StructDef()    .add(
      'CharacterID',UI16). add(
      'TextBounds',RECT).add(
      'TextMatrix',MAT).add(
      'GlyphBits',
      'AdvanceBits',UI8).add(
      'TextRecords',TEXTRECORD(tag)*( lambda n14 :not n14[0]  == 0 ))
  swf.valueReader.r('r',n,tag)