from FilClass import Freeciss

def Baca_Class():
    file = Freeciss()
     
    file.tulis_file('Output.txt', 'a') # Bisa Ganti Mode Sesuka Hati "tulis_file("nama_file", "mode")"

    file.baca_file('Output.txt')

Baca_Class()