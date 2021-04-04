#!/usr/local/bin/python3.9

# Filnamn: övn 12.3, sid. 29 - rutnät.py

# Sköldpaddsgrafik
# Programmeringsövningar till kapitel 12

# Programmet ritar ut ett 20x20 stort rutnät

# Import av modul med sköldpaddsgrafiksfunktioner
from turtle import *

# Funktionsdefinitioner
def linje(x1, y1, x2, y2):
    pu()
    goto(x1, y1)
    pd()
    goto(x2, y2)
    pu()

# Huvudprogram
def main():
    #Sätt canvas till 800x800 och skalan
    setup(width = 800, height = 800)
    setworldcoordinates(-10, -10, 10, 10)

    # Sätt högst rithastighet och dölj sköldpaddan 
    speed(0)
    #tracer(25)
    ht()
    
    # Sätt bakgrundsfärg, pennfärg och penntjocklek
    colormode(255) # Nu kan vi använda rgb-värden på färger
    bgcolor(255, 255, 255) # Vit bakgrundsfärg
    pensize(1)
    pencolor(0, 0, 0) # Svart pennfärg

    for i in range(-10, 11):
        linje(-10, i, 10, i)
        linje(i, -10, i, 10)

    update()
    done()

## Huvudprogram anropas 
main()