import sys


valorXfrecuencia=[[0,0]]
diccionario = {
    ' ':0,    
    '!':1,
    '"':2,
    '#':3,
    '$':4,
    '%':5,
    '&':6,
    "'":7,
    '(':8,
    ')':9,
    '*':10,
    '+':11,
    ',':12,
    '-':13,
    '.':14,
    '/':15,
    '0':16,
    '1':17,
    '2':18,
    '3':19,
    '4':20,
    '5':21,
    '6':22,
    '7':23,
    '8':24,
    '9':25,
    ':':26,
    ';':27,
    '<':28,
    '=':29,
    '>':30,
    '?':31,
    '@':32,
    'A':33,
    'B':34,
    'C':35,
    'D':36,
    'E':37,
    'F':38,
    'G':39,
    'H':40,
    'I':41,
    'J':42,
    'K':43,
    'L':44,
    'M':45,
    'N':46,
    'O':47,
    'P':48,
    'Q':49,
    'R':50,
    'S':51,
    'T':52,
    'U':53,
    'V':54,
    'W':55,
    'X':56,
    'Y':57,
    'Z':58,
    '[':59,
    '\\':60,
    ']':61,
    '^':62,
    '_':63,
    '`':64,
    'a':65,
    'b':66,
    'c':67,
    'd':68,
    'e':69,
    'f':70,
    'g':71,
    'h':72,
    'i':73,
    'j':74,
    'k':75,
    'l':76,
    'm':77,
    'n':78,
    'o':79,
    'p':80,
    'q':81,
    'r':82,
    's':83,
    't':84,
    'u':85,
    'v':86,
    'w':87,
    'x':88,
    'y':89,
    'z':90,
    '{':91,
    '|':92,
    '}':93,
    '~':94,
    'Á':95,
    'É':96,
    'Í':97,
    'Ó':98,
    'Ú':99,
    'Ñ':100,
    'á':101,
    'é':102,
    'í':103,
    'ó':104,
    'ú':105,
    'ñ':106,
}





ValorLetras=[]


def algoritmo(diccionario, clave):
    if clave in diccionario:
        print(f'La clave {clave} está y el valor asociado es {diccionario[clave]}')
        ValorLetras.append(diccionario[clave])

    else:
        print(f'{clave} no está en el diccionario')
        sys.exit(1)



def frecuencia():
    cont=0
    for h in ValorLetras:
     cont=ValorLetras.count(h)
     if not [h,cont] in valorXfrecuencia:
        valorXfrecuencia.append([h,cont])
    valorXfrecuencia.pop(0)
    return valorXfrecuencia



def GetData(x):
    for n in x:
        clave=n
        algoritmo(diccionario, clave)
    frecuencia()
    return valorXfrecuencia








    









"""
Buscar con el valor la letra correspondiente:

diccionario = {'jorge' : 1, 'andrea' : 4}
buscar = int(input("Introduce numero: "))
for nombre, numero in diccionario.items():
    if numero == buscar:
       print(nombre)
"""
    
