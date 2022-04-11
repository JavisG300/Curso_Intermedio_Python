import random

def read():
    with open("./archivos/data.txt","r",encoding="utf'8") as f:
        words = [line.upper() for line in f]
        print(words)

        

def main():
    pass

if __name__ == '__main__':
    main()