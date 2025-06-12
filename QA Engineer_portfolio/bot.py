import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile
from config import TOKEN
from keyboards import main_menu, back_button

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Стартовое приветствие с фото
@dp.message(lambda message: message.text == "/start")
async def start_command(message: types.Message):
    try:
        photo = FSInputFile("images/elena2.jpg")
        await message.answer_photo(
            photo,
            caption=(
                "👋 Привет! Я **Елена Заподойникова**, QA Engineer.\n"
                "Опыт: 4+ года в тестировании мобильных и веб-приложений.\n"
                "Воспользуйся меню ниже, чтобы узнать обо мне больше 👇"
            ),
            parse_mode="Markdown",
            reply_markup=main_menu
        )
    except Exception:
        await message.answer("❌ Фото не найдено! Убедись, что файл images/elena.jpg существует.")
        await message.answer("📌 Главное меню:", reply_markup=main_menu)

from aiogram.types import FSInputFile

@dp.callback_query(lambda c: c.data == "about")
async def about_handler(callback_query: types.CallbackQuery):
    # Сначала приветственный текст
    await callback_query.message.answer(
        "🔹 <b>О себе:</b>\n\n"
        "Привет! Я Елена, QA Engineer (ручное и автотестирование мобильных/веб-приложений).\n"
        "4+ года опыта, автоматизация, поиск багов, люблю свою работу 🫶\n\n"
        "👇 <b>Познакомься со мной лично — видео ниже!</b>",
        parse_mode="HTML",
        reply_markup=back_button
    )
    # Потом отправь видео-файл
    video = FSInputFile("media/lena.mp4")  # путь к видеофайлу
    await callback_query.message.answer_video(
        video,
        caption="👋 Привет! Я Елена, расскажу немного о себе.",
        parse_mode="HTML"
    )

@dp.callback_query(lambda c: c.data == "skills")
async def skills_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer(
        "<b>🛠️ Мои навыки:</b>\n"
        "- Тест-дизайн (чек-листы, тест-кейсы)\n"
        "- Jira, YouTrack, баг-трекинг\n"
        "- Postman, DevTools, Charles\n"
        "- Автотесты: PyTest, Selenium\n"
        "- SQL, API, REST\n"
        "- Документирование багов, создание отчетов\n"
        "- Git, GitHub Actions\n"
        "\n"
        "<b>🦾 QA Стэк:</b>\n"
        "API, Postman, DevTools, TestIT, Allure, Cypress, Pytest, Sentry,\n"
        "Grafana, Swagger, SOAP UI, Jmeter, Git, Jira, Agile, Python, HTML,\n"
        "CSS, Selenium, PostgreSQL, Android Studio, Kafka, CI/CD, Docker, Charles,\n"
        "REST, Kibana",
        parse_mode="HTML",
        reply_markup=back_button
    )

from aiogram.types import FSInputFile

@dp.callback_query(lambda c: c.data == "projects")
async def projects_handler(callback_query: types.CallbackQuery):
    # 1. Сначала фото (например, твой портрет или что-то символическое)
    photo = FSInputFile("images/qacat.jpg")  # путь к нужному фото
    await callback_query.message.answer_photo(
        photo,
        caption="📂 Моё портфолио (ниже подробнее 👇)",
        reply_markup=None  # Можно без клавиатуры для фотки
    )
    # 2. Потом — текст с кнопкой
    await callback_query.message.answer(
        "📂 Примеры проектов:\n"
        "- проводила функциональное, регрессионное, UX, интеграционное, кроссбраузерное (включая кастомные модули сравнения и подбора товаров), API-тестирование web и мобильного приложения на проекте Аскона (фильтры, админка для автоматического распределения товаров по категориям); тестировала админку сайта: проверяла бизнес-логику автоматического распределения матрасов по категориям по тегам, верифицировала отображение и работу фильтрации в каталоге (на проекте использовалась собственная админ-панель для управления\ товарами (матрасами, диванами и т. д.), построенная на headless CMS Strapi, которая получала данные из 1С. Админка позволяла менеджерам не вручную распределять карточки по разделам, а использовать теги, на основе которых система автоматически размещала товары в нужных категориях сайта. Это ускоряло работу контент-команды и снижало вероятность ошибок)\n"
        " - проводила тестирование каталога, проверяла расчёт стоимости полисов, личный кабинет, интеграций с базой клиентов и внешними API\n"
        "- Автоматизация API: автотесты на PyTest\n"
        "- GitHub: https://github.com/elenazapodoynikovaQA",
        reply_markup=back_button
    )

# Полезная теория
@dp.callback_query(lambda c: c.data == "theory")
async def theory_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer(
        "📚 Полезная теория для QA инженера:\n"
        "[Charles Proxy для начинающих тестировщиков: установка, HTTPS-сертификаты, кейсы и альтернативы (vc.ru)](https://vc.ru/dev/1995257-charles-proxy-dlya-testirovshchikov)\n"
        "[Тестирование неочевидного: баги в фильтрах, UX и логике подбора товаров (vc.ru)](https://vc.ru/dev/2025478-testirovanie-filtrov-tovarov-bagi-ux-i-logika-podbora)\n"
        "[Яндекс.Диск: материалы для QA, шпаргалки](https://disk.yandex.ru/d/NDqHxCmLyHzAng)\n"
        "✨ Подборка пополняется ✨",
        parse_mode="Markdown",
        reply_markup=back_button
    )

# Контакты
@dp.callback_query(lambda c: c.data == "contacts")
async def contacts_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer(
        "📞 Контакты для связи:\n"
        "Telegram: @Elneuro83\n"
        "Email: lenazew283@gmail.com",
        reply_markup=back_button
    )

# Назад в главное меню
@dp.callback_query(lambda c: c.data == "main_menu")
async def back_to_main(callback_query: types.CallbackQuery):
    await callback_query.message.answer("📌 Главное меню:", reply_markup=main_menu)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
