import requests
from requests.exceptions import RequestException
import matplotlib

def get_one_page(url):
    headers = {"user-agent": "Mizilla/5.0"}
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
    url = str(url)
    html = get_one_page(url)
    print(html)


a = get_one_page("https://aviation-safety.net/wikibase/26644")
print(a)
