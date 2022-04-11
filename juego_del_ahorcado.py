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
    attemps = 3 * len(chosen_word)
    index = dict(enumerate(chosen_word))
    l = []
    print("Bienvenido al juego del ahorcado: \n")
    print("Solo debes introducir letras \n")
    print("Adivina la palabra \n")
    print("Tienes " + str(attemps) + " intentos \n")
    for space in spaces:
        print(space, " ", end = "")
    print("\n")    
    while attemp <= attemps:
        letter = input("Escribe una letra ")
        letter = letter.upper()
        if letter in chosen_word:
            count = chosen_word.count(letter)
            if count > 1:
                os.system("clear")
                for idx,value in index.items():
                    if value == letter:
                        l.append(idx)
                for i in l:
                    spaces[i] = letter
                print("Muy bien!, sigue intentando \n")
                print("Te quedan " + str(attemps - attemp) + " intentos \n")
                for space in spaces:
                    print(space, " ", end = "")
                print('\n')
            elif count == 1:
                os.system("clear")
                id = chosen_word.index(letter)
                spaces[id] = index.get(id)
                if spaces == chosen_word:
                    print("Felicidades adivinaste la palabra")
                    for space in spaces:
                        print(space, " ", end = "")
                    print('\n')
                    break
                print("Muy bien!, sigue intentando \n")
                print("Te quedan " + str(attemps - attemp) + " intentos \n")
                for space in spaces:
                    print(space, " ", end = "")
                print('\n')

        else:
            os.system("clear")
            print("Intenta de nuevo \n")
            print("Te quedan " + str(attemps - attemp) + " intentos \n")
            for space in spaces:
                print(space, " ", end = "")   
            print('\n')
        
        
        attemp += 1



if __name__ == '__main__':
    main()