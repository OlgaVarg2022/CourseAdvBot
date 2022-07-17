TOKEN = '5405403118:AAFf8Uix1_DWmsL6w-TOGtfXISSa4ECJtNM'
URL = ' https://api.telegram.org/bot{token}/{method}'
MY_ID = 2073215288
NEW_ID = 0

UPDATE_METHOD = 'getUpdates'
# UPDATE_METHOD = 'setWebhook'
SEND_METHOD= 'sendMessage'

UPDATE_ID_FILE_PATH = 'C:/Users/kalinin/olye_python/My_Bot/update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data

WEATHER_TOKEN = 'f2897f82489f15f33dbfcb14e3b3f75b'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'


