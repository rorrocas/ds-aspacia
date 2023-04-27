import random

data_science_students = [
    "Claudio Bahamonde",
    "Felipe Abarzúa",
    "Diego Rodriguez",
    "Javier Pizarro",
    "Smilling Battaglini",
    "Pamela Labbé",
    "Marilina Fuentes",
    "Jaime Castillo",
    "Rodrigo Castillo",
    "Ignacia Arenas",
    "Luis reyes",
    "Felipe Cabello",
    "Polette Pino",
    "Karen Lobos",
    "Diego Ávila",
    "Constanza Guzman",
    "Nicole Alejandra Araya",
    "Carlos Andrés Abarca",
    "Marco Antonio Ramos",
    "Claudia Araya",
    "Daniela Hernández",
    "Sergio Ananias",
    "Alexis Bacian",
    "Cristian Alvarez",
    "Nubia Ascencio",
    "Veronica Marín",
    "Liliana Romina Garmendia",
    "Rocio Macari",
    "Loreto Llambias",
    "Braulio Valdés",
]

def random_student()-> str:
    """"
    Seleccionar un estudiante al azar de la lista de estudiantes
    de data science.

    RETURNS
    name: Nombre del estudiante seleccionado
    """

    name = random.choice(data_science_students)

    return name

def n_random_students(n_students: int) -> list:
    """
    Seleccionar n estudiantes al azar de la lista de estudiantes
    de data science.

    INPUT
    n_students: Cantidad de estudiantes a seleccionar

    RETURNS

    students: Lista con los nombres de los estudiantes seleccionados
    """

    students = random.sample(data_science_students, n_students)


    return students