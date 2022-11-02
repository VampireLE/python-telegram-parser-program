from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests
from bs4 import BeautifulSoup
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

data_time = []
data_name = []
last_result = []

def clear_list():
    data_time.clear()
    data_name.clear()
    last_result.clear()

def get_page(number_channel):
    
    headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    }
    url = 'https://tv.mail.ru/moskva/'

    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    channels_item = soup.find_all('div', class_='p-channels__item')

    channel(channels_item)
    main(number_channel)

def channel(channels_item):
    for program in channels_item:
        name = program.find_all('span', class_='p-programms__item__name')
        time = program.find_all('span', class_='p-programms__item__time')
        for times in time:
            data_time.append(times.text)
        for names in name:
            data_name.append(names.text)
    

def main(number_channel):

    second = (number_channel * 5)
    first = (second - 5)
    for broadcast, transmission_time in zip(data_name[first:second], data_time[first:second]):
        result = (transmission_time, "-", broadcast)
        result = " ".join(result)
        last_result.append(result)
    global a
    a = "\n".join(last_result)
    

#----------------------------------BOT---------------------------------------------------------------

print("Hello")

API = '5215475103:AAHRpCQtSEhgNutKoMKfcQgy7HiydY5fxME'
bot = Bot(API)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await message.answer("Привет!\nЭто бот который показывает тв программу\nВведи команду - /show чтобы узнать тв программу")


inline_btn_1 = InlineKeyboardButton('Первый канал', callback_data='1')
inline_btn_2 = InlineKeyboardButton('Россия 1', callback_data='2')
inline_btn_3 = InlineKeyboardButton('МАТЧ!', callback_data='3')
inline_btn_4 = InlineKeyboardButton('НТВ', callback_data='4')
inline_btn_5 = InlineKeyboardButton('ТВ Центр', callback_data='5')
inline_btn_6 = InlineKeyboardButton('Культура', callback_data='6')
inline_btn_7 = InlineKeyboardButton('СТС', callback_data='7')
inline_btn_8 = InlineKeyboardButton('РЕН ТВ', callback_data='8')
inline_btn_9 = InlineKeyboardButton('ОТР', callback_data='9')
inline_btn_10 = InlineKeyboardButton('ТНТ', callback_data='10')
inline_btn_11 = InlineKeyboardButton('Dомашний', callback_data='11')
inline_btn_12 = InlineKeyboardButton('Россия 24', callback_data='12')
inline_btn_13 = InlineKeyboardButton('Че', callback_data='13')
inline_btn_14 = InlineKeyboardButton('ТВ-3', callback_data='14')
inline_btn_15 = InlineKeyboardButton('Пятница', callback_data='15')
inline_btn_16 = InlineKeyboardButton('5 канал', callback_data='16')
inline_btn_17 = InlineKeyboardButton('Ю', callback_data='17')
inline_btn_18 = InlineKeyboardButton('Звезда', callback_data='18')
inline_btn_19 = InlineKeyboardButton('РБК', callback_data='19')
inline_btn_20 = InlineKeyboardButton('Суббота', callback_data='20')
inline_btn_21 = InlineKeyboardButton('Карусель', callback_data='21')
inline_btn_22 = InlineKeyboardButton('2x2', callback_data='22')
inline_btn_23 = InlineKeyboardButton('СТС Love', callback_data='23')
inline_btn_24 = InlineKeyboardButton('Disney', callback_data='24')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4, inline_btn_5, inline_btn_6, inline_btn_7, inline_btn_8, inline_btn_9, inline_btn_10, inline_btn_11, inline_btn_12, inline_btn_13, inline_btn_14, inline_btn_15, inline_btn_16, inline_btn_17, inline_btn_18, inline_btn_19, inline_btn_20, inline_btn_21, inline_btn_22, inline_btn_23, inline_btn_24)

@dp.message_handler(commands=["show"])
async def process_command_1(message:types.Message):
    await message.answer("Выберите канал:", reply_markup=inline_kb1)

@dp.callback_query_handler()
async def send_parse(callback: types.CallbackQuery):
    if callback.data == "15":
        clear_list()
        get_page(15)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "2":
        clear_list()
        get_page(2)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "3":
        clear_list()
        get_page(3)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "4":
        clear_list()
        get_page(4)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "5":
        clear_list()
        get_page(5)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "6":
        clear_list()
        get_page(6)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "7":
        clear_list()
        get_page(7)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "8":
        clear_list()
        get_page(8)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "9":
        clear_list()
        get_page(9)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "10":
        clear_list()
        get_page(10)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "11":
        clear_list()
        get_page(11)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "12":
        clear_list()
        get_page(12)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "13":
        clear_list()
        get_page(13)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "14":
        clear_list()
        get_page(14)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "1":
        clear_list()
        get_page(1)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "16":
        clear_list()
        get_page(16)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "17":
        clear_list()
        get_page(17)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "18":
        clear_list()
        get_page(18)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "19":
        clear_list()
        get_page(19)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "20":
        clear_list()
        get_page(20)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "21":
        clear_list()
        get_page(21)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "22":
        clear_list()
        get_page(22)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "23":
        clear_list()
        get_page(23)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "24":
        clear_list()
        get_page(24)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)

    elif callback.data == "25":
        clear_list()
        get_page(25)
        await callback.answer()
        return await callback.message.edit_text(a, reply_markup=inline_kb1)


# if __name__ == '__main__':
executor.start_polling(dp)
