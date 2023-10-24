import schedule
import threading
from threading import Thread
import time
import json
from time import sleep
import telebot
import pandas as pd
from telebot import types
import datetime
from datetime import date, timedelta
from bob_telegram_tools.bot import TelegramBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import os

bot = telebot.TeleBot(os.environ['TG_TOKEN'])
today = date.today()
if today.strftime('%Y-%m-%d') == '2023-10-23':
    lesson = '<b>УРОК 1. ЗЕМЛЯ</b> \n' \
    'Остановка: Земля \n\n' \
    'Йога  и медитация подводят нас к настоящему моменту, единственному месту, где существует жизнь. На сегодняшний день в просторах нашей галактики известно о жизни только на одной планете — планете Земля. \n\n' \
    'С Земли, и с практики Намерения, мы и начнём наше увлекательное путешествие по уголкам внутренней вселенной.\n\n' \
    '<a href="https://youtu.be/3HlhKcWDUNA?feature=shared">Ссылка на урок</a>\n\n' \
    '#lesson1'
elif today.strftime('%Y-%m-%d') == '2023-10-24':
    lesson = '<b>УРОК 2. Планета Алмазов Cancri e</b> \n' \
    'Остановка: планета Cancri e \n\n' \
    'Она вращается вокруг звезды, которая напоминает Солнце, в созвездии Рака. Год на ней равен нашим 18 часам.Она в два раза больше Земли и на треть состоит из алмаза. Представьте, сколько она может стоить? \n\n' \
    'В отличие от алмазов, здоровая спина — бесценна. И не зря говорят, что мы молоды настолько, насколько гибкий наш позвоночник. Сегодня мы как раз и поработаем над тем, чтобы быть ещё моложе и здоровее.\n\n' \
    '<a href="https://youtu.be/t4v3u6RCjM4?feature=shared">Ссылка на урок</a>\n\n' \
    '#lesson2'
elif today.strftime('%Y-%m-%d') == '2023-10-25':
    lesson = '<b>УРОК 3. Табата - силовая база йоги.</b> \n' \
    'Остановка: Галактика сомбреро \n\n' \
    'Только посмотрите на эту вселенную! Вообще — это не одна галактика, а целых две. Этот космический объект знаменателен тем, что внутри него находится сверхмассивная чёрная дыра, которая по массе, как 1 млрд наших Солнц.\n\n' \
    'Точно также, как галактика Сомбреро содержит в себе сразу три объекта в одном, мы будем развивать в сегодняшнем занятии сразу три качества: силу, гибкость иии...выносливость! Именно этим и славятся йоговские табаты.\n\n' \
    'Табата — это тренировки, которые проходят в строгом режиме чередования нагрузок (20 секунд) и отдыха (10 секунд). Ребята, это правда тяжело, лучше делать НЕ на ночь :) Но! Оно того стоит. Рельеф за счет такого появляется 💪\n\n' \
    '❗️Перед табатой немного разомните кисти, и после ОБЯЗАТЕЛЬНО сделайте шавасану.\n' \
    '<a href="https://youtu.be/efYGKgC7Q6w?feature=shared">Ссылка на урок</a>\n\n' \
    '#lesson3'
elif today.strftime('%Y-%m-%d') == '2023-10-26':
    lesson = '<b>УРОК 4. Чандра Намаскар</b> \n' \
    'Остановка: Луна \n\n' \
    'Сегодня мы прибыли на спутник Земли — прекрасна Луну, гравитационное влияние которой вызывает на Земле морские приливы и отливы. Луну мы поприветствуем цикличной практикой под названием Чандра Намскар (на санскрите переводится как приветствие Луне или сияние лунного света).\n\n' \
    '14 асан Чандра Намаскар представляют 14 лунных фаз. В лунном календаре 14 дней до полнолуния называются «сукла пакша» — светлые две недели, а 14 дней после полнолуния — «кришна пакша», то есть темные две недели. Имя каждого дня представляет отдельную асану в этой практике йоги.\n\n' \
    'А тем, кто не очень любит цикличные практики, я записала ещё практику НА ОСНОВЕ Чандра Намаскар. Выбирайте любую, и помните, что главное - наблюдать, а не асаны.\n\n' \
    '🌙Практику рекомендуется делать вечером.\n' \
    '<a href="https://youtu.be/t4v3u6RCjM4?feature=shared">Ссылка на урок</a>\n\n' \
    '#lesson4'
