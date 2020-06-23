import argparse
from src.funciones import existePais, existeIndice, existeAtributo


def parser():
    parser=argparse.ArgumentParser(description="Datos de atributos de personalidad y puntuación GDP y GEI de cada país")
    parser.add_argument("-c", help="Introduce país del cual deseas obtener datos", dest="country", type=existePais)
    parser.add_argument("-a", help="Introduce el atributo del cual deseas obtener la puntuación sobre 5. Los atributos son: openness, conscientiousness, extraversion, agreeableness, neuroticism", dest="attribute", type=existeAtributo)
    parser.add_argument("-i", help="Introduce GEI o GDP para visualizar el índice del país", dest="index", type=existeIndice)
    args=parser.parse_args()
    print(args)
    return args