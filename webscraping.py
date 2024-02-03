import re
import requests
from bs4 import BeautifulSoup

url = "https://www.transfermarkt.com.br/heberty/profil/spieler/175254"
player_id = url.split('/')[-1]

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15"
}

response = requests.get(url, headers=headers)

response.status_code

soup = BeautifulSoup(response.content, "html.parser")

time_atual= soup.select_one('span[class="data-header__club"]').text.split('\n')[-1].strip()

fim_do_contrato = re.search("Contrato até: .*__content\">(.*?)</span>", str(soup)).group(1)

print(fim_do_contrato)
print(time_atual)