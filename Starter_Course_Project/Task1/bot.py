import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
import os
import json
import pyjokes
import random
from prettytable import PrettyTable

#Specify your token here#
TOKEN = ''

bot = telebot.TeleBot(TOKEN)
bot.set_my_commands(
        commands=[
            BotCommand('/games', 'Зіграти у гру'),
            BotCommand('/jokes', 'Анекдоти/Цікаві історії'),
            BotCommand('/advice', 'Рекомендації фільмів/музики')
        ])
 
FUN_HISTORY_PATH = os.path.join(os.path.abspath(__file__ + '/..'), 'fun_histrory.json')

try:
    with open(FUN_HISTORY_PATH, 'r' ) as f:
        fun_histrory = json.load(f)
except:
    fun_histrory = None

@bot.message_handler(commands=['start'])
def start(message: Message):
    text = "Вітаю в розважальному чат-боті!\n\n"
    text += "/games - Зіграти у гру\n"
    text += "/jokes - Анекдоти/Цікаві історії\n"
    text += "/advice - Рекомендації фільмів/музики/ігор\n"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['jokes'])
def jokes(message: Message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton(text="Анекдот 😁", callback_data="joke")
    button2 = InlineKeyboardButton(text="Цікава історія 🤓", callback_data="history")
    keyboard.add(button1,button2)
    bot.send_message(message.chat.id, "Обери дію: 👇", reply_markup=keyboard)

@bot.message_handler(commands=['games'])
def games(message: Message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton(text="Камінь Ножиці Папір 🙃", callback_data="rps")
    button2 = InlineKeyboardButton(text="Вгадай число 🤔", callback_data="guess_number")
    keyboard.add(button1,button2)
    bot.send_message(message.chat.id, "Обери гру: 👇", reply_markup=keyboard)

@bot.message_handler(commands=['advice'])
def advice(message: Message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton(text="Фільми 🎬", callback_data="r_movie")
    button2 = InlineKeyboardButton(text="Музика 🎸", callback_data="r_music")
    keyboard.add(button1,button2)
    bot.send_message(message.chat.id, "Обери напрямок: 👇", reply_markup=keyboard)

def rps(message: Message):
    bot.send_message(message.chat.id, 'Гра "Камінь Ножиці Папір"')   
    keyboard = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton(text="Камінь 🪨", callback_data="rock")
    button2 = InlineKeyboardButton(text="Ножиці 🗒", callback_data="scissors")
    button3 = InlineKeyboardButton(text="Папір ✂", callback_data="paper")
    keyboard.add(button1,button2, button3)
    bot.send_message(message.chat.id, "Обери: камінь, ножиці або папір: 👇", reply_markup=keyboard)
    
def guess_number(message: Message):
    bot.send_message(message.chat.id, 'Гра "Вгадай число"')  
    keyboard = InlineKeyboardMarkup(row_width=5)
    button1 = InlineKeyboardButton(text="1️⃣", callback_data="1")
    button2 = InlineKeyboardButton(text="2️⃣", callback_data="2")
    button3 = InlineKeyboardButton(text="3️⃣", callback_data="3")
    button4 = InlineKeyboardButton(text="4️⃣", callback_data="4")
    button5 = InlineKeyboardButton(text="5️⃣", callback_data="5")
    keyboard.add(button1,button2, button3, button4, button5)
    bot.send_message(message.chat.id, "Обери число: 👇", reply_markup=keyboard)

def play_again(message: Message, game_type: str):
    keyboard = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton(text="Так ✅", callback_data=game_type)
    button2 = InlineKeyboardButton(text="Вибрати гру 🎲", callback_data="games")
    keyboard.add(button1,button2)
    bot.send_message(message.chat.id, "Зіграти ще раз? 😁", reply_markup=keyboard)

def recommend_movies(message: Message):
    table = PrettyTable()
    table.field_names = ["Фільм", "Жанр", "Рік"]
    table.add_row(["Інтерстеллар", "Наукова фантастика", "2014"])
    table.add_row(["Невидимий гість", "Трилер", "2016"])
    table.add_row(["Гра в імітацію", "Біографія, Драма", "2014"])
    bot.send_message(message.chat.id, "Ось декілька рекомендованих фільмів: 👇")
    for row in table:
        bot.send_message(message.chat.id, f"{row.get_string()}")

def recommend_music(message: Message):
    table = PrettyTable()
    table.field_names = ["Композиція", "Виконавець", "Рік"]
    table.add_row(["Thunder", "Imagine Dragons", "2017"])
    table.add_row(["Nothing Else Matters", "Metallica", "1991"])
    table.add_row(["Back to Black", "Amy Winehouse ", "2006"])
    bot.send_message(message.chat.id, "Ось декілька музичних рекомендацій: 👇")
    for row in table:
        bot.send_message(message.chat.id, f"{row.get_string()}")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "joke":
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            joke = pyjokes.get_joke(language="ru", category="neutral")
            bot.send_message(call.message.chat.id, f"<b> {joke} </b>", parse_mode='HTML')
        elif call.data == "history":
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            if fun_histrory:
                history = (random.randint(0,len(fun_histrory)-1))
                bot.send_message(call.message.chat.id, f"{fun_histrory[history]}", parse_mode='HTML')
            else:
                bot.send_message(call.message.chat.id, "На жаль зараз немає історій, спробуй пізніше", parse_mode='HTML')
        elif call.data == "rps":
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            rps(call.message)
        elif call.data == "guess_number":
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            guess_number(call.message)
        elif call.data in ("rock", "scissors", "paper"):
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            options = ['Камінь 🪨', 'Ножиці 🗒', 'Папір ✂']
            computer_choice = random.choice(options)            
            match call.data:
                case "rock" : user_choice = "Камінь 🪨"
                case "scissors" : user_choice = "Ножиці 🗒"
                case "paper" : user_choice = "Папір ✂"
            bot.send_message(call.message.chat.id, f"Ти вибрав: {user_choice}")   
            bot.send_message(call.message.chat.id, f"Комп'ютер обрав: {computer_choice}")
            if user_choice == computer_choice:
                bot.send_message(call.message.chat.id, "Нічия! 🤝")
            elif (user_choice == 'Камінь' and computer_choice == 'Ножиці') or \
                (user_choice == 'Ножиці' and computer_choice == 'Папір') or \
                (user_choice == 'Папір' and computer_choice == 'Камінь'):
                bot.send_message(call.message.chat.id, "Ти переміг! ✌")
            else:
                bot.send_message(call.message.chat.id, "Ти програв! 😔")
            play_again(call.message, "rps")            
        elif call.data in ("1", "2", "3", "4", "5"):
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            user_choice = int(call.data)
            computer_choice = random.randint(1, 5)          
            bot.send_message(call.message.chat.id, f"Ти вибрав: {user_choice}")   
            bot.send_message(call.message.chat.id, f"Комп'ютер обрав: {computer_choice}")
            if user_choice == computer_choice:
                bot.send_message(call.message.chat.id, "Ти вгадав, вітаю! ✌")
            else:
                bot.send_message(call.message.chat.id, "Ти не вгадав, спробуй ще раз 😔")
            play_again(call.message, "guess_number")
        elif call.data == "games":
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            games(call.message)
        elif call.data == "r_movie":
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            recommend_movies(call.message)
        elif call.data == "r_music":
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            recommend_music(call.message)
        
bot.infinity_polling()