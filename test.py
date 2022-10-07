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
word = ("Загружаю программу...")

def get_page(number_channel):
	
	headers = {
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
	}
	url = 'https://tv.mail.ru/moskva/'

	r = requests.get(url=url, headers=headers)
	soup = BeautifulSoup(r.text, 'lxml')
	channels_item = soup.find_all('div', class_='p-channels__item')

	channel(channels_item)
	mainp(number_channel)

def channel(channels_item):
	for program in channels_item:
		name = program.find_all('span', class_='p-programms__item__name')
		time = program.find_all('span', class_='p-programms__item__time')
		for times in time:
			data_time.append(times.text)
		for names in name:
			data_name.append(names.text)
	

def mainp(number_channel):

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
inline_btn_9 = InlineKeyboardButton('ТНТ', callback_data='9')
inline_btn_10 = InlineKeyboardButton('Dомашний', callback_data='10')
inline_btn_11 = InlineKeyboardButton('Россия 24', callback_data='11')
inline_btn_12 = InlineKeyboardButton('Че', callback_data='12')
inline_btn_13 = InlineKeyboardButton('ТВ-3', callback_data='13')
inline_btn_14 = InlineKeyboardButton('Пятница!', callback_data='14')
inline_btn_15 = InlineKeyboardButton('5 канал', callback_data='15')
inline_btn_16 = InlineKeyboardButton('Ю', callback_data='16')
inline_btn_17 = InlineKeyboardButton('Звезда', callback_data='17')
inline_btn_18 = InlineKeyboardButton('РБК', callback_data='18')
inline_btn_19 = InlineKeyboardButton('Суббота!', callback_data='19')
inline_btn_20 = InlineKeyboardButton('Карусель', callback_data='20')
inline_btn_21 = InlineKeyboardButton('2x2', callback_data='21')
inline_btn_22 = InlineKeyboardButton('СТС Love', callback_data='22')
inline_btn_23 = InlineKeyboardButton('Disney', callback_data='23')
inline_btn_24 = InlineKeyboardButton('Карусель', callback_data='24')
inline_btn_25 = InlineKeyboardButton('МИР', callback_data='25')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4, inline_btn_5, inline_btn_6, inline_btn_7, inline_btn_8, inline_btn_9, inline_btn_10, inline_btn_11, inline_btn_12, inline_btn_13, inline_btn_14, inline_btn_15, inline_btn_16, inline_btn_17, inline_btn_18, inline_btn_19, inline_btn_20, inline_btn_21, inline_btn_22, inline_btn_23, inline_btn_24, inline_btn_25)

@dp.message_handler(commands=["show"])
async def process_command_1(message:types.Message):
	await message.answer("Выберите канал:", reply_markup=inline_kb1)

@dp.callback_query_handler(text='1')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(1)
	await callback.message.answer(a)

@dp.callback_query_handler(text='2')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(2)
	await callback.message.answer(a)

@dp.callback_query_handler(text='3')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(3)
	await callback.message.answer(a)

@dp.callback_query_handler(text='4')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(4)
	await callback.message.answer(a)

@dp.callback_query_handler(text='5')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(5)
	await callback.message.answer(a)

@dp.callback_query_handler(text='6')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(6)
	await callback.message.answer(a)

@dp.callback_query_handler(text='7')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(7)
	await callback.message.answer(a)

@dp.callback_query_handler(text='8')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(8)
	await callback.message.answer(a)

@dp.callback_query_handler(text='9')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(9)
	await callback.message.answer(a)

@dp.callback_query_handler(text='10')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(10)
	await callback.message.answer(a)

@dp.callback_query_handler(text='11')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(11)
	await callback.message.answer(a)

@dp.callback_query_handler(text='12')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(12)
	await callback.message.answer(a)

@dp.callback_query_handler(text='13')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(13)
	await callback.message.answer(a)

@dp.callback_query_handler(text='14')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(14)
	await callback.message.answer(a)

@dp.callback_query_handler(text='15')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(15)
	await callback.message.answer(a)

@dp.callback_query_handler(text='16')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(16)
	await callback.message.answer(a)

@dp.callback_query_handler(text='17')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(17)
	await callback.message.answer(a)

@dp.callback_query_handler(text='18')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(18)
	await callback.message.answer(a)

@dp.callback_query_handler(text='19')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(19)
	await callback.message.answer(a)

@dp.callback_query_handler(text='20')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(20)
	await callback.message.answer(a)

@dp.callback_query_handler(text='21')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(21)
	await callback.message.answer(a)

@dp.callback_query_handler(text='22')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(22)
	await callback.message.answer(a)

@dp.callback_query_handler(text='23')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(23)
	await callback.message.answer(a)

@dp.callback_query_handler(text='24')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(24)
	await callback.message.answer(a)

@dp.callback_query_handler(text='25')
async def send_random_value(callback: types.CallbackQuery):
	await callback.message.answer(word)
	data_time.clear()
	data_name.clear()
	last_result.clear()
	get_page(25)
	await callback.message.answer(a)


# if __name__ == '__main__':
executor.start_polling(dp)
