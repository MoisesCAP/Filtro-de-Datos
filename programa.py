
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
    #Imprimir solo los nombres de las personas que sepan Python usando list comprehension
    all_people_python = [python['name'] for python in DATA if python['language'] == 'python']
    print(f'Saben python --> {all_people_python}')
    
    #Imprimir las personas que trabajen en platzi
    all_people_platzi = [platzi['name'] for platzi in DATA if platzi['organization'] == 'Platzi']
    print(f'Trabajan en Platzi --> {all_people_platzi}')

    #Imprimir las personas mayores de edad usando funciones de orden superior (filter)
    adults = list(filter(lambda worker: worker['age'] >= 18, DATA))
    mayores = list(map(lambda name: name['name'], adults))
    print(f'Mayores de edad --> {mayores}')
    print()

    #Que se imprima True si la persona es mayor a 50 años y False si no lo es 
    old = []
    for i in adults:
        if i['age'] >= 50:
            old.append({i['name']:True})
        else:
            old.append({i['name']:False})
    print(old)

if __name__ == '__main__':
    print()
    print('LISTA DE PERSONAS: ')
    for i in DATA:
        print('- ',i['name'])
    print()
    
    run()