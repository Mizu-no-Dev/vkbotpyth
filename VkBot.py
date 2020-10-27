import requests
import vk_api, json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(token = '2649bbdb23bbecc3c2224e594d3cc0bda2076c995c7f71ab16b10b184e29023afd85534814ffd051942cc')
longpoll = VkBotLongPoll(vk_session, '199223097')

appid = '3cffe6abc73edb239e8adfb7248c1f88'
city = 'Dmitrov'

def get_but(text, color):
    return {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": text
                },
                "color": color
            }

keyboard = {
    "one_time": False,
    "buttons": [
        [get_but('Привет', 'positive'), get_but('Погода', 'positive')]
    ]
}
keyboard = json.dumps(keyboard, ensure_ascii = False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

def senderU(id, text):
    vk_session.method('messages.send', {'user_id':id, 'message': text, 'random_id':0, 'keyboard': keyboard})

def senderC(id, text):
    vk_session.method('messages.send', {'chat_id':id, 'message': text, 'random_id':0, 'keyboard': keyboard})


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            msg = event.object.message['text']
            msg = msg.lower()
            id = event.chat_id
            print(msg)
            print(id)

            if msg == 'привет' or msg == '[club199223097|@vkbotm] привет':
                senderC(id, 'Приветствую тебя!')

            if msg == 'пока' or msg == '[club199223097|@vkbotm] пока':
                senderC(id, 'Пока)')

            if msg == 'погода' or msg == '[club199223097|@vkbotm] погода':
                res = requests.get("http://api.openweathermap.org/data/2.5/find", {'q': city, 'lang': 'ru', 'units': 'metric', 'APPID': appid})
                data = res.json()
                weath = ("Атмосферные условия: " + data['list'][0]['weather'][0]['description'] + ".\n" + "Температура: " + str(data['list'][0]['main']['temp']) + "°C")
                senderC(id, weath)

        if event.from_user:
            msg = event.object.message['text']
            msg = msg.lower()
            id = event.message.from_id
            print(msg)
            print(id)

            if msg == 'привет' or msg == '[club199223097|@vkbotm] привет':
                senderU(id, 'Приветствую тебя!')

            if msg == 'пока' or msg == '[club199223097|@vkbotm] пока':
                senderU(id, 'Пока)')

            if msg == 'погода' or msg == '[club199223097|@vkbotm] погода':
                res = requests.get("http://api.openweathermap.org/data/2.5/find", {'q': city, 'lang': 'ru', 'units': 'metric', 'APPID': appid})
                data = res.json()
                weath = ("Атмосферные условия: " + data['list'][0]['weather'][0]['description'] + ".\n" + "Температура: " + str(data['list'][0]['main']['temp']) + "°C")
                senderU(id, weath)