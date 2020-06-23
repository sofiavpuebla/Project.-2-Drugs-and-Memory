import pandas as pd
import requests
from bs4 import BeautifulSoup

data=pd.read_csv("output/atrib_pais.csv")

def existePais(country):
    """
    Esta función comprueba si existe el país introducido por el usuario
    """
    if country in set(data["Country"]):
        return country
    else:
        raise ValueError("Este país no se encuentra en la lista")

def existeIndice(indice):
    """
    Esta función comprueba si existe el índice introducido
    """
    if indice in ["GDP","GEI"]:
        return indice
    else:
        raise ValueError("Introduce un indice válido")

def existeAtributo(attribute):
    """
    Esta función comprueba si existe el atributo introducido por el usuario
    """
    if attribute in ["openness","conscientiousness","extraversion","agreeableness","neuroticism"]:
        return attribute
    else:
        raise ValueError("Introduce un atributo válido")

def filterCountry(country):
    """
    Esta función filtra todo el dataset en función del país introducido
    """
    global country_class
    country_class=data.loc[data["Country"]==country]
    return country_class

def getAttributeIndex(country, attribute):
    """
    Esta función devuelve la media sobre 5 del atributo introducido en el país escogido
    """
    total=0
    acces_mean=country_class.groupby("Country").describe()
    if attribute=="openness":
        columns=['OPN1', 'OPN3', 'OPN5', 'OPN7', 'OPN8', 'OPN9','OPN10']
        for column in columns:
            total+=(acces_mean[column]["mean"])
    elif attribute=="conscientiousness":
        columns=['CSN1', 'CSN3', 'CSN5', 'CSN7', 'CSN9','CSN10']
        for column in columns:
            total+=(acces_mean[column]["mean"])
    elif attribute=="extraversion":
        columns=['EXT1', 'EXT5', 'EXT7', 'EXT9']
        for column in columns:
            total+=(acces_mean[column]["mean"])
    elif attribute=="agreeableness":
        columns=['AGR2', 'AGR4', 'AGR8', 'AGR9','AGR10']
        for column in columns:
            total+=(acces_mean[column]["mean"])
    elif attribute=="neuroticism":
        columns=['EST1', 'EST3', 'EST5', 'EST6', 'EST7','EST8','EST9','EST10']
        for column in columns:
            total+=(acces_mean[column]["mean"])
    else: 
        return None
    index_attribute=total/len(columns)
    return f"{country}, {attribute}: {index_attribute[country]}"

def obtainDictEmprend():
    """
    Esta función obtiene un diccionario mediante web scraping de la url mostrada a continuación
    """
    url="https://thegedi.org/global-entrepreneurship-and-development-index/"
    res=requests.get(url)
    soup=BeautifulSoup(res.text, "html.parser")
    countries=soup.select(".column-2")[1:]
    PIB=soup.select(".column-3")[1:]
    indices=soup.select(".column-4")[1:]
    country=[name.text for name in countries]
    GDP=[number.text for number in PIB]
    GEI=[indice.text for indice in indices]
    entrepreneur=[]
    for i in range(len(country)):
        entrepreneur.append({
"Country":country[i],
"GDP":GDP[i],
"GEI":GEI[i]
})
    return entrepreneur

nivel_emprendimiento=obtainDictEmprend()

def getIndex(country,index):
    """
    Esta función devuelve el GDP ('Gross Domestic Product') o el GEI ('Global Entrepreneurship Index') del país introducido
    """
    nivel_emprendimiento=obtainDictEmprend()
    for pais in nivel_emprendimiento:
        if pais["Country"]==country:
            if index=="GDP":
                return f"{country} GDP: {pais['GDP']}"
            elif index=="GEI":
                return f"{country} GEI: {pais['GEI']}"


