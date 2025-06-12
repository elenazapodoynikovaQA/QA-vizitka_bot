from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔹 О себе", callback_data="about")],
    [InlineKeyboardButton(text="🛠 Навыки", callback_data="skills")],
    [InlineKeyboardButton(text="📂 Портфолио", callback_data="projects")],
    [InlineKeyboardButton(text="📚 Полезная теория", callback_data="theory")],
    [InlineKeyboardButton(text="📞 Контакты", callback_data="contacts")],
])

back_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="main_menu")]
])
