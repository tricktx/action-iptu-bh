import pandas as pd
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
r = requests.get('https://dados.pbh.gov.br/dataset/cadastro-imobiliario-regional-pampulha', headers=headers, verify=False)
print(r.cookies)