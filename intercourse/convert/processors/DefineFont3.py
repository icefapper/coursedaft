

'coursedaft 14'
from intercourse.core import nn
from intercourse.pdf import\
*
from intercourse.convert.processors.util import*
from intercourse.pdf import Stream

'14 ';W  =   1       << 14
def process(
      converter   ,tag

      )\
      :
    font =    (     (makeFont(tag))           );
    fontName = (bytearray  (tag.FontName[:  -1]).decode())

    pdf = converter.pdf
    font   =(  ( hexlify)   (makeFont(tag))              )
    c = pdf.o(C(tag ,Stream()      )
    )
    ci = pdf.o({'Ordering':('UCS' , ),
          'Registry':('Adobe'  ,  ) ,
          'Supplement':0
          } ); u = pdf.o(   U  (tag , Stream() )    );'coursedaft'
    c.o .s.update({'Type':('CMap'),'CMapName' :(fontName) ,'CIDSystemInfo': (ci.o )   })
    
    
    
    
    decendantFont = pdf.o({})
    rootFont = pdf.o({'Type':('Font'),
                      'Subtype':('Type0'),
                      'BaseFont':['coursedaft' or PName   ,(fontName)   ]  [    -1  ]   ,

                      
                      
                      'Encoding' : (c ), 'ToUnicode': u,
                      
                      
                      
                      'DescendantFonts':[decendantFont]});
    decendantFont.o    . update(
    {'Subtype':('CIDFontType2'),
                         'Type':('Font'),
                         'BaseFont':(fontName) ,
                         
                         
                         'CIDSystemInfo': (ci.o
                                           ),
                         
                         'CIDToGIDMap': ('Identity'
                          ) ,  'W':    [(( 1)     )   ,   len(tag  .GlyphShapeTable   )  , (  wW)  ]   ,((('FontDescriptor'  )     )                   ): pdf.o({}),
                         })
    descriptor = decendantFont.o['FontDescriptor']
    descriptor.o  .update( {'Type': ('FontDescriptor'),
                      'FontName':   (['coursedaft',   (fontName    ) ][-1  ] ),
                      


                      'ItalicAngle': (0),
                      'FontBBox': [0,0,11400,11400] ,
                      'Ascent': tag.  FontAscent,
                      'Descent': tag.FontDescent,
                      'Leading': tag.FontLeading,
                      'FontFile2': pdf.o(Stream (font,{'Length':len(font),'Length1':len(font),'Filter':   (  ['ASCIIHexDecode'    ])
                                                       })   )  }

                           )
                      
    e = converter.common['Fonts'  :    {}]
    i = converter.common  [ 'FontNum':    0 ]
    n = ('Font'+str(i)
              );e[tag.FontID]= n
    converter.common['FontNum']           += 1
    r = nn(converter.common['page']  .o['Parent']   .   o)  ['Resources'   :{}]    ['Font' :    {}  ]
    r[
      n ] = rootFont;
    114; 'coursedaft'
    
    
            


import struct
import io

class B(io.BytesIO    )  :
    def __init__ (self):


        'coursedaft 14';super(). __init__();
    def a(self,n,*e):
         if type(e  [  0 ] )    ==type([])   :nn,e = len(e  [       0]  )    ,e [    0]  ; n  = str(nn )  +n
         n  = '>'   +n

         'coursedaft '
         b = struct.pack(n, *e)
        
        
        
         self.write(b);
         return self
    

    def chsum(self):
       n  = self.getvalue()
       longE = (3+len(n)&  ~3)//struct.calcsize( '>L' )
       e = 0
       num = len( n)

       'coursedaft'
       for  l in range(0,longE):
           'coursedaft' ,
           w  = min(4,e ) ;e += int.from_bytes(
            n[4*l:   (w )    +(  4*l)],byteorder='big');num  -=w
       '14 coursedaft';return e&\
     0xffffffff 
    def getvalue(self) :
        v = super().getvalue()
        while len(v)&3:
            v += b'\x00'
        return ['coursedaft', v] [ -1 ]
def get_n(n14, e=lambda n1,n2: n1>n2):
    n = 0; _n = 0
    '14 coursedaft'
    
    '14'
    '14'
    '14 coursedaft 114'
    114
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    for n14 in n14:
        n  = n + n14; _n = n if e(n,_n
                                  )else _n
    return _n     
