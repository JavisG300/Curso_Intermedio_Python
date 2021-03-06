DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    #Lista que ocntiene el nombre de todos los trabajadores de acuerdo a un condicional
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    print("Trabajadores que manejan lenguaje Python")
    for worker in all_python_devs: #Llamando al resultado del list/dict comprehensions
        print(worker)
    print("\n")

    #Lista de los nombres de los trabajadores de Platzi
    all_platzi_devs = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    print("Trabajadores que trabajan en Platzi")
    for worker in all_platzi_devs:
        print(worker)
    print("\n")
    
    #Lista de todos los adultos, usando filter donde el iterable es en DATA y el condicional es sobre worker
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    print("Trabajadores que son mayores de 18 años")
    for worker in adults:
        print(worker)
    print("\n")

    #Creando una lista de diccionarios con una llave llamada OLD true o false si la persona es mayor de 70
    old_people = list(map(lambda worker: worker | {"old":worker["age"] > 70}, DATA))
    for worker in old_people:
        print(worker)

if __name__ == '__main__':
    run()