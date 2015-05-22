'coursedaft'
14
14 , 14
def process(
            converter , tagN)            :
    if not tagN.CharacterId in ( converter   .common ["ID"]   .   o)   : raise Exception (tagN)
    converter.common['display':[]].append({"ed": tagN.ClipDepth if tagN.PlaceFlagHasClipDepth else 0,
                                           "sd": tagN.Depth   ,
                                           "ch": tagN.CharacterId if tagN.PlaceFlagHasCharacter else None})
