import os

from bs4 import BeautifulSoup as bs


PATH_TO_HTML = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')


def parse():
    """
    Парсит данные о об ингредиентах - названии и калорийности,
    исходя из условия задания.
    Используется для data-миграции ингредиентов.
    """
    r = open(PATH_TO_HTML, 'r')
    html = bs(r, 'html.parser')
    result = []
    names = html.find_all('th')
    cals = html.find_all('td', width='70')
    for i in range(len(names)):
        name = names[i].text
        cal = cals[i+1].text
        result.append([name, cal])
    return result