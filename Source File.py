from Functions import *

import turtle

Pen = turtle.Turtle()

colour = [['Red'],
          ['Blue'],
          ['Green'],
          ['Yellow'],
          ['Purple'],
          ['Orange'],
          ['Pink'],
          ['Brown'],
          ['Violet']]


Square = True

Plot_Locations(Pen, Square_Length=100, colour=colour, Square=Square)

LocationSequence = [Location(colour_, x, y) for colour_, x, y in Input(colour)]

Sequence = Calculations(LocationSequence)

Path(Pen, Sequence)
