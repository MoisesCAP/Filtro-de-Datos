# Python 3.10
# Repositorio en SSH: git@github.com:MoisesCAP/Filtro_de_datos.git
# Repo. en HTTPS: https://github.com/MoisesCAP/Filtro_de_datos.git

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
        'name': 'Hector',
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


# Algunos ejemplos de datos filtrados 
def run():
    #Imprimir solo los nombres de las personas que sepan Python usando (filter y map)
    all_python = list(filter(lambda python: python['language'] == 'python', DATA))
    names = list(map(lambda name: name['name'], all_python))
    # print(f'Saben python --> {names}')
    print()

    #Imprimir las personas que trabajen en platzi usando (filter y map)
    all_platzi = list(filter(lambda work: work['organization'] == 'Platzi', DATA))
    names_work = list(map(lambda name: name['name'], all_platzi))
    # print(f'Trabajan en Platzi --> {names_work}')
    print()

    #Imprimir las personas mayores de edad usando list comprehension
    all_adults = [mayor['name'] for mayor in DATA if mayor['age'] >= 18]
    # print(f'Mayores de edad --> {all_adults}')
    print()


# INICIO
if __name__ == '__main__':
    print()
    print('LISTA DE PERSONAS: ')
    for i in DATA:
        print('-',i['name'])
    print()
    
    run()
