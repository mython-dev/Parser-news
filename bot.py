# 
#                  _______          _________                 ______   _______          
#                 (       )|\     /|\__   __/|\     /|       (  __  \ (  ____ \|\     /|
#                 | () () |( \   / )   ) (   | )   ( |       | (  \  )| (    \/| )   ( |
#                 | || || | \ (_) /    | |   | (___) | _____ | |   ) || (__    | |   | |
#                 | |(_)| |  \   /     | |   |  ___  |(_____)| |   | ||  __)   ( (   ) )
#                 | |   | |   ) (      | |   | (   ) |       | |   ) || (       \ \_/ / 
#                 | )   ( |   | |      | |   | )   ( |       | (__/  )| (____/\  \   /  
#                 |/     \|   \_/      )_(   |/     \|       (______/ (_______/   \_/   
#                             
#                                                              
#                             Code by: Myth-dev or thehackerworld_
#                             Instagram: @mython_dev or @thehackerworld_
#                             Telegram: @myth_dev
#                             Github: https://github.com/mython-dev
# 
#                        This bot can parse the news from the site kun.uz :)

from config import TOKEN
import time
try:
    from aiogram import Dispatcher, executor, types, Bot
    import requests
    from bs4 import BeautifulSoup
    from aiogram.types import *
except ImportError:
    print('Please run: "pip3 install requirements.txt"')

bot = Bot(TOKEN, parse_mode=types.ParseMode.HTML)
 
dp = Dispatcher(bot)

ID  = '1543290559'

async def on_startup(_):
    print('The bot has successfully runned :)')

async def on_shutdown(_):
    print('The bot has successfully stopped!')

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    kb_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

    kb_uzbekistan = KeyboardButton(text='Ўзбекистон')
    kb_jahon = KeyboardButton(text='Жаҳон')
    kb_iktisodiet =  KeyboardButton(text='Иқтисодиёт')
    kb_jamiyat = KeyboardButton(text='Жамият')
    kb_tehnologia = KeyboardButton(text='Фан-техника')
    kb_sport = KeyboardButton(text='Спорт')
    kb_search = KeyboardButton(text='Қидирув')
    kb_xdud = KeyboardButton(text='Ҳудудлар')

    kb_menu.add(kb_uzbekistan,
                kb_jahon,
                kb_iktisodiet,
                kb_jamiyat,
                kb_tehnologia,
                kb_sport,
                kb_xdud)

    await bot.send_message(message.from_user.id, 'Янгиликларни билиш учун бирор нарсани танланг!', reply_markup=kb_menu)

