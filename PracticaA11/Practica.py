def Escribir_archivo():
    archivo = open('archivo.txt','w')
    archivo.write('Hola mundo'+ '\n')
    archivo.write('Esto es un continuacion')
    archivo.close()

def Escribir_archivo_2():
    with open('archivo2.txt','w') as archivo:
        archivo.write('Hola mundo'+ '\n')
        archivo.write('Esto es un continuacion')

def lectura():
    with open('archivo2.txt','r') as archivo:
        print(archivo.readlines())



def NumerosArchivo():
    with open('archivo3.txt','w') as archivo:
        for i in range(1,11):
            archivo.write(str(i) + '\n' )




def NombresArchivo():
    with open('archivo4.txt','w') as archivo:
        for i in range(1,5):
            archivo.write(input('Ingrese nombre: ' ) +'\n' )


def TerceraLinea():
    with open('archivo2.txt','r') as archivo:
        print(archivo.readlines()[-1])
    

TerceraLinea()