
import requests
from bs4 import BeautifulSoup

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