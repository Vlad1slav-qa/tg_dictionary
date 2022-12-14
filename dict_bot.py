# В google colab добавить: !pip install pyTelegramBotAPI
# Чтобы добавить новое слово — нужно его прописать в массиве DEFINITOINS на 11 строчке
# Важно все новые аббривиатуры в коде писать только с маленьких букв
# Пользователь в телеграм может писать и с большой и с маленькой — код всегда приводит к строчным

from telebot import TeleBot, types

bot = TeleBot(token='Вставить_свой_токен', parse_mode='html') # создание бота

# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'ключевая фраза': 'соответствующее ей определение'
DEFINITOINS = {
    'регресс': 'Проверка, что новый функционал не сломал уже существующий.',
    'смоук': 'Краткая выжимка самых критичных тест-кейсов.',
    'чек-лист': 'Общее количество проверок без детализации.',
    'тест-кейс': 'Четкое описание действий, которые необходимо выполнить для проверки функционала.',
    'ручка': 'HTTP запрос',
    'quality assurance': 'QA - контроль качества. Включает в себя QC  и testing. Тестировщик отвечает за прохождение чек-листов, тест-кейсов, проверку и документирование дефектов, разработку документации. Quality Control в дополнение к обязанностям тестировщика анализирует результаты тестирования и качество билдов,  выявляет причины отклонений. Quality Assuranse анализирует весь проект и процессы,  превентивно работает над улучшением качества продукта.',
    'сборка': 'Подготовленая к использованию/тестированию версия ПО (например, Chrome ver 105.xxxxx)',
    'клиент-серверная архитектура': 'Взаимодействие клиента, бэкенда и БД. Клиент - визуал, бэкенд - логика, БД - данные.  Клиент-сервер общаются через HTTP запросы и ответы. Бэкенд с БД общаются с помощью SQL запросов и ответов',
    'qa': 'QA - контроль качества. Включает в себя QC  и testing. Тестировщик отвечает за прохождение чек-листов, тест-кейсов, проверку и документирование дефектов, разработку документации. Quality Control в дополнение к обязанностям тестировщика анализирует результаты тестирования и качество билдов, выявляет причины отклонений. Quality Assuranse анализирует весь проект и процессы, превентивно работает над улучшением качества продукта.',
    'тест-дизайн': 'Процесс, который помогает ограничить количество тест-кейсов',
}

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет! Я помогу тебе расшифровать сложные аббревиатуры и термины 🤓\nВведи интересующий термин, например, регресс', # текст сообщения
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # пробуем найти ключевую фразу в словаре
    definition = DEFINITOINS.get(
        message.text.lower(), # приводим текст сообщения к нижнему регистру
    )
    # если фразы нет в словаре, то переменная definition будет иметь значение None
    # проверяем это условие
    if definition is None:
        # если ключевая фраза не была найдена в словаре
        # отправляем ответ
        bot.send_message(
            chat_id=message.chat.id,
            text='😋 Я пока не знаю такого определения',
        )
        # выходим из функции
        return
    
    # если ключевая фраза была найдена, формируем текст сообщения и отправляем его
    # если перед строкой поставить букву f, то в фигурных скобках {} можно использовать переменные :)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Жду следующий термин',
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
