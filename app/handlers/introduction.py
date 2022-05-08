from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.utils.text_decorations import html_decoration as html


async def start_cmd(m: Message):
    first_name = html.quote(m.from_user.first_name)
    text = (
        f"Hello, {first_name}!\n\n"
        "Send me manga's name for searching manga by this name.\n\n"
        "This bot is open source and don't save users' info about users!"
    )

    await m.answer(
        text=text,
        parse_mode="HTML",
        disable_web_page_preview=True,
        disable_notification=False,
    )


def register_introduction_handlers(dp: Dispatcher):
    dp.register_message_handler(
        callback=start_cmd,
        commands={"start", "help"},
        content_types=["text"],
        state="*",
    )