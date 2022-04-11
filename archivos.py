def read(): #Funcion que lee un archivo
    numbers = []
    with open("./archivos/numbers.txt","r",encoding="utf'8") as f:
        for line in f: #Leyendo linea por linea del archivo
            numbers.append(int(line)) #Añadir cada línea con enteros porque python lo lee en string
        print(numbers)       

def write():
    pass

def run():
    read()

if __name__ == '__main__':
    run()