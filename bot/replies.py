import telebot
from emoji import emojize


def years_markup():
    keyboard = telebot.types.InlineKeyboardMarkup()
    for year in range(2017, 2023): # TODO: add time.now.year
        key = telebot.types.InlineKeyboardButton(text=str(year), callback_data=str(year))
        keyboard.add(key)
    # Add button for going back
    key_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data="back")
    #keyboard.add(key_back)
    return keyboard


def countries_markup():
    keyboard = telebot.types.InlineKeyboardMarkup()

    key = telebot.types.InlineKeyboardButton(text=f"Россия {emojize(':Russia:')}", callback_data="1")
    keyboard.add(key)
    key = telebot.types.InlineKeyboardButton(text=f"Казахстан {emojize(':Kazakhstan:')}", callback_data="1")
    keyboard.add(key)
    key = telebot.types.InlineKeyboardButton(text=f"Беларусь {emojize(':Belarus:')}", callback_data="1")
    keyboard.add(key)
    key = telebot.types.InlineKeyboardButton(text=f"Украина {emojize(':Ukraine:')}", callback_data="1")
    keyboard.add(key)
    # Add button for going back
    key_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data="back")
    #keyboard.add(key_back)
    return keyboard


def direction_markup():
    keyboard = telebot.types.InlineKeyboardMarkup()

    key = telebot.types.InlineKeyboardButton(text="Потенция ", callback_data="1")
    keyboard.add(key)
    key = telebot.types.InlineKeyboardButton(text="Похудение ", callback_data="1")
    keyboard.add(key)
    key = telebot.types.InlineKeyboardButton(text="Суставы ", callback_data="1")
    keyboard.add(key)
    key = telebot.types.InlineKeyboardButton(text="и тд) ", callback_data="1")
    keyboard.add(key)
    # Add button for going back
    key_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data="back")
    #keyboard.add(key_back)

    return keyboard