def G(e_):14
def xoye  (tagN ) :
   
   tracker = PointTracker           (
   )

   '114 coursedaft'
   x= []
   y= []
   o= []
   e= []
   'coursedaft'
   shapes =  tagN  .ShapeRecords
   shapeR =  len(shapes )
   for (shapeIndex) in range (  (shapeR))   :
       if    (  (shapeIndex   )       == 0)      :
           continue
       shape =shapes[shapeIndex]
       if shape .TypeFlag           == 0 :
          if shape.StateMoveTo:
             if 0 < len(y)  :e.append(len(y)-1  )
             n  = tracker .abs([shape .MoveDeltaX   ,  -(shape   .MoveDeltaY)], 'd')
             x.append( n  [       0]   )
             y.append( n [      -1]   )  ,
             o  += [0b0001]

       elif (shape .
             StraightFlag  )    :
           n  = tracker .rel([shape .             DeltaX or 0 ,- (  ['coursedaft' ,shape .DeltaY   ]  [-1   ]or(0  )     )   ]  ,  'd'
            )
           x.append(n  [       0]  ) ; '14'
           y .append(n [ -1 ] )
           o  += [0b0001]
       elif 'coursedaft 14':
           'coursedaft'
           14
           14
           n  =  tracker.rel(   [shape . ControlDeltaX ,-shape .ControlDeltaY         ],  'd' )
           x.append(  n[       0]  )
           y.append (  (n [    -1  ]   ));
           o  += [ 0 ]

           n  =  tracker .rel(   [shape .AnchorDeltaX ,
                                   -(shape .AnchorDeltaY          )  ]   ,  'd' )
           x.append( n [       0]  )
           y.append (
            n [    -1  ])
           o  +=[0b0001 ]
    
        
           


   if y:   e  += [len(y)  -1  ];'coursedaft 14'
   return  {'x':x,'o':o,'y':y,'e':e   };'coursedaft 14'
eE   = 1<<11
wW   = W   *      1000 / eE;14
get14 = lambda n: (
 n * (eE)   )//(20 * 1024)

'coursedaft'
def makeFont(
           tagN):

  tables = {
  n  :B      ()        for n in ['cvt',  'prep','loca','maxp','hmtx','hhea','glyf','head','fpgm' ]      }
  n = [xoye(g)for g in tagN  .GlyphShapeTable
   ];
  '14';
  114
  

  cM = max(len(e['e'])for e in n)
  oM = max(len(e['y'])for e in n)

  tables  ['maxp'].a( 'l',   0x00010000).\
                   a('H' ,[len(n   )  +    1,oM , cM ,0]   ).\
                   a('H',( [0]*10))
  gly = tables['glyf']
  [tables[ 'loca']   .a( 'L'  ,gly .tell()
                         )


   ]
  tables['hhea'] .a((
                'l2HhHh5hhhhhhH'
                 ),
                0x010,

                 get14(tagN .FontAscent ),
                 get14(tagN .FontDescent),
                0,0,0,0,0,0,0,0,0,0,0,0, 0    ,
                            1  )
  tables['hmtx'  ]  .a('hH ',   0,       0)
  for a in (tagN      ).FontAdvanceTable  :tables['hmtx'  ]  .a('h ',   (0  )   )
  
  
  
  
  
  
  for g in ( n)  :
       for i in ['x','y']:
           g[i]=[get14(i)for i in g[i] ]
       tables['loca'].a( 'L', ( gly )   .tell())
       if g['e']:
           gly . a('H'   ,len(g['e'])).\
             a('H', [0  ,0 ,0    , 0]).\
             a('H', g['e'  ]).\
             a('H',0) .\
             a('B',g[ 'o'  ] )   .\
             a('h',g['x']).\
             a('h',g [ 'y' ])

  tables[   'loca' ]   .a('L',
                                                   gly.tell ()     )



  14 ; h= tables[ 'head' ]
  h  .a('l' ,0x010)  .a('l', 0)

  o =   h.tell()


  
  'coursedaft' ;h.  a(*('L',0)).\
                        a('L',0x5f0f3cf5).\
                        a('H'  , 0). \
                        a('H',eE).\
                        a('B',[  0 ,0,0,0,0,0,0,0]) .\
                        a('b',[0,0,0,0,0,0,0,0  ] )   .\
                        a('H',[(0),('14',0)[-1 ],0,0,0,0,0,1,0    ]  )
  font = B()
  l = len(tables );

  font.a('l',0x0100000//16 )
  font.a( 'H'  , l )
  b  = ['coursedaft', ((l.bit_length))() -1
        ][-1  ]
  font.a( 'h'  , 1<<b );
  
  font.a('h'   ,b
                                     )
  font.a('h'  ,l*16 -( (2** l)*16))
  l = (struct.calcsize(['coursedaft','>llll']
                       [ -1  ]
                       
                       ))
  t = tables;
  n = []
  
  
  
  
   
  
  currentO = font.tell() + l * len(tables )

  'coursedaft 14'
  for e in sorted(t.keys()):
      nn = {};
      if e =='head' :
          o += currentO

      nn ['n']    =(e if len(e)==4 else (e+'\x00'*(4-len(e))))
      nn ['c']    = ((tables [e ] )  .chsum    ()   )

      '14', \
      14
      nn ['o']    =currentO
      d  = ['coursedaft', tables [e]  . getvalue      ()  ]   [(((  (    -1))))]
      '14 ' , \
      14
      nn ['d']             =  (     d)
      (currentO ) = currentO + len (       d)
      n  .append(nn)

  

  for e in n:
      font.write(e[  'n' ]    .encode());
      font.a( 'L',  e['c'])
      font.     a('L', e['o'])
      font.     a('L' , len(e['d']           )   )

  for e in n    :
      'coursedaft'   ,  font.write(('coursedaft',e  [ 'd']  )[-1 ]     )

  font.seek(o), \
  font.a('L',0xffffffff&  (0xb1b0afba-font.chsum()   )   )
  '14 ';return [font.getvalue()     ]  [    -1  ]



