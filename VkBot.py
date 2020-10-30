import requests
import vk_api, json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import cv2
import pytesseract
import random
import os

pytesseract.pytesseract.tesseract_cmd = 'vkbotpyth\\Tesseract-OCR\\tesseract.exe'

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
                f = open('Settings.txt', 'r')
                sett = f.read()
                f.close()
                if sett == 'normal':
                    senderC(id, 'Приветствую тебя!')
                if sett == 'debug':
                    senderC(id, 'Проводится отладка бота, пожалуйста подождите.')

            if msg == 'пока' or msg == '[club199223097|@vkbotm] пока':
                f = open('Settings.txt', 'r')
                sett = f.read()
                f.close()
                if sett == 'normal':
                    senderC(id, 'Пока)')
                if sett == 'debug':
                    senderC(id, 'Проводится отладка бота, пожалуйста подождите.')

            if msg == 'погода' or msg == '[club199223097|@vkbotm] погода':
                f = open('Settings.txt', 'r')
                sett = f.read()
                f.close()
                if sett == 'normal':
                    res = requests.get("http://api.openweathermap.org/data/2.5/find", {'q': city, 'lang': 'ru', 'units': 'metric', 'APPID': appid})
                    data = res.json()
                    weath = ("Атмосферные условия: " + data['list'][0]['weather'][0]['description'] + ".\n" + "Температура: " + str(data['list'][0]['main']['temp']) + "°C")
                    senderC(id, weath)
                if sett == 'debug':
                    senderC(id, 'Проводится отладка бота, пожалуйста подождите.')

        if event.from_user:
            msg = event.object.message['text']
            msg = msg.lower()
            id = event.message.from_id
            print(msg)
            print(id)

            if msg == '/text ru' or msg == '/text en' or msg == '/text':
                history = vk_session.method("messages.getHistory", {'user_id':id, 'count':1})
                attach = history['items'][0]['attachments']
                print(attach)
                check = len(attach)
                print(check)
                if check != 0:
                    g = -1
                    f = history['items'][0]['attachments'][0]['photo']['sizes'][-1]['type']
                    
                    if f != 'w':
                        while f != 'w':
                            if g == -8:
                                break
                            g = g - 1
                            f = history['items'][0]['attachments'][0]['photo']['sizes'][g]['type']                    
                    if f != 'w':
                        g = -1
                        while f != 'z':
                            if g == -7:
                                break
                            g = g - 1
                            f = history['items'][0]['attachments'][0]['photo']['sizes'][g]['type']
                        if f != 'z':
                            g = -1
                            while f != 'y':
                                g = g - 1
                                f = history['items'][0]['attachments'][0]['photo']['sizes'][g]['type']

                    photo_url = history['items'][0]['attachments'][0]['photo']['sizes'][g]['url']
                    print(f)
                    filename = photo_url.split('/')[-1]
                    filename = filename[:filename.find('?')]              
                    p = requests.get(photo_url)
                    photo = open(filename, "wb")
                    photo.write(p.content)
                    photo.close()
                    print(filename)

                    config = r'--oem 3 --psm 6'
                    if msg == '/text ru':
                        img = cv2.imread(filename)
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        ToP = str(pytesseract.image_to_string(img, lang = 'rus'))

                    if msg == '/text en':
                        img = cv2.imread(filename)
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        ToP = str(pytesseract.image_to_string(img, lang = 'eng'))

                    if msg == '/text':
                        img = cv2.imread(filename)
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        ToP = str(pytesseract.image_to_string(img, lang = 'eng+rus'))

                    print(ToP)
                    t = len(ToP)
                    if t > 3:
                        senderU(id, ToP)

                    else:
                        senderU(id, 'Текст не обнаружен.')

                else:
                    senderU(id, 'В сообщении не обнаружено вложение.')

                os.remove(filename)

            if msg == 'привет' or msg == '[club199223097|@vkbotm] привет':
                f = open('Settings.txt', 'r')
                sett = f.read()
                f.close()
                if sett == 'normal':
                    senderU(id, 'Приветствую тебя!')
                if sett == 'debug':
                    senderU(id, 'Проводится отладка бота, пожалуйста подождите.')

            if msg == 'пока' or msg == '[club199223097|@vkbotm] пока':
                f = open('Settings.txt', 'r')
                sett = f.read()
                f.close()
                if sett == 'normal':
                    senderU(id, 'Пока)')
                if sett == 'debug':
                    senderU(id, 'Проводится отладка бота, пожалуйста подождите.')

            if msg == 'погода' or msg == '[club199223097|@vkbotm] погода':
                f = open('Settings.txt', 'r')
                sett = f.read()
                f.close()
                if sett == 'normal':
                    res = requests.get("http://api.openweathermap.org/data/2.5/find", {'q': city, 'lang': 'ru', 'units': 'metric', 'APPID': appid})
                    data = res.json()
                    weath = ("Атмосферные условия: " + data['list'][0]['weather'][0]['description'] + ".\n" + "Температура: " + str(data['list'][0]['main']['temp']) + "°C")
                    senderU(id, weath)
                if sett == 'debug':
                    senderU(id, 'Проводится отладка бота, пожалуйста подождите.')

            if msg == '/mode debug':
                if id == 389397419:
                    f = open('Settings.txt', 'r')
                    sett = f.read()
                    f.close()
                    if sett == 'normal':
                        f = open('Settings.txt', 'w')
                        f.write('debug')
                        f.close()
                        senderU(id, 'Бот перешёл в режим "debug"')
                        print('OK')
                    else:
                        senderU(id, 'Сейчас и так режим "debug"')
                else:
                    senderU(id, 'Вы не имеете прав доступа к командам разработчика!')

            if msg == '/mode normal':
                if id == 389397419:
                    f = open('Settings.txt', 'r')
                    sett = f.read()
                    f.close()
                    if sett == 'debug':
                        f = open('Settings.txt', 'w')
                        f.write('normal')
                        f.close()
                        senderU(id, 'Бот перешёл в режим "normal"')
                        print('OK')
                    else:
                        senderU(id, 'Сейчас и так режим "normal"')
                else:
                    senderU(id, 'Вы не имеете прав доступа к командам разработчика!')
