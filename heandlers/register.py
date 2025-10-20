from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message,ChatMemberUpdated
from aiogram import F
from heandlers.kyboards import fetch_products
from config import ADMIN
from aiogram import types
from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

register = Router()





@register.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Xush kelibsiz! Quyidagi tugmalardan foydalaning:")
    keyboard = await fetch_products()
    await message.answer("Kategoriyalar:", reply_markup=keyboard)


