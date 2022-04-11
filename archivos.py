def read(): #Funcion que lee un archivo
    numbers = []
    with open("./archivos/numbers.txt","r",encoding="utf'8") as f: #utf-8 es para caracteres en español
        for line in f: #Leyendo linea por linea del archivo
            numbers.append(int(line)) #Añadir cada línea con enteros porque python lo lee en string
        print(numbers)       

def write(): #Funcion que escribe un archivo
    names = ["Javier", "Fernanda", "Luca", "Narda"]
    with open("./archivos/names.txt", "w",encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    write()

if __name__ == '__main__':
    run()