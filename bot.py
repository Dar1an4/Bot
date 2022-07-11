# Учусть писать код. Попытка создания бота напоминалки о ДР. БД на основе словаря.....))
import datetime
import time

from aiogram import Bot, Dispatcher, executor, types

TOKEN = 'TOKEN'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Привет!\n введите команду /help, что бы ознакомиться со списокм команд!")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("Доступны следующие функции:\n - /bthrdaynow - день рождения в ближайшие дни \n - "
                         "/bthrdaycheck - автоматическое напоминание о ДР из БД \n - /showlist - показать список ДРОВ"
                         " ")

d = datetime.timedelta(days=1)

wook = {
    'Степан': 20220709,
    'Алексей': 20220710,
    'Питер': 20220711,
    'Ворон': 20220713,
}
b = wook.values()

inv_wook = {}
c = inv_wook
for key, value in wook.items():
    inv_wook[value] = key

@dp.message_handler(commands=['showlist'])
async def process_showlist_command(message: types.Message):
    await message.answer(wook)

@dp.message_handler(commands=['bthrdaynow'])
async def process_bthrdaynow_command(message: types.Message):
    await message.answer("Показываю список ДРов:")
    if int(datetime.datetime.today().strftime("%Y%m%d")) in b:
        await message.answer("Сегодня день рождения у него: ")
        await message.answer(inv_wook[int(datetime.datetime.today().strftime("%Y%m%d"))])
    tomorroww = datetime.datetime.today() + datetime.timedelta(days=1)
    tomorrow = int(tomorroww.strftime("%Y%m%d"))
    if tomorrow in b:
        await message.answer("Завтра день рождения у него: ")
        await message.answer(inv_wook[tomorrow])

@dp.message_handler(commands=['bthrdaycheck'])
async def process_bthrdaycheck_command(message: types.Message):
    await message.answer("Автоматическое напоминанеие о днях рождения включено!")
    while True:
        if int(datetime.datetime.now().strftime("%H%M")) == 2259:
            if int(datetime.datetime.today().strftime("%Y%m%d")) in b:
                await message.answer("Сегодня день рождения у него: ")
                await message.answer(inv_wook[int(datetime.datetime.today().strftime("%Y%m%d"))])
            tomorrow1 = datetime.datetime.today() + datetime.timedelta(days=1)
            tomorrow2 = int(tomorrow1.strftime("%Y%m%d"))
            if tomorrow2 in b:
                await message.answer("Завтра день рождения у него: ")
                await message.answer(inv_wook[tomorrow2])
            time.sleep(32)
        else:
            time.sleep(32)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)