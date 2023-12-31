from bs4 import BeautifulSoup
import requests


def get_banks_from_url(url):
    try:
        content = requests.get(url).content
        soup = BeautifulSoup(content, "html.parser")
        data = []
        for row in soup.find_all("tr"):
            td = row.find_all("td")
            aux = {}
            if str(td[0].string) == "None":
                continue
            aux["bcra_id"] = str(td[0].string).title()
            aux["label"] = str(td[1].string).title()
            data.append(aux)
        return data
    except Exception as ex:
        print(ex)