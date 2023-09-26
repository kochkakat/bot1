import telebot

TOKEN = '6355288960:AAEDimP3GcD4U2_gZ2blsm2M0okw0UPvw6w'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Хочешь карту?).")

import telebot
from telebot import types
import os
import random

@bot.message_handler(content_types=['text'])
def start(message):
  photo = open('test/' + random.choice(os.listdir('test')), 'rb')
  bot.send_photo(message.from_user.id, photo)
  markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn = telebot.types.KeyboardButton('Хочу карту')
  markup.row(btn)
  bot.send_message(message.chat.id, 'Если хочешь ещё карту, пиши "Хочу карту" или нажимай на кнопку внизу', reply_markup=markup)
  
  
  
bot.polling()