elif today.strftime('%Y-%m-%d') == '2023-10-27':
    lesson = '<b>УРОК 5. Дыхательная практика</b> \n' \
    'Остановка: ОТКРЫТЫЙ КОСМОС \n\n' \
    'Всем известно, что в открытом космосе - вакуум, и дышать там не представляется возможным. Однако йогам и такая преграда может быть по плечу. \n\n' \
    'Расскажу интересный факт. Есть зафиксированные случаи, когда йоги задерживали дыхание от 30 до 60 минут. Но как??? В это сложно поверить, но основную роль в этом играют психологические факторы. Йоги умеют управлять своей нервной системой - уменьшать частоту пульса, регулировать давление. Представляете? \n\n' \
    'К задержкам нужно готовиться, но начинать надо не с задержек, а с подготовительных техник. С них-то мы и начнём:\n' \
    '&#129729; Дыхание Уджайи - растягивает дыхательный цикл.\n' \
    '&#129729; Капалабхати - наоборот, уменьшает и способствует выводу СО2.\n\n' \
    'Кстати интересный факт: в йоге дыхательные практики по сложности идут после асан, как бы следующей ступенью.\n\n' \
    'Поехали!\n\n' \
    '<a href="https://youtu.be/1SjLLTf5Uu8?feature=shared">Ссылка на урок</a>\n\n' \
    '#lesson5'
elif today.strftime('%Y-%m-%d') == '2023-10-28':
    lesson = '<b>УРОК 6. Живая практика</b> \n' \
    'Остановка: Milky Way \n\n' \
    'В ясные и особенно в безлунные ночи вдали от мегаполиса, вероятно, каждому приходилось видеть на небе молочно-белую полосу, которая как бы опоясывает небосвод. Словно река, растекается по небу этот поток - Млечный путь. \n\n' \
    'Сегодня мы будем идти по Млечному пути среди светил - таких ярких и прекрасных, которые легко могут отвлечь наше внимание, но мы учимся сосредотачиваться на себе, на своем собственном свете.\n\n' \
    'На этом занятии мы объединим все то, что выучили за неделю, и наконец-то увидимся «вживую». \n\n' \
    'Начало: 10:00\n' \
    'Длительность: 1:30\n' \
    '<a href="https://join.skype.com/Od8oDejQf9gc">Ссылка на Skype</a>\n\n' \
    'Регистрироваться не нужно, просто переходите по ссылке. И еще, для тех, кто не сможет присоединиться, <b>запись занятия конечно же будет.</b>\n\n' \
    '#lesson6'
elif today.strftime('%Y-%m-%d') == '2023-10-29':
    lesson = '<b>УРОК 7. Йога-Нидра</b> \n' \
    'Остановка: Квазар TON 618 \n\n' \
    'Сегодня мы нырнём в пучину неизведанного, сделав остановку на самой огромной чёрной дыре на данный момент: её масса в 66 млрд раз больше массы Солнца. Квазар TON 618 – самая большая из когда-либо открытых черных дыр.\n\n' \
    'Наверняка вы слышали о концепции трехуровневая разума: сознательном, подсознательном и бессознательном. Наш сознательный ум кажется нам капитаном космического корабля, ведь это наш «контроллер», это наше Я. Однако... именно в других отделах находится информация, которая значительно управляет нашей жизнью (оттуда берутся блоки, повторяющиеся сценарии в жизни и т.д.), а мы этого даже не осознаём.\n\n' \
    'Сегодня мы попробуем добраться до этой чёрной дыры через Йога-Нидру. Практику, которая относится к NSDR – non-sleep deep rest. Это практика глубокого расслабления, которая отличается от медитации сниженным уровнем бодрствования. Мы не спим, но и не стараемся поддерживать максимальную ясность сознания и контроль внимания, как в медитации.\n\n' \
    'Даже если вы уснёте, знайте, работа идёт\n\n' \
    '🌙 Лучше делать прям перед сном в любимой кровати и под одеялом \n\n' \
    '<a href="https://youtu.be/t4v3u6RCjM4?feature=shared">Ссылка на урок</a>\n\n' \
    '#lesson7'
