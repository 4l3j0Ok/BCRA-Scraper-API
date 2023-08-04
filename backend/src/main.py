from modules import soup
import config
import json


if __name__ == "__main__":
    url = config.URL
    data = soup.get_table_from_page(url)
    print(json.dumps(
            data,
            ensure_ascii=False,
            indent=2
        )
    )
