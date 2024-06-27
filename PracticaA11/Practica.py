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

lectura()