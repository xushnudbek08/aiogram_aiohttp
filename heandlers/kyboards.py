from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import aiohttp
import asyncio


# async def fetch_products():
#     url = 'https://sanjar0202.pythonanywhere.com/products/'
#     buttons=[]
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             data = await response.json()
            
#             for item in data:
#                 category =( 
                    
#                     item['category']['name']
#                     if  isinstance(item['category'],dict)
#                     else item['category']
#                     )
#                 button = KeyboardButton(text=category)
#                 buttons.append([button])
#             inline_kb = ReplyKeyboardMarkup(resize_keyboard=buttons)
#     return inline_kb




async def fetch_products():
    url = 'https://sanjar0202.pythonanywhere.com/categories/'
    buttons=[]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            
            for item in data:
                category = item['name']
                button = InlineKeyboardButton(
                    text=category,
                    callback_data=f"category_{item['id']}"
                )
                
                buttons.append([button])

    inline_kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return inline_kb

