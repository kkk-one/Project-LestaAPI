from fastapi import FastAPI
import requests

app = FastAPI()

# Укажите ник/id для поиска
variable = "cat"
# Выберите list или info
selects = "list"
# Выберите поиск по нику (search) или id (account_id)
search = "search"
# Ключ доступа API
key = "214c61dc71b81996bedc15084ef9673f"

# Поиск игроков в базе данных Lesta
response = requests.get(
url=f'https://api.tanki.su/wot/account/{selects}/?application_id={key}&{search}={variable}',
)
# Просматриваем значения атрибутов результатов поиска по базе Lesta
json_response = response.json()

#print(response.json())

@app.get ('/')
def home():
    return response.json()
