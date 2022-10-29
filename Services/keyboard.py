from telegram import KeyboardButton, ReplyKeyboardMarkup


def create_button(text: str) -> KeyboardButton:
    button = KeyboardButton(text=text, callback_data=text)
    return button


def create_markup(city_name: str) -> ReplyKeyboardMarkup:
    buttons = ReplyKeyboardMarkup([[create_button(city_name)]], resize_keyboard=True)
    return buttons
