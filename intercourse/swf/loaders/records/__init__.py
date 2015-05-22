from intercourse.swf.DataTypes import *





RGB= StructDef().add    ('R', 'G','B', UI8)
RGBA=StructDef().add(RGB).add('A',  UI8 )

ARGB =  StructDef().add('A',UI8  ) .add(RGB


)

RECT= StructDef().add(
'Nbits',UB(5)).add(
'Xmin',
'Xmax',
'Ymin',
'Ymax',(SB('Nbits'  ))   )

MAT=StructDef().add(
'HasScale', UB    (1)     ).addCond(
'NScaleBits',UB(5) ,'HasScale').addCond(
'ScaleX',
'ScaleY',FB('NScaleBits') ,lambda _s:_s .HasScale==1).add(
'HasRotate', UB(1
                ) )   .addCond(
'NRotateBits', UB(5),'HasRotate') .addCond (
'RotateSkew0',
'RotateSkew1',FB('NRotateBits')   , lambda _s:_s.HasRotate==1 ) .    add(
'NTranslateBits' ,UB(5) ).add(
'TranslateX',
'TranslateY',
SB('NTranslateBits'   )   ).align(before=8)

CXFORM_m=(StructDef())   .add(
'HasAddTerms', UB(1)).add(
'HasMultTerms',  UB(1)).add(
'Nbits', UB(4) ).addCond(
'RMultTerm', SB('Nbits'), 'HasMultTerms').addCond(
'GMultTerm', (('BMultTerm')), SB('Nbits'),

             'HasMultTerms'   );

CXFORM_a = StructDef().addCond(


'RAddTerm', SB('Nbits')   ,'HasAddTerms') .addCond(
'GAddTerm', 'BnAddTerm', SB(('Nbits'))    ,'HasAddTerms')

CXFORM = StructDef().add(CXFORM_m   ).add(CXFORM_a).align(before=8)

CXFORMWITHALPHA=(StructDef().add(CXFORM_m).addCond('AlphaMultTerm',SB('Nbits'),'HasMultTerms' ).
                             add(CXFORM_a).addCond(

                             ['coursedaft', 'AlphaAddTerm']   [ -1 ] , SB       (['Nbits'][0 ])   ,'HasAddTerms'))   .align   (  (      8)  ); "coursedaft"
LANGCODE=UI8