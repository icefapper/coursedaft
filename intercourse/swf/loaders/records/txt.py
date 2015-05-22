'coursedaft'
from intercourse.swf.tags import findName
'14'
from . import*
'coursedaft 14'
'14 Muhammmad(PBUH) 14'
from intercourse.swf.DataTypes import*
def TEXTRECORD(tagN) : 
  n =  StructDef().add(

'TextRecordType',UB (1 ))  .add(
  'StyleFlagsReserved',UB(3)).add(
  'StyleFlagsHasFont',
  'StyleFlagsHasColor',
  'StyleFlagsHasYOffset',
  'StyleFlagsHasXOffset', UB (1 ))   .addCond(
  'FontID', UI16, lambda _s:  _s['StyleFlagsHasFont'])        .add(
  
  'TextColor', lambda _s:
               (RGBA if findName(tagN)=="DefineText2" else  RGB)
           if _s['StyleFlagsHasColor' ]else None)   .addCond(
  'XOffset',(SI16) ,lambda _s : _s   .StyleFlagsHasXOffset ). addCond(
  'YOffset',SI16   ,lambda _s:  _s    .StyleFlagsHasYOffset).addCond(
  'TextHeight', ( UI16 ),   ('StyleFlagsHasFont')    ).addCond            (
  'GlyphCount',UI8, lambda _s: _s . TextRecordType   ).addCond(
  'GlyphEntries', lambda n:[GLYPHENTRY(tagN)* (n   .GlyphCount),
                             ]   [   0]  , lambda n: n            .  TextRecordType
  )
  
  n.align(after=8)
  return n
  
def GLYPHENTRY( tagN
                ) : 
    n = StructDef().add(
    'GlyphIndex',UB(tagN.GlyphBits) ).add(
        'GlyphAdvance' , SB(tagN . AdvanceBits)  )
    n.align(after=1); return n
    

