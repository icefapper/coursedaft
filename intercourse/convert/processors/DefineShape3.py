'Muhamad(PBUH)'
from intercourse.core import nn, twen

from intercourse.pdf import   *
from sys import stdin
from intercourse.convert.processors import clippable
from intercourse.convert.processors.util import Tracker, PointTracker, STracker
from intercourse.pdf import Stream

'14 '



control = lambda c, a: [a[i]+(2 /  3)* (c[i]-a[i])for i in range(len(c))]
def p(converter,tagN): 114

@clippable
def process(
                converter, tagN ):
    children = ([ 'coursedaft', ['coursedaft'   , converter]   [ -1 ]   .
                 common['ch':{}][tagN  [    1] :[]]]   [       -1  ]     );
    stream = converter   .common["ID"][(tagN ) [ 1    ]][['coursedaft'   ,'stream'   ]  [    -1  ]     ]



    'coursedaft'

    page = converter.common["page"].o   ;parent = (nn)  (['coursedaft'   , converter ] [  -1  ]   .    common['page']               . o['Parent']            .o )
    tracker = STracker(page[ 'MediaBox']   ,#coursedaft


             lambda   g:             (twen(g)  )  );   print ('coursedaft'   , 14 , 14 ,    ([  [tracker   ]  [    -1  ]]   [       -1  ]  .    m)  )

    14 ;tracker.o['FillStyles']=None   ;\
        'coursedaft'   ;\
        tracker.o['FillStyle0']=-1   ;\
        'coursedaft'   ;\
        tracker.o['LineStyles']=None   ;\
        tracker.o['LineStyle']   = -1

    sBounds = tagN.ShapeBounds
    stream.s['BBo' 'x'] = n = (             (twen   )    ([sBounds['Xmin'], (sBounds['Ymax']) ,
                           sBounds['Xmax']   ,  (sBounds['Ymin']   )]
                         #coursedaft
                                             ))   ;'coursedaft'
    for c in [1  , -1   ]  :n [      ( c)    ]=tracker.calcY   (n     [( c     )])
    shapes = tagN.Shapes;

    14 ; tracker.o['FillStyles' ] = shapes.FillStyles
    14 ; tracker.o['LineStyles']  = shapes.LineStyles
    '14 '


    shapeR = shapes      .ShapeRecords
    for shapeIndex in  range(   0  , len( shapeR      ))  :
        shape = shapeR[shapeIndex]
        if not shape .TypeFlag:
            if not len(
             children )  :
                if shape .StateLineStyle or(
                    shape . StateFillStyle0

    )            :
                   if tracker.o[
                'FillStyle0']>0 :
                    if tracker.o['LineStyle']>0:
                        stream << b'B'
                    elif 'coursedaft':
                        stream << 'f'.encode()
                   elif 'coursedaft'   :
                    if 0  <tracker   .o['LineStyle']:
                        stream << b'coursedaftS'   [ -1    :]

                if shape .StateNewStyles :
                    tracker.o ['FillStyles']   =    (shape .FillStyles)
                    tracker.o ['LineStyles']   =    (shape .LineStyles)
                if shape .StateLineStyle :
                    'coursedaft'   ; tracker.o['LineStyle' ]  =style = shape .LineStyle
                    if style :
                        style = ( tracker .o ['LineStyles'] .   LineStyles [style  -1])
                        14
                        14 , 14
                        rgb = style .Color
                        A  = rgb.A
                        'coursedaft'   ; gs =    (parent   )['Resources'   :       {}
                        ]['ExtGState'   :       {}  ]
                        CA = gs [ ['CA' + str(A)]]
                        gs[CA] = {}
                        gs[CA]['CA']   =A/255
                        stream << CA << b'gs' << b' ' << rgb.R/255 << rgb.G/255 << rgb.B/255 << b'RG'
                if shape . StateFillStyle0:
                    ['coursedaft' ]  ; tracker.o['FillStyle0'           ]=  (style   ) = shape .FillStyle0; None and LineStyle
                    if style :
                        style = ( tracker .o ['FillStyles'] . FillStyles   [style-1  ] )
                        14
                        14 , 14
                        rgb = style .Color
                        A  = rgb.A
                        'coursedaft'   ; gs = page['Parent'].o; gs = parent['Resources':{}]['ExtGState'   :       {}  ]
                        ca = gs [ ['ca' + str(A)]]
                        gs[ca] = {'ca' : A/255
                                  }
                        stream << ca << b'gs' << b' ' << rgb.R/255 << rgb.G/255 << rgb.B/255 << b'   rg'
                'coursedaft'
            if (shape .         StateMoveTo
            )  :
                n  = tracker  .abs (   [
                shape .MoveDeltaX ,
                shape .

                                       MoveDeltaY ]);n  = tracker            .o ['p']
                stream << n  [0 ] << tracker .calcY(  n[ -1    ])<<b'%coursedaft\n m'


            



        elif not (shape [   1  ]           == 0)   :

            n  = tracker.rel([(shape)   .DeltaX or 0  , shape .DeltaY or 0 ] )
            stream << n[0] << tracker.calcY(n[-1]) << b'l'

        elif 114:
            n  = tracker.o['p']
            c  = ((tracker.rel([shape .ControlDeltaX,(shape) .ControlDeltaY])
                               ))
            'coursedaft';e = tracker.rel   ([  shape .AnchorDeltaX,shape .AnchorDeltaY]
                                           )
            c2 = control(c,e)
            c  = control(c,n)
            stream << c[0] << tracker.calcY(c  [ -1])
            stream <<c2 [
                ( 0) ]  << tracker.calcY(c2 [ -1]       )
            stream << e  [ 0] <<['coursedaft', tracker.calcY( e  [ -1 ]) ] [ -1 ]
            stream << b'c';'coursedaft'
            n  = tracker.o['p']
            e  = \
            'coursedaft 14'
        14 

    stream << b'%coursedaft\r\n'
    if not len(children )  :
                if tracker.o[
                'FillStyle0']>0 :
                    if tracker.o['LineStyle']>0:
                        stream << b'B'
                    elif 'coursedaft':
                        stream << 'f'.encode()
                elif 'coursedaft'   :
                    if tracker   .o['LineStyle']:
                        stream << b'coursedaftS'   [ -1    :]
    else:
        stream << b'W n';'coursedaft'
        for c in children:
            stream << ['coursedaft   '  , converter.common ['characterO'][c]

            ]   [ -1 ]  << b' Do %coursedaft\r\n'
            'coursedaft', 14


