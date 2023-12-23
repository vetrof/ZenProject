import telebot

# Замените 'YOUR_BOT_TOKEN' на реальный токен вашего бота
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

# Словарь для хранения текста сообщений пользователей
user_messages = {}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я бот. Напиши мне что-то.")

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    # Если пользователь отправил текстовое сообщение
    if message.text:
        # Сохраняем текст сообщения в словаре
        user_messages[message.chat.id] = message.text

        # Создаем клавиатуру
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

        # Создаем кнопку "Отправить сообщение"
        button_send_message = telebot.types.KeyboardButton('Отправить сообщение')

        # Добавляем кнопку на клавиатуру
        markup.add(button_send_message)

        # Отправляем клавиатуру с кнопкой пользователю
        bot.send_message(message.chat.id, "Текст сохранен. Нажми на кнопку для отправки.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Отправить сообщение')
def send_message_button_handler(message):
    # Получаем текст сообщения из словаря
    user_message = user_messages.get(message.chat.id, 'Текст не найден.')

    # Отправляем сообщение с сохраненным текстом
    bot.send_message(message.chat.id, f"Текст для отправки: {user_message}")
