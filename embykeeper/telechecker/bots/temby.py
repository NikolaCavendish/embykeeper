from .base import AnswerBotCheckin

from pyrogram.types import Message


class TembyCheckin(AnswerBotCheckin):
    name = "Temby"
    bot_username = "HiEmbyBot"
    bot_checkin_cmd = "/hi"
    bot_success_keywords = ["Checkin successfully"]

    async def on_answer(self, message: Message):
        await super().on_answer(message)
        await message.click(0)
