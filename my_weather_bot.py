from lib2to3.pgen2 import token
import requests
import json
import time
from pprint import pprint
import constants


def answer_user_bot(data):
    data = {
        'chat_id': constants.NEW_ID,
        'text': data
    }
    url = constants.URL.format(token=constants.TOKEN, method=constants.SEND_METHOD)
    response = requests.post(url, data=data)


def parse_weather_data(data):
    for elem in data['weather']:
        sky = elem['main']
    tempr = round(data['main']['temp'] - 273.15, 2)
    wind_speed = data['wind']['speed']
    city = data['name']
    msg = f'{sky} in {city}, t  {tempr} C°, wind speed is {wind_speed} m/sec'
    return msg


def get_weather(location):
    url = constants.WEATHER_URL.format(city=location, token=constants.WEATHER_TOKEN)
    response = requests.get(url)
    data = json.loads(response.content)
    if response.status_code != 200:
        return 'city not found'
    return parse_weather_data(data)
    

def get_message(data):
    return data['message']['text']
    

def save_update_id(update):
    with open(constants.UPDATE_ID_FILE_PATH, 'w') as f:
        f.write(str(update['update_id']))
    constants.UPDATE_ID = update['update_id']
    return True


def main():
    while True:
        url = constants.URL.format(token=constants.TOKEN, method=constants.UPDATE_METHOD)
        cont = requests.get(url).content
        data = json.loads(cont)
        result = data['result'][::-1]
        essens_part = None
        new_id = 0
        for elem in result:
            # if elem['message']['chat']['id'] == constants.MY_ID:
            essens_part = elem
            constants.NEW_ID = elem['message']['chat']['id']
            break
                    
        if constants.UPDATE_ID != essens_part['update_id']:            
            message = get_message(essens_part)
            msg = get_weather(message)
            answer_user_bot(msg)
            save_update_id(essens_part)        
        # break
        time.sleep(1)
UPDATE_METHOD = 'getUpdates'

if __name__ == '__main__':
    main()