elif today.strftime('%Y-%m-%d') == '2023-10-30':
    lesson = lesson2
elif today.strftime('%Y-%m-%d') == '2023-10-31':
    lesson = lesson2
elif today.strftime('%Y-%m-%d') == '2023-11-01':
    lesson = lesson2
elif today.strftime('%Y-%m-%d') == '2023-11-02':
    lesson = lesson2
elif today.strftime('%Y-%m-%d') == '2023-11-03':
    lesson = lesson2
elif today.strftime('%Y-%m-%d') == '2023-11-04':
    lesson = lesson2
elif today.strftime('%Y-%m-%d') == '2023-11-05':
    lesson = lesson2
elif today.strftime('%Y-%m-%d') == '2023-11-06':
    lesson = lesson2
elif today.strftime('%Y-%m-%d') == '2023-11-07':
    lesson = lesson2
elif today.strftime('%Y-%m-%d') == '2023-11-08':
    lesson = lesson2
elif today.strftime('%Y-%m-%d') == '2023-11-09':
    lesson = lesson2
elif today.strftime('%Y-%m-%d') == '2023-11-10':
    lesson = lesson2
elif today.strftime('%Y-%m-%d') == '2023-11-11':
    lesson = lesson2
elif today.strftime('%Y-%m-%d') == '2023-11-12':
    lesson = lesson2

@bot.message_handler(commands=['start'])
def start(message):
    global markup
    lst1 = []
    name = message.from_user.id
    lst1.append(name)
    with open("chat_id.txt", "a") as file:
        for id in lst1:
            file.write(str(id) +'\n')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Расписание")
    btn2 = types.KeyboardButton("Технические моменты")
    markup.add(btn1, btn2)
    markup1 = InlineKeyboardMarkup()
    markup1.add(InlineKeyboardButton(text='Дополнительное задание', callback_data='addtask'))
    text = 'Намасте🙏, {0.first_name} \n\n' \
    'Я очень рада приветствовать вас на этом курсе! На курсе, с помощью которого вы получите ключики к управлению своим состоянием через познание себя с помощью древних практик йоги.\n\n' \
    'Скоро откроется первое занятие, а пока для вас есть послание!'
    bot.send_message(message.chat.id, text=text.format(message.from_user), reply_markup=markup)  
    audio = open(r"Music.mp3", 'rb')
    bot.send_audio(message.chat.id, audio, title = 'Послание', reply_markup=markup1)
    audio.close()

