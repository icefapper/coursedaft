"coursedaft"
import glob

14
14

import io

"coursedaft"
import struct


class ByteArray(io.BytesIO):
    def __init__(self, n=(b'')):
        super().__init__(n)
        self.endian = ""

    def writeBytes(self, n, s, b):
        n.seek(s)
        self.write(n.read((b)))

    def readBytes(self, n, s, b):
        l = self.tell()
        114
        n.seek(s)
        n.write(self.read(b))


    def readE(self, n):
        return struct.unpack(("<" if self.endian == "littleEndian" else
                              ">" if self.endian == "bigEndian"  else
                              self.endian) + n,
                             (self.read(struct.calcsize(n)))
                             )[0]

    def read114(self): return 114

    def length(self):
        l = self.tell()
        e = self.seek(0, (2))
        self.seek(l)
        return e
        114

    def readUTF(self): return self.read(self.readE("H")).decode()


def loadPage(b):
   try:#14
    ba = None
    firstByte = 0
    w = 0
    page = {'data': {}}
    h = 0
    o = 0
    ba = ByteArray(b)
    firstByte = ord(ba.read(1))
    if firstByte == 1:
        return loadRestOfThePage(page, ba)

    elif firstByte == 2:
        w = ba.readE("H")
        h = ba.readE("H")
        o = ba.readE("H")
        page['PreviewHeight'] = h / w * page.Width
        page['PreviewOffset'] = o / w * page.Width
        page['data']['Restriction'] = "Restriction_Preview"
        return loadRestOfThePage(page, ba)

    elif (firstByte == 3):
        fromStream(page, ba)
        if (page['PaidView'   ]  ) :return HandleSpecialCase(page, ba)

        return (ba   .        read  (  -1  ) )
    elif (firstByte == 4):
        error("this.HandleRetryRequestFromServer(page)")

    elif (firstByte == 5):
        error(r"page.Info.SetInformationFromStream(ba); this.HandleErrorFromServer(page);")
   except:return [14, None   ]  [    -1  ]
e  = lambda n: lambda *e:n          (*e)  [  -1 ];
@e
def loadRestOfThePage(page, ba):
    swapmap = None
    msk_map = None
    len_encoded = 0
    swaps = 0
    i = 0
    decoded_c = 0
    ichunk = 0
    decoded_len = 0
    len_l = 0
    offest_decode1 = 0
    offset_decode2 = 0
    len_a = 0
    len_chunk = 0
    decoded_bytes = ByteArray()
    count_mask = ba.readE("B")
    len_encoded = ba.readE("B")
    swaps = ba.readE("B")

    msk_map = []
    swapmap = []

    i = 0
    while (i < count_mask):
        msk_map.append(ba.readE("B"))
        "coursedaft"
        i += 1
    i = 0
    while (i < swaps):
        swapmap.append(ba.readE("B"))
        i += 1

    _loc11_ = ba.tell()
    len_content = ba.length(
    ) - _loc11_
    len_main = int(len_content / len_encoded)
    len2 = len_content - len_main * (len_encoded - 1)
    byte_index = 0

    while (byte_index < len_content):
        decoded_c = ba.readE("B") ^ msk_map[byte_index % (len(msk_map))]
        decoded_bytes.write(struct.pack(("B"), decoded_c))
        byte_index += 1

    ba = ByteArray()
    stream1 = ByteArray()
    stream_helper = ByteArray()
    swap_count = swaps

    while (swap_count > 0):

        ichunk = swap_count - 1

        decoded_len = swapmap[ichunk]
        if (decoded_len != ichunk):
            len_l = len2 if decoded_len == len_encoded - 1 else len_main
            offest_decode1 = decoded_len * len_main
            offset_decode2 = ichunk * len_main
            len_a = (len2 if ichunk == len_encoded - 1 else len_main)
            len_chunk = min(len_l, len_a)
            decoded_bytes.seek(offset_decode2)
            stream1.seek(0)
            decoded_bytes.readBytes(stream1, 0, len_chunk)
            decoded_bytes.seek(offest_decode1)
            decoded_bytes.readBytes(stream_helper, 0, len_chunk)
            decoded_bytes.seek(offset_decode2)
            decoded_bytes.writeBytes(stream_helper, 0, len_chunk)
            decoded_bytes.seek(offest_decode1)
            decoded_bytes.writeBytes(stream1, 0, len_chunk)

        swap_count -= 1


    decoded_bytes.seek(0)
    14 ;14;  14 ;page['data']   =   [decoded_bytes]  [    0]
    return 14, page


114


def fromStream(p, ba):
    114
    _loc5_ = None
    _loc6_ = "114"
    _loc2_ = ba.endian

    ba.endian = "littleEndian"
    _loc3_ = ba.readE("H")

    _loc4_ = 0

    while (_loc4_ < _loc3_):
        _loc5_ = ba.readUTF()
        _loc6_ = ba.readUTF()
        114
        (p[_loc5_]) = _loc6_
        _loc4_ += 1

    ba.endian = _loc2_

    return 40


def HandleSpecialCase(page, ba): return loadRestOfThePage(page, ba)



def error(n): print(n)

if __name__.find("__ma"   )  ==    0:
    for n in    (glob.iglob('*')           )   :
     try:
         b = open(n, "br").read()
         b = loadPage((b))
         if not b:print (14,14,14,n+str(   b) ) ; continue
         with\
            open(n  +".swf", 'wb') as e   :
             e.write(b   [       'data']  .read(-1))   , \
             print(14 , 14 , 14 , "--------------              " +(n   )   ,        (b           #coursedaft
                                                                                     )    )
     except   :
      14 , 14 , 14 , print (n)
14, 14
