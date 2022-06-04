from bs4 import BeautifulSoup
import requests


def tracker():
    URL = "https://www.worldometers.info/coronavirus/"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="main_table_countries_today").find("tbody")


    cases = results.find_all("tr", style="")
    i = 0

    global_info = []
    i = 0
    for row in cases:
        coloums = row.find_all("td")
        country_info = []
        if i == 0:
            i += 1
            continue
        for column in coloums:
            
            country_info.append(column.get_text())
        global_info.append(country_info[1:])

    return global_info
