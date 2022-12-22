import requests

response = requests.get("https://www.ozon.ru/api/composer-api.bx/_action/summary")
print(response.text)
