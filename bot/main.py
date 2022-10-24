import telebot
from bot.state import *
from bot.replies import years_markup, countries_markup, direction_markup
from pyqiwip2p import QiwiP2P

# from pyqiwip2p.p2p_types import QiwiCustomer, QiwiDatetime, PaymentMeth

bot = telebot.TeleBot('5606754843:AAElr9IYXFMPNsiDUzxeu9JykqMQpzmPEWM')
key = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6Im9rMHFjNC0wMCIsInVzZXJfaWQiOiI3OTE2MjY4NzkxMSIsInNlY3JldCI6ImU5MzU0YzQxZmFhMGMwOTY3NWY3MzBiMTgwYjUxOGFjMDMyYTI0NGEyZDg1OGY5MzY2Nzc0OTc1YjhiMTgzODAifX0="
p2p = QiwiP2P(auth_key=key)
states = {}


@bot.message_handler(commands=['start'])
def start(message):
    user = message.chat.id
    states[user] = State()

    bot.send_message(user, 'Это бот для продажи тестов...')
    bot.send_message(user, 'Выбери год', reply_markup=years_markup())
    states[user].go_next()


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    print(call.data)
    # Get user from call and his state
    user = call.from_user.id
    user_state = states[user].state_now

    if call.data == "back":
        states[user].go_back()

    if user_state == YEAR_SELECTION_STATE:
        bot.send_message(user, 'Выбери год', reply_markup=years_markup())
        states[user].go_next()

    elif user_state == COUNTRY_SELECTION_STATE:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выбери страну',
                              reply_markup=countries_markup())
        # bot.send_message(user, 'Выбери страну', reply_markup=countries_markup())
        states[user].go_next()
    elif user_state == DIRECTION_SELECTION_STATE:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выбери направление',
                              reply_markup=direction_markup())
        # bot.send_message(user, 'Выбери направление', reply_markup=direction_markup())
        states[user].go_next()
        # TODO: delete later
        states[user].go_next()
    elif user_state == MEDICINE_SELECTION_STATE:
        # TODO: change for correct version
        pass
    elif user_state == PAYMENT_STATE:
        comment = "Тестовая оплата для бота)"
        bill = p2p.bill(amount=1, lifetime=10, comment=comment)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f"Произведите оплату по ссылке\n{bill.pay_url}")
        # bot.send_message(user, f"Произведите оплату по ссылке\n{bill.pay_url}")
        pass
    else:  # Something went bad
        print("bad state")


def run_bot():
    bot.polling(none_stop=True, interval=0)