# Реакция на кнопки
@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Расписание":
        lst1 = []
        name = message.from_user.id
        lst1.append(name)
        with open("chat_id.txt", "a") as file:
            for id in lst1:
                file.write(str(id) +'\n')
        with open('Schedule.json') as json_file:
            data = json.load(json_file, encoding='utf-8')
            sc = pd.read_json(data, orient='values')
            sc['Дата'] = pd.to_datetime(sc['Дата']).dt.date
            sc['d'] = pd.to_datetime(sc['Дата']).dt.strftime('%d')
            sc['m'] = pd.to_datetime(sc['Дата']).dt.strftime('%m').astype('int64')
            date = pd.DataFrame({'Month_num': [1,2,3,4,5,6,7,8,9,10,11,12], 
                                 'Month_name': ['января','февраля','марта','апреля','мая','июня','ибля','августа','сентября','октября','ноября','декабря']})
            sc = sc.merge(date, left_on = 'm', right_on = 'Month_num', how = 'left')
            sc['date_text'] = sc['d'] + ' ' + sc['Month_name']
            sc = sc[['Урок','Дата','Описание','Ссылка','date_text']]
        lst = []
        for _,row in sc.iterrows():
            if row['Урок'] == 'Шавасана':
                schedule = f"&#128301; <b>{row['Урок']}</b>"'\n' + f"&#128467; {row['Описание']}" + '\n' + f"{row['Ссылка']}" + '\n' + '_____________'
                lst.append(schedule)
            elif row['Урок'] != 'Шавасана' and row['Дата'] <= today:
                schedule = f"&#128301; <b>{row['Урок']}</b>" + '\n' + f"&#128467; {row['date_text']}" + '\n' + f"{row['Описание']}" + '\n' + f"{row['Ссылка']}" + '\n' + '_____________'
                lst.append(schedule)
            else:
                schedule = f"&#128301; <b>{row['Урок']}</b>" + '\n' + f"&#128467; {row['date_text']}" + '\n' + f"{row['Описание']}" + '\n' + f"<i>Ссылка появится в день урока</i>" + '\n' + '_____________'
                lst.append(schedule)
        bot.send_message(message.chat.id, '\n'.join(lst), parse_mode="html")#, reply_markup = markup)
    elif message.text == "Технические моменты":
        lst1 = []
        name = message.from_user.id
        lst1.append(name)
        with open("chat_id.txt", "a") as file:
            for id in lst1:
                file.write(str(id) +'\n')
        send = 'Несколько технических моментов: \n' \
        '1. <b>Занятия будут приходить каждый день в этом боте.</b> Постарайся не откладывать занятия, чтобы у тебя не накопилось много пропусков. Полнота практики очень важна. \n' \
        '2. <b>Для всех занятий понадобится коврик.</b> Возможно, не помешает иметь фитнес-блоки и ремешки. Их смело можно заменить на книги и пояс от халата😅 \n' \
        '3. <b>До занятия лучше не есть за 1,5-2 часа.</b>\n' \
        '4. <b>После каждого занятия делай шавасану (практика расслабления).</b> Это важно! \n' \
        '5. <b>Все вопросы можно задавать <a href="https://t.me/NataliLarina8">лично</a> или <a href="https://t.me/+oSpisjZHdR8yNzI6">в общем чате.</a></b> \n' \
        '6. <b>Также я дарю тебе трекер, в котором ты сможешь отмечать свои успехи.</b> 21 день - не так много, чтобы не слиться, но вполне достаточно, чтобы заложить кирпичик к большим изменениям❤️'
        bot.send_message(message.from_user.id, send, parse_mode="html")
        treker = open(r"Tracker.pdf","rb")
        bot.send_document(message.chat.id, document = treker, visible_file_name = 'Трекер.pdf')
        
@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    req = call.data.split('_')
    if req[0] == 'addtask':
        send = 'Подробнее о том, как выбрать для себя намерение, ты можешь почитать по этой <a href="https://www.oum.ru/yoga/osnovy-yogi/slovar-yogi-sankalpa/">ссылке</a> \n\n' \
        'Выпиши свою санкальпу на листок. Она понадобится тебе к первому дню.\n\n' \
        'Удачи! Встречаемся в понедельник на первом занятии.'
        bot.send_message(call.from_user.id, send, parse_mode="html")

def schedule_checker():
    schedule.every().day.at("12:37").do(function_to_run, lesson = lesson)
    schedule.every(1).minutes.do(dont_sleep)
    while True:
        schedule.run_pending()
        sleep(1)

def function_to_run(lesson):
    fp = open('chat_id.txt','r')
    df = pd.DataFrame(fp,columns = ['chat_id'])
    df = df.drop_duplicates()
    df['chat_id'] = df['chat_id'].apply(lambda x: x.replace('\n',''))
    fp.close()
    for chat_id in df['chat_id']:
        print(chat_id)
        bot.send_message(chat_id, text = lesson, parse_mode="html")
        time.sleep(2)
    t1.should_abort_immediately = True

def dont_sleep():
    print(f"I'm not sleeping")

if __name__ == '__main__':
    t1 = Thread(target=schedule_checker, daemon=True)
    t2 = Thread(target=start)
    t1.start()
    t2.start()

bot.infinity_polling(timeout=10, long_polling_timeout = 5)

