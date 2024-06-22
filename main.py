import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode, ContentType, ChatAction
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TELEGRAM_BOT_API_TOKEN
import db
import text_generation_model


logging.basicConfig(level=logging.INFO)


dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: Message):
    await message.answer('Привет я бот-момот, идеальный компаньон для твоего чаты. Вы можете добавить меня в группу.')


@dp.message()
async def handle_text(message: Message):
    if message.content_type != ContentType.TEXT:
        pass

    await db.create_message(message.chat.id, message.text, message.from_user.id, message.from_user.is_bot)
    last_messages = await db.get_messages_by(message.chat.id, limit=20)
    last_messages.reverse()
    history = [(msg[4], msg[2]) for msg in last_messages]

    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)

    response = text_generation_model.generate(history).replace('.', '').strip() or 'хуй'
    bot_message = await message.bot.send_message(message.chat.id, response)
    await db.create_message(bot_message.chat.id, bot_message.text, bot_message.from_user.id,
                            bot_message.from_user.is_bot)


async def main() -> None:
    await db.db_init()

    bot = Bot(token=TELEGRAM_BOT_API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


try:
    if __name__ == '__main__':
        asyncio.run(main())
except KeyboardInterrupt:
    print('Бот остановлен')
