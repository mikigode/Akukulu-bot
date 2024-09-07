import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = "6417148529:AAFOM2umzWM7GOq0hoiL-VTuQ3DSdk0XnEc"
group_id = -1002014551406
group2_id = -1002049831009
group3_id= -1002018554869

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

log1 = InlineKeyboardButton('Order Now', callback_data="thank_you")  
log2 = InlineKeyboardButton('Sign in', callback_data="textbook")  # buttons for textbook
key2 = InlineKeyboardMarkup().add(log1)

catag1 = InlineKeyboardButton('Order Now', callback_data="thank_you2")
tnx1= InlineKeyboardMarkup().add(catag1)
catag2 = InlineKeyboardButton('Order Now', callback_data="thank_you3")
tnx2= InlineKeyboardMarkup().add(catag2)
catag3 = InlineKeyboardButton('Order Now', callback_data="thank_you4")
tnx3= InlineKeyboardMarkup().add(catag3)
catag4 = InlineKeyboardButton('Order Now', callback_data="thank_you5")
tnx4= InlineKeyboardMarkup().add(catag4)
key3 = InlineKeyboardMarkup(resize_keyboard=True).add(catag1, catag2).add(catag3, catag4)

btn1 = KeyboardButton('🥞 አኩኩሉ Toast')
btn2 = KeyboardButton('🥪 አኩኩሉ Special')
btn3 = KeyboardButton('🥘 አኩኩሉ sandwich')
btn4 = KeyboardButton('🍳 custome አኩኩሉ')


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    print(message)
    await bot.send_message(group_id, f"User {message.chat.mention} clicked /start")
    
    text = f"""Hi, *{message.from_user.first_name}! 👋*

` * This is አኩኩሉ Gursha order management simulation bot. * `

📌 To continue, please *Share Contact ☎️* using the button below.
"""
    await message.answer(
        text,
        parse_mode="MARKDOWN",
        reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton(
                "Share Contact ☎",
                request_contact=True,
            ))
    )
@dp.message_handler(content_types=types.ContentType.CONTACT)
async def handle_contact(message: types.Message):
    phone_number = message.contact.phone_number
    await bot.send_message(group_id, f"User {message.chat.mention} shared their phone number: +{phone_number}")

    btn = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1, btn2).add(btn3, btn4).add(KeyboardButton("📱 Download App 📱"))

    congratulations_message = "Congratulations! 🎉🎉🎉\n\nYou have registered successfully! ✅"
    await message.answer(congratulations_message, reply_markup=btn)

@dp.message_handler()
async def handle_message(message: types.Message):
    
    if message.text == '🥞 አኩኩሉ Toast':
         
        #  phone_number = message.contact.phone_number
         await bot.send_message(group2_id, f"user {message.from_user.mention} clicked: #አኩኩሉ_Toast ")

         await message.answer(
            f'''🥇Toast 🍞

We use bread 🥐 for Toast
--> To provide Carbohydrates i.e source for Energy
--> Fiber i.e responsible for digestion
--> And some Vitamin and Mineral i.e stand for building.
--> To provide healthy Fat and Proteins
--> Iron for Good blood Circulations

order now, we will call you soon..''',
            reply_markup=key2)
    

    elif message.text == "🥪 አኩኩሉ Special":
        await bot.send_message(group2_id, f"user {message.chat.mention} clicked: 🥪 #አኩኩሉ_Special ")
        await message.answer(
            '''For Special one Toast 🍞.. we give the additional bonus which of Temir(Dates) and Tomato 🍅 ketchup ..

Those are rich in nutrients and literally the same ingredients; that both are have Antioxidant properties, Rich in Vitamin
Incorporating dates and tomatoes into your diet can provide a wide range of health benefits, including improved digestion, Natural sweeter, enhanced immune function, and reduced risk of chronic diseases.
order now, we will call you soon..''',
            reply_markup=tnx1)
    elif message.text == "🥘 አኩኩሉ sandwich":
        await bot.send_message(group2_id, f"user {message.chat.mention} clicked: 🥘 #አኩኩሉ_sandwich ")
        await message.answer('order now, we will call you soon..', reply_markup=tnx2)
    elif message.text == "🍳 custome አኩኩሉ":
        await bot.send_message(group2_id, f"user {message.chat.mention} clicked: 🍳 #custome_አኩኩሉ ")
        await message.answer('order now, we will call you soon..', reply_markup=tnx3)

@dp.callback_query_handler(lambda c: c.data == 'thank_you')
async def handle_thank_you(callback_query: types.CallbackQuery):
    await bot.send_message(group3_id, f"user {callback_query.from_user.mention} Ordered: #አኩኩሉ_Toast ")
    await callback_query.answer()
    await callback_query.message.answer("Thank you for your order!\nYou ordered 🥞 አኩኩሉ Toast\n \n We will contact you soon.")

@dp.callback_query_handler(lambda c: c.data == 'thank_you2')
async def handle_thank_you(callback_query: types.CallbackQuery):
    await bot.send_message(group3_id, f"user {callback_query.from_user.mention} Ordered: #አኩኩሉ_special ")
    await callback_query.answer()
    await callback_query.message.answer("Thank you for your order!\n You ordered 🥪 አኩኩሉ Special\n \n We will contact you soon.")

@dp.callback_query_handler(lambda c: c.data == 'thank_you3')
async def handle_thank_you(callback_query: types.CallbackQuery):
    await bot.send_message(group3_id, f"user {callback_query.from_user.mention} Ordered: #አኩኩሉ_sandwich")
    await callback_query.answer()
    await callback_query.message.answer("Thank you for your order!\nYou ordered 🥘 አኩኩሉ sandwich\n \n We will contact you soon.")

@dp.callback_query_handler(lambda c: c.data == 'thank_you4')
async def handle_thank_you(callback_query: types.CallbackQuery):
    await bot.send_message(group3_id, f"user {callback_query.from_user.mention} Ordered: #custome ")
    await callback_query.answer()
    await callback_query.message.answer("\bThank you for your order!\b \nYou ordered 🍳 custome አኩኩሉ\n \n We will contact you soon.")

print("Bot started successfully!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)