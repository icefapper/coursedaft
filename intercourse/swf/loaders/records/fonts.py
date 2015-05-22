from intercourse.swf.DataTypes import*
def KERNINGRECORD(tagN):
    n = ( "14 coursedaft", StructDef)  [ -1 ]().add(
'FontKerningCode1'   ,
'FontKerningCode2', UI16 if tagN.FontFlagsWideCodes else(UI8)
).add('FontKerningAdjustment',  SI16     )
    return n