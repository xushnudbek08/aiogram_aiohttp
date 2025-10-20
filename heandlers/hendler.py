



from aiogram import F, Router
from aiogram.types import CallbackQuery
import aiohttp

router = Router()

@router.callback_query(F.data.startswith("category_"))
async def category_callback(callback_query: CallbackQuery):

    category_id = callback_query.data.split("_")[1]

    url = 'https://sanjar0202.pythonanywhere.com/products/'
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            products = await response.json()


            filtered_products = [
                p for p in products
                if (
                    p['category']['id'] == int(category_id)
                    if isinstance(p['category'], dict)
                    else p['category'] == int(category_id)
                )
            ]

            # Natijani chiroyli ko‘rsatish
            if filtered_products:
                text = "\n".join([
                    f"📦 {p['name']} — {p['price']}so`m" for p in filtered_products
                ])
            else:
                text = "Bu kategoriyada mahsulotlar yo‘q."

            await callback_query.message.answer(text)
