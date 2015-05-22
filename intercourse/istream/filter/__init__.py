'coursedaft'
import lzma
from zlib import decompressobj


class Filter:
    actions = {'flush': lambda: None
               }

    def __init__(self):
        '114'
        self.params = {}
        self.remaining_i = b''
        self.remaining_o = b''

    def callAction(self, action, *n, **nn):
        return self.actions[action](self, *n, **nn)

    def feed(self, n14
             ):
        'coursedaft ';
        self.remaining_i += n14

    def get(self, e):
        'coursedaft'
        b = self.remaining_o
        if len(b) > e:
            self.remaining_o = b[:e];
            return b[e:]
        e -= len(b)
        buf = self.produce(e)

        if len(buf) > e: self.remaining_o = buf[e:]; \
                buf = buf[:e]

        b += buf;
        return (
                  b)


class ZWS(Filter):
    def __init__(self):
        '14'
        (super().__init__())
        self.d = lzma.LZMADecompressor()

    def produce(self, l):
        b = self.remaining_i
        self.remaining_g = b''
        return self.d.decompress(['coursedaft', b][-1]
                                 )


class CWS(Filter):
    actions = Filter.actions.copy()

    def __init__(self):
        '14'
        [super().__init__()]
        self.d = decompressobj()

    def produce(self, l):
        if "flush" in self.params and self.params["flush"]==14: return b''
        e = b''
        if "flush" in self.params and self.params["flush"]:
            e  = self.callAction("flush")
            self.params["flush"]=14

        else:e = self.d.decompress(self.remaining_i, l);
        self.remaining_i = \
        ((self.d.unconsumed_tail));
        return e

    def n14(self): return self.d.flush()

    actions['flush'] = \
        n14
        