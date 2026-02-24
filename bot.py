import telebot
import os

TOKEN = os.getenv("8367825042:AAHmyhnTn3s8Yz18c8WSHttZoTWsY7mNwgY")

bot = telebot.TeleBot(8367825042:AAHmyhnTn3s8Yz18c8WSHttZoTWsY7mNwgY)

users = {}

def get_points(uid):
    return users.get(uid, 0)

@bot.message_handler(commands=['start'])
def start(msg):
    kb = telebot.types.InlineKeyboardMarkup()
    kb.add(telebot.types.InlineKeyboardButton("Мій баланс", callback_data="bal"))
    kb.add(telebot.types.InlineKeyboardButton("Рейтинг", callback_data="rate"))
    bot.send_message(msg.chat.id,"Меню",reply_markup=kb)

@bot.callback_query_handler(func=lambda c: True)
def cb(c):

    if c.data=="bal":
        p=get_points(c.from_user.id)
        bot.answer_callback_query(c.id)
        bot.send_message(c.message.chat.id,f"Баланс: {p}")

    if c.data=="rate":
        txt="🏆 Рейтинг\n\n"
        sorted_users=sorted(users.items(),key=lambda x:x[1],reverse=True)
        for i,(uid,p) in enumerate(sorted_users[:10]):
            txt+=f"{i+1}. {uid} — {p}\n"
        if not sorted_users:
            txt="Поки пусто"
        bot.answer_callback_query(c.id)
        bot.send_message(c.message.chat.id,txt)

bot.infinity_polling()
