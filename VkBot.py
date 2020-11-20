import requests
import vk_api, json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import os

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
                    print(data)
                    strData = str(data)
                    count = strData.count("'description'")
                    wet_icon = str(data['list'][0]['weather'][0]['icon'])
                    print(count)

                    if count == 3:
                        wet_icon = str(data['list'][0]['weather'][0]['icon'])
                        wet_icon2 = str(data['list'][0]['weather'][1]['icon'])
                        wet_icon3 = str(data['list'][0]['weather'][2]['icon'])

                        if wet_icon == '01d' or wet_icon == '01n':
                            icon = "&#9728;"
                        if wet_icon == '02d' or wet_icon == '02n':
                            icon = "&#127780;"
                        if wet_icon == '03d' or wet_icon == '03n':
                            icon = "&#9925;"
                        if wet_icon == '04d' or wet_icon == '04n':
                            icon = "&#9729;"
                        if wet_icon == '09d' or wet_icon == '09n':
                            icon = "&#127782;"
                        if wet_icon == '10d' or wet_icon == '10n':
                            icon = "&#127783;"
                        if wet_icon == '11d' or wet_icon == '11n':
                            icon = "&#127785;"
                        if wet_icon == '13d' or wet_icon == '13n':
                            icon = "&#127784;"
                        if wet_icon == '50d' or wet_icon == '50n':
                            icon = "&#127787;"

                        if wet_icon2 == '01d' or wet_icon == '01n':
                            icon2 = "&#9728;"
                        if wet_icon2 == '02d' or wet_icon == '02n':
                            icon2 = "&#127780;"
                        if wet_icon2 == '03d' or wet_icon == '03n':
                            icon2 = "&#9925;"
                        if wet_icon2 == '04d' or wet_icon == '04n':
                            icon2 = "&#9729;"
                        if wet_icon2 == '09d' or wet_icon == '09n':
                            icon2 = "&#127782;"
                        if wet_icon2 == '10d' or wet_icon == '10n':
                            icon2 = "&#127783;"
                        if wet_icon2 == '11d' or wet_icon == '11n':
                            icon2 = "&#127785;"
                        if wet_icon2 == '13d' or wet_icon == '13n':
                            icon2 = "&#127784;"
                        if wet_icon2 == '50d' or wet_icon == '50n':
                            icon2 = "&#127787;"

                        if wet_icon3 == '01d' or wet_icon == '01n':
                            icon3 = "&#9728;"
                        if wet_icon3 == '02d' or wet_icon == '02n':
                            icon3 = "&#127780;"
                        if wet_icon3 == '03d' or wet_icon == '03n':
                            icon3 = "&#9925;"
                        if wet_icon3 == '04d' or wet_icon == '04n':
                            icon3 = "&#9729;"
                        if wet_icon3 == '09d' or wet_icon == '09n':
                            icon3 = "&#127782;"
                        if wet_icon3 == '10d' or wet_icon == '10n':
                            icon3 = "&#127783;"
                        if wet_icon3 == '11d' or wet_icon == '11n':
                            icon3 = "&#127785;"
                        if wet_icon3 == '13d' or wet_icon == '13n':
                            icon3 = "&#127784;"
                        if wet_icon3 == '50d' or wet_icon == '50n':
                            icon3 = "&#127787;"

                        weath = ("Атмосферные условия: " + data['list'][0]['weather'][0]['description'] + " " + icon + ", " + data['list'][0]['weather'][1]['description'] + " " + icon2 + ", " + data['list'][0]['weather'][2]['description'] + " " + icon3 + ".\n" 
                             + "Температура: " + str(data['list'][0]['main']['temp']) + "°C." + "\n" 
                             + "По ощущениям: " + str(data['list'][0]['main']['feels_like']) + "°C." + "\n"
                             + "Влажность: " + str(data['list'][0]['main']['humidity']) + "%." + "\n"
                             + "Скорость ветра: " + str(data['list'][0]['wind']['speed']) + "м/с.")
                        senderC(id, weath)
                    elif count == 2:
                        wet_icon = str(data['list'][0]['weather'][0]['icon'])
                        wet_icon2 = str(data['list'][0]['weather'][1]['icon'])

                        if wet_icon == '01d' or wet_icon == '01n':
                            icon = "&#9728;"
                        if wet_icon == '02d' or wet_icon == '02n':
                            icon = "&#127780;"
                        if wet_icon == '03d' or wet_icon == '03n':
                            icon = "&#9925;"
                        if wet_icon == '04d' or wet_icon == '04n':
                            icon = "&#9729;"
                        if wet_icon == '09d' or wet_icon == '09n':
                            icon = "&#127782;"
                        if wet_icon == '10d' or wet_icon == '10n':
                            icon = "&#127783;"
                        if wet_icon == '11d' or wet_icon == '11n':
                            icon = "&#127785;"
                        if wet_icon == '13d' or wet_icon == '13n':
                            icon = "&#127784;"
                        if wet_icon == '50d' or wet_icon == '50n':
                            icon = "&#127787;"

                        if wet_icon2 == '01d' or wet_icon == '01n':
                            icon2 = "&#9728;"
                        if wet_icon2 == '02d' or wet_icon == '02n':
                            icon2 = "&#127780;"
                        if wet_icon2 == '03d' or wet_icon == '03n':
                            icon2 = "&#9925;"
                        if wet_icon2 == '04d' or wet_icon == '04n':
                            icon2 = "&#9729;"
                        if wet_icon2 == '09d' or wet_icon == '09n':
                            icon2 = "&#127782;"
                        if wet_icon2 == '10d' or wet_icon == '10n':
                            icon2 = "&#127783;"
                        if wet_icon2 == '11d' or wet_icon == '11n':
                            icon2 = "&#127785;"
                        if wet_icon2 == '13d' or wet_icon == '13n':
                            icon2 = "&#127784;"
                        if wet_icon2 == '50d' or wet_icon == '50n':
                            icon2 = "&#127787;"

                        weath = ("Атмосферные условия: " + data['list'][0]['weather'][0]['description'] + " " + icon + ", " + data['list'][0]['weather'][1]['description'] + " " + icon + ".\n" 
                             + "Температура: " + str(data['list'][0]['main']['temp']) + "°C." + "\n" 
                             + "По ощущениям: " + str(data['list'][0]['main']['feels_like']) + "°C." + "\n"
                             + "Влажность: " + str(data['list'][0]['main']['humidity']) + "%." + "\n"
                             + "Скорость ветра: " + str(data['list'][0]['wind']['speed']) + "м/с.")
                        senderC(id, weath)
                    else:
                        wet_icon = str(data['list'][0]['weather'][0]['icon'])

                        if wet_icon == '01d' or wet_icon == '01n':
                            icon = "&#9728;"
                        if wet_icon == '02d' or wet_icon == '02n':
                            icon = "&#127780;"
                        if wet_icon == '03d' or wet_icon == '03n':
                            icon = "&#9925;"
                        if wet_icon == '04d' or wet_icon == '04n':
                            icon = "&#9729;"
                        if wet_icon == '09d' or wet_icon == '09n':
                            icon = "&#127782;"
                        if wet_icon == '10d' or wet_icon == '10n':
                            icon = "&#127783;"
                        if wet_icon == '11d' or wet_icon == '11n':
                            icon = "&#127785;"
                        if wet_icon == '13d' or wet_icon == '13n':
                            icon = "&#127784;"
                        if wet_icon == '50d' or wet_icon == '50n':
                            icon = "&#127787;"

                        weath = ("Атмосферные условия: " + data['list'][0]['weather'][0]['description'] + " " + icon + ".\n" 
                             + "Температура: " + str(data['list'][0]['main']['temp']) + "°C." + "\n" 
                             + "По ощущениям: " + str(data['list'][0]['main']['feels_like']) + "°C." + "\n"
                             + "Влажность: " + str(data['list'][0]['main']['humidity']) + "%." + "\n"
                             + "Скорость ветра: " + str(data['list'][0]['wind']['speed']) + "м/с.")
                        senderC(id, weath)
                if sett == 'debug':
                    senderC(id, 'Проводится отладка бота, пожалуйста подождите.')

        if event.from_user:
            msg = event.object.message['text']
            msg = msg.lower()
            id = event.message.from_id
            print(msg)
            print(id)

            
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
                    print(data)
                    strData = str(data)
                    count = strData.count("'description'")
                    wet_icon = str(data['list'][0]['weather'][0]['icon'])
                    print(count)

                    if count == 3:
                        wet_icon = str(data['list'][0]['weather'][0]['icon'])
                        wet_icon2 = str(data['list'][0]['weather'][1]['icon'])
                        wet_icon3 = str(data['list'][0]['weather'][2]['icon'])

                        if wet_icon == '01d' or wet_icon == '01n':
                            icon = "&#9728;"
                        if wet_icon == '02d' or wet_icon == '02n':
                            icon = "&#127780;"
                        if wet_icon == '03d' or wet_icon == '03n':
                            icon = "&#9925;"
                        if wet_icon == '04d' or wet_icon == '04n':
                            icon = "&#9729;"
                        if wet_icon == '09d' or wet_icon == '09n':
                            icon = "&#127782;"
                        if wet_icon == '10d' or wet_icon == '10n':
                            icon = "&#127783;"
                        if wet_icon == '11d' or wet_icon == '11n':
                            icon = "&#127785;"
                        if wet_icon == '13d' or wet_icon == '13n':
                            icon = "&#127784;"
                        if wet_icon == '50d' or wet_icon == '50n':
                            icon = "&#127787;"

                        if wet_icon2 == '01d' or wet_icon == '01n':
                            icon2 = "&#9728;"
                        if wet_icon2 == '02d' or wet_icon == '02n':
                            icon2 = "&#127780;"
                        if wet_icon2 == '03d' or wet_icon == '03n':
                            icon2 = "&#9925;"
                        if wet_icon2 == '04d' or wet_icon == '04n':
                            icon2 = "&#9729;"
                        if wet_icon2 == '09d' or wet_icon == '09n':
                            icon2 = "&#127782;"
                        if wet_icon2 == '10d' or wet_icon == '10n':
                            icon2 = "&#127783;"
                        if wet_icon2 == '11d' or wet_icon == '11n':
                            icon2 = "&#127785;"
                        if wet_icon2 == '13d' or wet_icon == '13n':
                            icon2 = "&#127784;"
                        if wet_icon2 == '50d' or wet_icon == '50n':
                            icon2 = "&#127787;"

                        if wet_icon3 == '01d' or wet_icon == '01n':
                            icon3 = "&#9728;"
                        if wet_icon3 == '02d' or wet_icon == '02n':
                            icon3 = "&#127780;"
                        if wet_icon3 == '03d' or wet_icon == '03n':
                            icon3 = "&#9925;"
                        if wet_icon3 == '04d' or wet_icon == '04n':
                            icon3 = "&#9729;"
                        if wet_icon3 == '09d' or wet_icon == '09n':
                            icon3 = "&#127782;"
                        if wet_icon3 == '10d' or wet_icon == '10n':
                            icon3 = "&#127783;"
                        if wet_icon3 == '11d' or wet_icon == '11n':
                            icon3 = "&#127785;"
                        if wet_icon3 == '13d' or wet_icon == '13n':
                            icon3 = "&#127784;"
                        if wet_icon3 == '50d' or wet_icon == '50n':
                            icon3 = "&#127787;"

                        weath = ("Атмосферные условия: " + data['list'][0]['weather'][0]['description'] + " " + icon + ", " + data['list'][0]['weather'][1]['description'] + " " + icon2 + ", " + data['list'][0]['weather'][2]['description'] + " " + icon3 + ".\n" 
                             + "Температура: " + str(data['list'][0]['main']['temp']) + "°C." + "\n" 
                             + "По ощущениям: " + str(data['list'][0]['main']['feels_like']) + "°C." + "\n"
                             + "Влажность: " + str(data['list'][0]['main']['humidity']) + "%." + "\n"
                             + "Скорость ветра: " + str(data['list'][0]['wind']['speed']) + "м/с.")
                        senderU(id, weath)
                    elif count == 2:
                        wet_icon = str(data['list'][0]['weather'][0]['icon'])
                        wet_icon2 = str(data['list'][0]['weather'][1]['icon'])

                        if wet_icon == '01d' or wet_icon == '01n':
                            icon = "&#9728;"
                        if wet_icon == '02d' or wet_icon == '02n':
                            icon = "&#127780;"
                        if wet_icon == '03d' or wet_icon == '03n':
                            icon = "&#9925;"
                        if wet_icon == '04d' or wet_icon == '04n':
                            icon = "&#9729;"
                        if wet_icon == '09d' or wet_icon == '09n':
                            icon = "&#127782;"
                        if wet_icon == '10d' or wet_icon == '10n':
                            icon = "&#127783;"
                        if wet_icon == '11d' or wet_icon == '11n':
                            icon = "&#127785;"
                        if wet_icon == '13d' or wet_icon == '13n':
                            icon = "&#127784;"
                        if wet_icon == '50d' or wet_icon == '50n':
                            icon = "&#127787;"

                        if wet_icon2 == '01d' or wet_icon == '01n':
                            icon2 = "&#9728;"
                        if wet_icon2 == '02d' or wet_icon == '02n':
                            icon2 = "&#127780;"
                        if wet_icon2 == '03d' or wet_icon == '03n':
                            icon2 = "&#9925;"
                        if wet_icon2 == '04d' or wet_icon == '04n':
                            icon2 = "&#9729;"
                        if wet_icon2 == '09d' or wet_icon == '09n':
                            icon2 = "&#127782;"
                        if wet_icon2 == '10d' or wet_icon == '10n':
                            icon2 = "&#127783;"
                        if wet_icon2 == '11d' or wet_icon == '11n':
                            icon2 = "&#127785;"
                        if wet_icon2 == '13d' or wet_icon == '13n':
                            icon2 = "&#127784;"
                        if wet_icon2 == '50d' or wet_icon == '50n':
                            icon2 = "&#127787;"

                        weath = ("Атмосферные условия: " + data['list'][0]['weather'][0]['description'] + " " + icon + ", " + data['list'][0]['weather'][1]['description'] + " " + icon + ".\n" 
                             + "Температура: " + str(data['list'][0]['main']['temp']) + "°C." + "\n" 
                             + "По ощущениям: " + str(data['list'][0]['main']['feels_like']) + "°C." + "\n"
                             + "Влажность: " + str(data['list'][0]['main']['humidity']) + "%." + "\n"
                             + "Скорость ветра: " + str(data['list'][0]['wind']['speed']) + "м/с.")
                        senderU(id, weath)
                    else:
                        wet_icon = str(data['list'][0]['weather'][0]['icon'])

                        if wet_icon == '01d' or wet_icon == '01n':
                            icon = "&#9728;"
                        if wet_icon == '02d' or wet_icon == '02n':
                            icon = "&#127780;"
                        if wet_icon == '03d' or wet_icon == '03n':
                            icon = "&#9925;"
                        if wet_icon == '04d' or wet_icon == '04n':
                            icon = "&#9729;"
                        if wet_icon == '09d' or wet_icon == '09n':
                            icon = "&#127782;"
                        if wet_icon == '10d' or wet_icon == '10n':
                            icon = "&#127783;"
                        if wet_icon == '11d' or wet_icon == '11n':
                            icon = "&#127785;"
                        if wet_icon == '13d' or wet_icon == '13n':
                            icon = "&#127784;"
                        if wet_icon == '50d' or wet_icon == '50n':
                            icon = "&#127787;"

                        weath = ("Атмосферные условия: " + data['list'][0]['weather'][0]['description'] + " " + icon + ".\n" 
                             + "Температура: " + str(data['list'][0]['main']['temp']) + "°C." + "\n" 
                             + "По ощущениям: " + str(data['list'][0]['main']['feels_like']) + "°C." + "\n"
                             + "Влажность: " + str(data['list'][0]['main']['humidity']) + "%." + "\n"
                             + "Скорость ветра: " + str(data['list'][0]['wind']['speed']) + "м/с.")
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