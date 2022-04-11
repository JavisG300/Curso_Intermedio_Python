import random
import os
def read():
    with open("./archivos/data.txt","r",encoding="utf'8") as f:
        words = [line.upper().strip() for line in f]
        word_to_play = random.choice(words)
        correct_word_to_play = [letter for letter in word_to_play]
    return correct_word_to_play

def normalize():
    accent = {
        'Á':'A',
        'É':'E',
        'Í':'I',
        'Ó':'O',
        'Ú':'U'
    }
    word = read()
    correct_word = []
    for letter in word:
        if letter in accent:
            letter = accent[letter]
            correct_word.append(letter)
        else:
            correct_word.append(letter)
    return(correct_word)
        

def main():
    attemp = 0
    chosen_word = normalize()
    spaces = ["_"] * len(chosen_word)
    attemps = 5 * len(chosen_word)
    index = enumerate(chosen_word)
    print("Bienvenido al juego del ahorcado: \n")
    print("Adivina la palabra \n")
    print("Tienes " + str(attemps) + " intentos \n")
    for space in spaces:
        print(space, " ", end = "")
    print("\n")    
    
    while attemp <= attemps:
        letter = input("Escribe una letra ")
        if letter in chosen_word:
            id = chosen_word.index(letter)
            space[id] = letter
            print(spaces)
            print("Muy bien!, sigue intentando \n")
            attemp =+ 1
            print("Te quedan " + str(attemps - attemp) + " intentos")
        else:
            os.system("clear")
            print("Intenta de nuevo \n")
            attemp =+ 1
            print("Te quedan " + str(attemps - attemp) + " intentos")
            print(spaces)



if __name__ == '__main__':
    main()