@dp.message_handler()
async def parser(message: types.Message):
        if message.text == 'Ўзбекистон':
            url_category_uzbekiston = f'https://kun.uz/news/category/uzbekiston'
            response = requests.get(url_category_uzbekiston)
            soup = BeautifulSoup(response.text, 'html.parser')
            news = soup.find_all('div', class_='news')

            await bot.send_message(message.from_user.id, "Besh ta so'nggi yangiliklarni yuborish")
            
            time.sleep(3)

            for new in news[-5:]:
                time_new = new.findChildren('div')[0]
                new_img = new.findChildren('a')[0]
                name_news = new.findChildren('a')[-1]
                links_news = new.findChildren('a')[0]
                kb_podrobnee = InlineKeyboardMarkup()
                podrobnee = InlineKeyboardButton(text='Батафсил', url='https://kun.uz' + links_news['href'])
                kb_podrobnee.add(podrobnee)
                result = f'<b>Время:</b><em> {time_new.text}</em>\n<b>Назвение:</b> <code>{name_news.text}</code>\n'
                        
                await bot.send_photo(message.from_user.id, new_img.findChildren('img')[0]["src"], 
                                    caption = result,
                                    parse_mode='HTML', 
                                    reply_markup=kb_podrobnee)


        elif message.text == 'Жаҳон':
        
            url_category_jahon = 'https://kun.uz/news/category/jahon'
            response = requests.get(url_category_jahon)
            soup = BeautifulSoup(response.text, 'html.parser')
            news = soup.find_all('div', class_='news')

            await bot.send_message(message.from_user.id, "Besh ta so'nggi yangiliklarni yuborish")
                
            time.sleep(3)

            for new in news[-5:]:
                time_new = new.findChildren('div')[0]
                new_img = new.findChildren('a')[0]
                name_news = new.findChildren('a')[-1]
                links_news = new.findChildren('a')[0]
                kb_podrobnee = InlineKeyboardMarkup()
                podrobnee = InlineKeyboardButton(text='Батафсил', url='https://kun.uz' + links_news['href'])
                kb_podrobnee.add(podrobnee)
                result = f'<b>Время:</b><em> {time_new.text}</em>\n<b>Назвение:</b> <code>{name_news.text}</code>\n'
                        
                await bot.send_photo(message.from_user.id, new_img.findChildren('img')[0]["src"], 
                                    caption = result,
                                    parse_mode='HTML', 
                                    reply_markup=kb_podrobnee)


        elif message.text == 'Иқтисодиёт':
        
            url_category_iktisodiet = 'https://kun.uz/news/category/iktisodiet'
            response = requests.get(url_category_iktisodiet)
            soup = BeautifulSoup(response.text, 'html.parser')
            news = soup.find_all('div', class_='news')

            await bot.send_message(message.from_user.id, "Besh ta so'nggi yangiliklarni yuborish")
                
            time.sleep(3)

            for new in news[-5:]:
                time_new = new.findChildren('div')[0]
                new_img = new.findChildren('a')[0]
                name_news = new.findChildren('a')[-1]
                links_news = new.findChildren('a')[0]
                kb_podrobnee = InlineKeyboardMarkup()
                podrobnee = InlineKeyboardButton(text='Батафсил', url='https://kun.uz' + links_news['href'])
                kb_podrobnee.add(podrobnee)
                result = f'<b>Время:</b><em> {time_new.text}</em>\n<b>Назвение:</b> <code>{name_news.text}</code>\n'
                        
                await bot.send_photo(message.from_user.id, new_img.findChildren('img')[0]["src"], 
                                    caption = result,
                                    parse_mode='HTML', 
                                    reply_markup=kb_podrobnee)


        elif message.text == 'Жамият':
        
            url_category_jamiyat = 'https://kun.uz/news/category/jamiyat'
            response = requests.get(url_category_jamiyat)
            soup = BeautifulSoup(response.text, 'html.parser')
            news = soup.find_all('div', class_='news')

            await bot.send_message(message.from_user.id, "Besh ta so'nggi yangiliklarni yuborish")
                
            time.sleep(3)

            for new in news[-5:]:
                time_new = new.findChildren('div')[0]
                new_img = new.findChildren('a')[0]
                name_news = new.findChildren('a')[-1]
                links_news = new.findChildren('a')[0]
                kb_podrobnee = InlineKeyboardMarkup()
                podrobnee = InlineKeyboardButton(text='Батафсил', url='https://kun.uz' + links_news['href'])
                kb_podrobnee.add(podrobnee)
                result = f'<b>Время:</b><em> {time_new.text}</em>\n<b>Назвение:</b> <code>{name_news.text}</code>\n'
                        
                await bot.send_photo(message.from_user.id, new_img.findChildren('img')[0]["src"], 
                                    caption = result,
                                    parse_mode='HTML', 
                                    reply_markup=kb_podrobnee)

        elif message.text == 'Фан-техника':

            url_category_tehnologia = 'https://kun.uz/news/category/tehnologia'
            response = requests.get(url_category_tehnologia)
            soup = BeautifulSoup(response.text, 'html.parser')
            news = soup.find_all('div', class_='news')

            await bot.send_message(message.from_user.id, "Besh ta so'nggi yangiliklarni yuborish")
                
            time.sleep(3)

            for new in news[-5:]:
                time_new = new.findChildren('div')[0]
                new_img = new.findChildren('a')[0]
                name_news = new.findChildren('a')[-1]
                links_news = new.findChildren('a')[0]
                kb_podrobnee = InlineKeyboardMarkup()
                podrobnee = InlineKeyboardButton(text='Батафсил', url='https://kun.uz' + links_news['href'])
                kb_podrobnee.add(podrobnee)
                result = f'<b>Время:</b><em> {time_new.text}</em>\n<b>Назвение:</b> <code>{name_news.text}</code>\n'
                        
                await bot.send_photo(message.from_user.id, new_img.findChildren('img')[0]["src"], 
                                    caption = result,
                                    parse_mode='HTML', 
                                    reply_markup=kb_podrobnee)
               
        elif message.text == 'Спорт':

            url_category_sport = 'https://kun.uz/news/category/sport'
            response = requests.get(url_category_sport)
            soup = BeautifulSoup(response.text, 'html.parser')
            news = soup.find_all('div', class_='news')

            await bot.send_message(message.from_user.id, "Besh ta so'nggi yangiliklarni yuborish")
                
            time.sleep(3)

            for new in news[-5:]:
                time_new = new.findChildren('div')[0]
                new_img = new.findChildren('a')[0]
                name_news = new.findChildren('a')[-1]
                links_news = new.findChildren('a')[0]
                kb_podrobnee = InlineKeyboardMarkup()
                podrobnee = InlineKeyboardButton(text='Батафсил', url='https://kun.uz' + links_news['href'])
                kb_podrobnee.add(podrobnee)
                result = f'<b>Время:</b><em> {time_new.text}</em>\n<b>Назвение:</b> <code>{name_news.text}</code>\n'
                        
                await bot.send_photo(message.from_user.id, new_img.findChildren('img')[0]["src"], 
                                    caption = result,
                                    parse_mode='HTML', 
                                    reply_markup=kb_podrobnee)

        elif message.text == 'Ҳудудлар':

            kb_xdud = InlineKeyboardMarkup(row_width=2)

            kb_toshkent = InlineKeyboardButton(text='Тошкент ш.', callback_data='toshkent')
            kb_qorakalpakiston = InlineKeyboardButton(text='Қорақалпоғистон', callback_data='qorakalpakiston')
            kb_andijon = InlineKeyboardButton(text='Андижон', callback_data='andijon')
            kb_fargona = InlineKeyboardButton(text='Фарғона', callback_data='fargona')
            kb_namangan = InlineKeyboardButton(text='Наманган', callback_data='namangan')
            kb_samarqand = InlineKeyboardButton(text='Самарқанд', callback_data='samarqand')
            kb_buxoro = InlineKeyboardButton(text='Бухоро', callback_data='buxoro')
            kb_xorazm = InlineKeyboardButton(text='Хоразм', callback_data='xorazm')
            kb_surxondaryo = InlineKeyboardButton(text='Сурхондарё', callback_data='surxondaryo')
            kb_qashqadaryo = InlineKeyboardButton(text='Қашқадарё', callback_data='qashqadaryo')
            kb_jizzax = InlineKeyboardButton(text='Жиззах', callback_data='jizzax')
            kb_sirdaryo = InlineKeyboardButton(text='Сирдарё', callback_data='sirdaryo')
            kb_toshkent_viloyati = InlineKeyboardButton('Тошкент вил', callback_data='toshkent_viloyati')
            kb_navoiy = InlineKeyboardButton('Навоий', callback_data='navoiy')

            kb_xdud.add(kb_toshkent,
                        kb_qorakalpakiston,
                        kb_andijon,
                        kb_fargona,
                        kb_namangan,
                        kb_samarqand,
                        kb_buxoro,
                        kb_xorazm,
                        kb_surxondaryo,
                        kb_qashqadaryo,
                        kb_jizzax,
                        kb_sirdaryo,
                        kb_toshkent_viloyati,
                        kb_navoiy
                        )

            await bot.send_message(message.from_user.id, 'Viloyat yangiliklarini tanlang!', reply_markup=kb_xdud)

            @dp.callback_query_handler()

            async def region_toshkent(call: types.CallbackQuery):

                if call.data == 'toshkent':
                    url_region_tashkent = 'https://kun.uz/region/toshkent'
                    response = requests.get(url_region_tashkent)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    news = soup.find_all('div', class_='l-item')

                    await bot.send_message(message.from_user.id, "<b>Besh ta so'nggi yangiliklarni yuborish</b>")

                    time.sleep(3)

                    for new in news[:-5]:
                        news_time  = new.findChildren('span')[-1]
                        name_news  = new.findChildren('a')[-1]
                        description = new.findChildren('p')[0]
                        links_news =  new.findChildren('a')[0]
                        final_link_news = 'https://kun.uz' + links_news['href']
                        links_img = new.findChildren('img')[0]["src"]

                        kb_podrobnee = InlineKeyboardMarkup(row_width=1)
                        podrobnee = InlineKeyboardButton(text='Батафсил', url=final_link_news)
                        kb_podrobnee.add(podrobnee)

                        result = f'<b>Время:</b> <em>{news_time.text}</em><b>\nНазвания:</b> <em>{name_news.text}</em><b>\nОписания:</b> <em>{description.text}</em>'
                        await bot.send_photo(message.from_user.id, links_img,
                                            caption=result,
                                            parse_mode='HTML',
                                            reply_markup=kb_podrobnee)

                elif call.data == 'qorakalpakiston':
                    url_region_qorakalpakiston = 'https://kun.uz/region/qorakalpakiston'
                    response = requests.get(url_region_qorakalpakiston)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    news = soup.find_all('div', class_='l-item')

                    await bot.send_message(message.from_user.id, "<b>Besh ta so'nggi yangiliklarni yuborish</b>")

                    time.sleep(3)

                    for new in news[:-5]:
                        news_time  = new.findChildren('span')[-1]
                        name_news  = new.findChildren('a')[-1]
                        description = new.findChildren('p')[0]
                        links_news =  new.findChildren('a')[0]
                        final_link_news = 'https://kun.uz' + links_news['href']
                        links_img = new.findChildren('img')[0]["src"]

                        kb_podrobnee = InlineKeyboardMarkup(row_width=1)
                        podrobnee = InlineKeyboardButton(text='Батафсил', url=final_link_news)
                        kb_podrobnee.add(podrobnee)

                        result = f'<b>Время:</b> <em>{news_time.text}</em><b>\nНазвания:</b> <em>{name_news.text}</em><b>\nОписания:</b> <em>{description.text}</em>'
                        await bot.send_photo(message.from_user.id, links_img,
                                            caption=result,
                                            parse_mode='HTML',
                                            reply_markup=kb_podrobnee)


                elif call.data == 'andijon':
                    url_region_andijon = 'https://kun.uz/region/andijon'
                    response = requests.get(url_region_andijon)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    news = soup.find_all('div', class_='l-item')

                    await bot.send_message(message.from_user.id, "<b>Besh ta so'nggi yangiliklarni yuborish</b>")

                    time.sleep(3)

                    for new in news[:-5]:
                        news_time  = new.findChildren('span')[-1]
                        name_news  = new.findChildren('a')[-1]
                        description = new.findChildren('p')[0]
                        links_news =  new.findChildren('a')[0]
                        final_link_news = 'https://kun.uz' + links_news['href']
                        links_img = new.findChildren('img')[0]["src"]

                        kb_podrobnee = InlineKeyboardMarkup(row_width=1)
                        podrobnee = InlineKeyboardButton(text='Батафсил', url=final_link_news)
                        kb_podrobnee.add(podrobnee)

                        result = f'<b>Время:</b> <em>{news_time.text}</em><b>\nНазвания:</b> <em>{name_news.text}</em><b>\nОписания:</b> <em>{description.text}</em>'
                        await bot.send_photo(message.from_user.id, links_img,
                                            caption=result,
                                            parse_mode='HTML',
                                            reply_markup=kb_podrobnee)

                elif call.data == 'fargona':
                    url_region_fargona= 'https://kun.uz/region/fargona'
                    response = requests.get(url_region_fargona)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    news = soup.find_all('div', class_='l-item')

                    await bot.send_message(message.from_user.id, "<b>Besh ta so'nggi yangiliklarni yuborish</b>")

                    time.sleep(3)

                    for new in news[:-5]:
                        news_time  = new.findChildren('span')[-1]
                        name_news  = new.findChildren('a')[-1]
                        description = new.findChildren('p')[0]
                        links_news =  new.findChildren('a')[0]
                        final_link_news = 'https://kun.uz' + links_news['href']
                        links_img = new.findChildren('img')[0]["src"]

                        kb_podrobnee = InlineKeyboardMarkup(row_width=1)
                        podrobnee = InlineKeyboardButton(text='Батафсил', url=final_link_news)
                        kb_podrobnee.add(podrobnee)

                        result = f'<b>Время:</b> <em>{news_time.text}</em><b>\nНазвания:</b> <em>{name_news.text}</em><b>\nОписания:</b> <em>{description.text}</em>'
                        await bot.send_photo(message.from_user.id, links_img,
                                            caption=result,
                                            parse_mode='HTML',
                                            reply_markup=kb_podrobnee)

                elif call.data == 'namangan':
                    url_region_namangan= 'https://kun.uz/region/namangan'
                    response = requests.get(url_region_namangan)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    news = soup.find_all('div', class_='l-item')

                    await bot.send_message(message.from_user.id, "<b>Besh ta so'nggi yangiliklarni yuborish</b>")

                    time.sleep(3)

                    for new in news[:-5]:
                        news_time  = new.findChildren('span')[-1]
                        name_news  = new.findChildren('a')[-1]
                        description = new.findChildren('p')[0]
                        links_news =  new.findChildren('a')[0]
                        final_link_news = 'https://kun.uz' + links_news['href']
                        links_img = new.findChildren('img')[0]["src"]

                        kb_podrobnee = InlineKeyboardMarkup(row_width=1)
                        podrobnee = InlineKeyboardButton(text='Батафсил', url=final_link_news)
                        kb_podrobnee.add(podrobnee)

                        result = f'<b>Время:</b> <em>{news_time.text}</em><b>\nНазвания:</b> <em>{name_news.text}</em><b>\nОписания:</b> <em>{description.text}</em>'
                        await bot.send_photo(message.from_user.id, links_img,
                                            caption=result,
                                            parse_mode='HTML',
                                            reply_markup=kb_podrobnee)

                elif call.data == 'samarqand':
                    url_region_samarqand = 'https://kun.uz/region/samarqand'
                    response = requests.get(url_region_samarqand)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    news = soup.find_all('div', class_='l-item')

                    await bot.send_message(message.from_user.id, "<b>Besh ta so'nggi yangiliklarni yuborish</b>")

                    time.sleep(3)

                    for new in news[:-5]:
                        news_time  = new.findChildren('span')[-1]
                        name_news  = new.findChildren('a')[-1]
                        description = new.findChildren('p')[0]
                        links_news =  new.findChildren('a')[0]
                        final_link_news = 'https://kun.uz' + links_news['href']
                        links_img = new.findChildren('img')[0]["src"]

                        kb_podrobnee = InlineKeyboardMarkup(row_width=1)
                        podrobnee = InlineKeyboardButton(text='Батафсил', url=final_link_news)
                        kb_podrobnee.add(podrobnee)

                        result = f'<b>Время:</b> <em>{news_time.text}</em><b>\nНазвания:</b> <em>{name_news.text}</em><b>\nОписания:</b> <em>{description.text}</em>'
                        await bot.send_photo(message.from_user.id, links_img,
                                            caption=result,
                                            parse_mode='HTML',
                                            reply_markup=kb_podrobnee)                                        

                elif call.data == 'qashqadaryo':
                    url_region_qashqadaryo = 'https://kun.uz/region/qashqadaryo'
                    response = requests.get(url_region_qashqadaryo)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    news = soup.find_all('div', class_='l-item')

                    await bot.send_message(message.from_user.id, "<b>Besh ta so'nggi yangiliklarni yuborish</b>")

                    time.sleep(3)

                    for new in news[:-5]:
                        news_time  = new.findChildren('span')[-1]
                        name_news  = new.findChildren('a')[-1]
                        description = new.findChildren('p')[0]
                        links_news =  new.findChildren('a')[0]
                        final_link_news = 'https://kun.uz' + links_news['href']
                        links_img = new.findChildren('img')[0]["src"]

                        kb_podrobnee = InlineKeyboardMarkup(row_width=1)
                        podrobnee = InlineKeyboardButton(text='Батафсил', url=final_link_news)
                        kb_podrobnee.add(podrobnee)

                        result = f'<b>Время:</b> <em>{news_time.text}</em><b>\nНазвания:</b> <em>{name_news.text}</em><b>\nОписания:</b> <em>{description.text}</em>'
                        await bot.send_photo(message.from_user.id, links_img,
                                            caption=result,
                                            parse_mode='HTML',
                                            reply_markup=kb_podrobnee)  


                elif call.data == 'buxoro':
                    url_region_buxoro = 'https://kun.uz/region/buxoro'
                    response = requests.get(url_region_buxoro)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    news = soup.find_all('div', class_='l-item')

                    await bot.send_message(message.from_user.id, "<b>Besh ta so'nggi yangiliklarni yuborish</b>")

                    time.sleep(3)

                    for new in news[:-5]:
                        news_time  = new.findChildren('span')[-1]
                        name_news  = new.findChildren('a')[-1]
                        description = new.findChildren('p')[0]
                        links_news =  new.findChildren('a')[0]
                        final_link_news = 'https://kun.uz' + links_news['href']
                        links_img = new.findChildren('img')[0]["src"]

                        kb_podrobnee = InlineKeyboardMarkup(row_width=1)
                        podrobnee = InlineKeyboardButton(text='Батафсил', url=final_link_news)
                        kb_podrobnee.add(podrobnee)

                        result = f'<b>Время:</b> <em>{news_time.text}</em><b>\nНазвания:</b> <em>{name_news.text}</em><b>\nОписания:</b> <em>{description.text}</em>'
                        await bot.send_photo(message.from_user.id, links_img,
                                            caption=result,
                                            parse_mode='HTML',
                                            reply_markup=kb_podrobnee)  


                elif call.data == 'xorazm':
                    url_region_xorazm = 'https://kun.uz/region/xorazm'
                    response = requests.get(url_region_xorazm)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    news = soup.find_all('div', class_='l-item')

                    await bot.send_message(message.from_user.id, "<b>Besh ta so'nggi yangiliklarni yuborish</b>")

                    time.sleep(3)

                    for new in news[:-5]:
                        news_time  = new.findChildren('span')[-1]
                        name_news  = new.findChildren('a')[-1]
                        description = new.findChildren('p')[0]
                        links_news =  new.findChildren('a')[0]
                        final_link_news = 'https://kun.uz' + links_news['href']
                        links_img = new.findChildren('img')[0]["src"]

                        kb_podrobnee = InlineKeyboardMarkup(row_width=1)
                        podrobnee = InlineKeyboardButton(text='Батафсил', url=final_link_news)
                        kb_podrobnee.add(podrobnee)

                        result = f'<b>Время:</b> <em>{news_time.text}</em><b>\nНазвания:</b> <em>{name_news.text}</em><b>\nОписания:</b> <em>{description.text}</em>'
                        await bot.send_photo(message.from_user.id, links_img,
                                            caption=result,
                                            parse_mode='HTML',
                                            reply_markup=kb_podrobnee)  

                elif call.data == 'qashqadaryo':
                    url_region_qashqadaryo = 'https://kun.uz/region/qashqadaryo'
                    response = requests.get(url_region_qashqadaryo)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    news = soup.find_all('div', class_='l-item')

                    await bot.send_message(message.from_user.id, "<b>Besh ta so'nggi yangiliklarni yuborish</b>")

                    time.sleep(3)

                    for new in news[:-5]:
                        news_time  = new.findChildren('span')[-1]
                        name_news  = new.findChildren('a')[-1]
                        description = new.findChildren('p')[0]
                        links_news =  new.findChildren('a')[0]
                        final_link_news = 'https://kun.uz' + links_news['href']
                        links_img = new.findChildren('img')[0]["src"]

                        kb_podrobnee = InlineKeyboardMarkup(row_width=1)
                        podrobnee = InlineKeyboardButton(text='Батафсил', url=final_link_news)
                        kb_podrobnee.add(podrobnee)

                        result = f'<b>Время:</b> <em>{news_time.text}</em><b>\nНазвания:</b> <em>{name_news.text}</em><b>\nОписания:</b> <em>{description.text}</em>'
                        await bot.send_photo(message.from_user.id, links_img,
                                            caption=result,
                                            parse_mode='HTML',
                                            reply_markup=kb_podrobnee)  

                elif call.data == 'jizzax':
                    url_region_jizzax = 'https://kun.uz/region/jizzax'
                    response = requests.get(url_region_jizzax)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    news = soup.find_all('div', class_='l-item')

                    await bot.send_message(message.from_user.id, "<b>Besh ta so'nggi yangiliklarni yuborish</b>")

                    time.sleep(3)

                    for new in news[:-5]:
                        news_time  = new.findChildren('span')[-1]
                        name_news  = new.findChildren('a')[-1]
                        description = new.findChildren('p')[0]
                        links_news =  new.findChildren('a')[0]
                        final_link_news = 'https://kun.uz' + links_news['href']
                        links_img = new.findChildren('img')[0]["src"]

                        kb_podrobnee = InlineKeyboardMarkup(row_width=1)
                        podrobnee = InlineKeyboardButton(text='Батафсил', url=final_link_news)
                        kb_podrobnee.add(podrobnee)

                        result = f'<b>Время:</b> <em>{news_time.text}</em><b>\nНазвания:</b> <em>{name_news.text}</em><b>\nОписания:</b> <em>{description.text}</em>'
                        await bot.send_photo(message.from_user.id, links_img,
                                            caption=result,
                                            parse_mode='HTML',
                                            reply_markup=kb_podrobnee)  

                elif call.data == 'sirdaryo':
                    url_region_sirdaryo = 'https://kun.uz/region/sirdaryo'
                    response = requests.get(url_region_sirdaryo)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    news = soup.find_all('div', class_='l-item')

                    await bot.send_message(message.from_user.id, "<b>Besh ta so'nggi yangiliklarni yuborish</b>")

                    time.sleep(3)

                    for new in news[:-5]:
                        news_time  = new.findChildren('span')[-1]
                        name_news  = new.findChildren('a')[-1]
                        description = new.findChildren('p')[0]
                        links_news =  new.findChildren('a')[0]
                        final_link_news = 'https://kun.uz' + links_news['href']
                        links_img = new.findChildren('img')[0]["src"]

                        kb_podrobnee = InlineKeyboardMarkup(row_width=1)
                        podrobnee = InlineKeyboardButton(text='Батафсил', url=final_link_news)
                        kb_podrobnee.add(podrobnee)

                        result = f'<b>Время:</b> <em>{news_time.text}</em><b>\nНазвания:</b> <em>{name_news.text}</em><b>\nОписания:</b> <em>{description.text}</em>'
                        await bot.send_photo(message.from_user.id, links_img,
                                            caption=result,
                                            parse_mode='HTML',
                                            reply_markup=kb_podrobnee)  

                elif call.data == 'toshkent_viloyati':
                    url_region_toshkent_viloyati = 'https://kun.uz/region/toshkent_viloyati'
                    response = requests.get(url_region_toshkent_viloyati)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    news = soup.find_all('div', class_='l-item')

                    await bot.send_message(message.from_user.id, "<b>Besh ta so'nggi yangiliklarni yuborish</b>")

                    time.sleep(3)

                    for new in news[:-5]:
                        news_time  = new.findChildren('span')[-1]
                        name_news  = new.findChildren('a')[-1]
                        description = new.findChildren('p')[0]
                        links_news =  new.findChildren('a')[0]
                        final_link_news = 'https://kun.uz' + links_news['href']
                        links_img = new.findChildren('img')[0]["src"]

                        kb_podrobnee = InlineKeyboardMarkup(row_width=1)
                        podrobnee = InlineKeyboardButton(text='Батафсил', url=final_link_news)
                        kb_podrobnee.add(podrobnee)

                        result = f'<b>Время:</b> <em>{news_time.text}</em><b>\nНазвания:</b> <em>{name_news.text}</em><b>\nОписания:</b> <em>{description.text}</em>'
                        await bot.send_photo(message.from_user.id, links_img,
                                            caption=result,
                                            parse_mode='HTML',
                                            reply_markup=kb_podrobnee)  

                elif call.data == 'navoiy':
                    url_region_navoiy = 'https://kun.uz/region/navoiy'
                    response = requests.get(url_region_navoiy)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    news = soup.find_all('div', class_='l-item')

                    await bot.send_message(message.from_user.id, "<b>Besh ta so'nggi yangiliklarni yuborish</b>")

                    time.sleep(3)

                    for new in news[:-5]:
                        news_time  = new.findChildren('span')[-1]
                        name_news  = new.findChildren('a')[-1]
                        description = new.findChildren('p')[0]
                        links_news =  new.findChildren('a')[0]
                        final_link_news = 'https://kun.uz' + links_news['href']
                        links_img = new.findChildren('img')[0]["src"]

                        kb_podrobnee = InlineKeyboardMarkup(row_width=1)
                        podrobnee = InlineKeyboardButton(text='Батафсил', url=final_link_news)
                        kb_podrobnee.add(podrobnee)

                        result = f'<b>Время:</b> <em>{news_time.text}</em><b>\nНазвания:</b> <em>{name_news.text}</em><b>\nОписания:</b> <em>{description.text}</em>'
                        await bot.send_photo(message.from_user.id, links_img,
                                            caption=result,
                                            parse_mode='HTML',
                                            reply_markup=kb_podrobnee)  

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, 
    on_startup=on_startup, on_shutdown=on_shutdown)