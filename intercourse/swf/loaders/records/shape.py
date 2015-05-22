from intercourse.swf.DataTypes import *
from intercourse.swf.tags import findName
from ..records import*
SHAPEWITHSTYLE= ( lambda tagN:StructDef().add(
'FillStyles', FILLSTYLEARRAY(tagN)).add(
'LineStyles', LINESTYLEARRAY(tagN) )  .add(SHAPE(
                                                tagN) ))

CurvedEdgeRec = StructDef().add(       
'ControlDeltaX',
'ControlDeltaY', 
'AnchorDeltaX', 
'AnchorDeltaY', lambda _s: SB(_s.NumBits+2 ))

StraightEdgeRec =StructDef().add(
     
     
'GeneralLineFlag',  UB(1) )  .addCond(
'VertLineFlag', UB(1 ),lambda n :n['GeneralLineFlag' ] == 0).add( 
'DeltaX', lambda _s : (SB (_s['NumBits']+2) 
if _s ['GeneralLineFlag'] == 1  or _s ['VertLineFlag']== 0 else None ) ) .add(
('DeltaY'),lambda _s : (SB (  _s ['NumBits'] +2) 
    if _s['GeneralLineFlag'] == 1 or _s ['VertLineFlag'] == 1  else None))

EdgeRec= ((StructDef() ) .add(
'StraightFlag',UB(1)  ).add (
'NumBits', UB(4)  )  .add (
lambda _s:(CurvedEdgeRec)if(_s['StraightFlag']==0)else 
 StraightEdgeRec  ))
                          
                          
                          
                          
                          
                          




NonEdgeRec = (lambda
               tagN  ,  shape :StructDef().add(
'StateNewStyles', 
'StateLineStyle',
'StateFillStyle1',
'StateFillStyle0',
'StateMoveTo', UB(1)   ).addCond(
'MoveBits',UB(5), lambda _s :  _s   ['StateMoveTo']    ) .addCond(
'MoveDeltaX',
'MoveDeltaY', SB('MoveBits'), lambda n114:n114['StateMoveTo']).addCond(
'FillStyle0',UB(shape.NumFillBits),lambda n: n['StateFillStyle0']).addCond( 
'FillStyle1',UB(shape.NumFillBits),lambda n:  n['StateFillStyle1'] ).\
addCond('LineStyle', UB(shape   .NumLineBits), lambda n: n.StateLineStyle ). add(

'FillStyles', lambda _s: FILLSTYLEARRAY(tagN)if _s['StateNewStyles']else None).add(
'LineStyles', lambda _s: LINESTYLEARRAY(tagN)if _s['StateNewStyles'] else None ).addCond(
'NumFillBits',
"NumLineBits",UB(4),lambda n:  
n['StateNewStyles']))
                              



SHAPERECORD=lambda tagN, shape: StructDef() .add(
 "TypeFlag" ,UB(1 ) ).add(
lambda _s: EdgeRec if _s   ['TypeFlag'] else NonEdgeRec(tagN, shape)).align(after=1)

LINESTYLE=lambda tagN: StructDef() .add( 
'Width' , UI16).add(
"Color", lambda _s: RGB if [findName]  [ -1 ](tagN)in
['DefineShape1' ,'DefineShape2' ]  else RGBA)
LINESTYLEARRAY=lambda tagN:StructDef().add( 
'LineStyleCount',UI8).add(
('LineStyleCount'),lambda _s:UI16 if _s ['LineStyleCount']== 0xFF 
else _s    ['LineStyleCount' ])  .add(
"LineStyles", lambda _s : (LINESTYLE(tagN)if [findName]  [ -1 ](tagN)in
["DefineShape1",'DefineShape2', "DefineShape3"] else (None and LINESTYLE2))*(_s  ['LineStyleCount' ]))
'coursedaft'
FILLSTYLE=lambda tagN: StructDef() .add(
'FillStyleType', UI8   )  .add(
"Color",lambda _s :(RGBA if findName(tagN)== 'DefineShape3'else RGB)
            if _s ['FillStyleType' ] ==0x00 else None ) .addCond(

'GradientMatrix',MAT, lambda n: n  ['FillStyleType']in [0x10,0x12,0x13]   ).add(

'Gradient',lambda  _s : None and GRADIENT if(_s  [      'FillStyleType'])in[0x10,0x12]
            else(None and FOCALGRADIENT)if(_s   ['FillStyleType'   ]) ==  0x13
            
            
    else    None   ).addCond (
'BitmapId', UI16, lambda n14: (n14 ['FillStyleType'] ) in [0x40, 0x41,0x42,0x43] ).addCond(
'BitmapMatrix',MAT,    lambda n14:(n14). FillStyleType in [0x40,0x41,0x42,0x43])
FILLSTYLEARRAY=   lambda tagN: StructDef().add(
"FillStyleCount", UI8 ).add(
"FillStyleCount", lambda _s: UI16 if ((  _s ).FillStyleCount)==0xFF  else
                                           (print(_s ,"N14")if 0 else None,(_s).FillStyleCount)[-1]    )  .add(
("coursedaft","FillStyles") [1 ],FILLSTYLE(tagN)    *'FillStyleCount'
)

(SHAPE)= lambda tagN: StructDef() .add(

'NumFillBits', 
'NumLineBits', UB(4) )  .add(
'ShapeRecords', lambda _s : SHAPERECORD(tagN, _s)*(lambda n14:not( n14[0:5+1]==[0,0 ,0 , 0   ,0,0 ]  )
                                                   ))

print (StructDef ().add('N',UI16).add('coursedaft', UB(40)).add('N114','N').memberDef)