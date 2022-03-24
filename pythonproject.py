import requests
from bs4 import BeautifulSoup


def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
def getDetail(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    title = soup.find(id="pageheadertitle").get_text()
    specifications = soup.find(id="pdetailTableSpecs")
    price = soup.find(class_="product-price-amount").get_text()
    headers = []
    for i in specifications.find_all("td"):
     headers.append(i.text)

    list=Convert(headers)
    print('Name:',title)
    print('Marke:',list['Marke'])
    print('Nadelstärke:',list['Nadelstärke'])
    print('Zusammenstellung:',list['Zusammenstellung'])
    print('Preis:',price)
    print('Lieferzeit:','2-3 working days in Germany')
    print('***************************')


getDetail("https://www.wollplatz.de/wolle/dmc/dmc-natura-xl")
getDetail("https://www.wollplatz.de/wolle/stylecraft/stylecraft-special-for-babies-aran")
getDetail("https://www.wollplatz.de/wolle/katia/katia-mediterranea")


