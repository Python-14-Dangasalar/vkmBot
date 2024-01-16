from aiogram import executor
from aiogram.types import Message, CallbackQuery
from config import dp
from reply_button import start_btn, jahon_btn, uzbek_btn, top_btn, sura_btn, alafasi, domla
from inline_button import jahon_top3, yevropa, garb, osiyo, uzbek_top3, yangi, eski, uzbek_rep, like_dislike

@dp.message_handler(commands=['start'])
async def start(message: Message):
    photo = open("images/music.jpg", 'rb')
    text = (f"Hello {message.from_user}👋 vkmBot ga xush kelibsiz🎵\n"
            f"Ushbu bot vkmBot plagiati xisoblanadi,\n"
            f"Maroqli tinglov tilab qolamiz😊")
    await message.answer_photo(photo=photo, caption=text, reply_markup=start_btn)

@dp.message_handler(text="Bosh menyu")
async def bosh(message: Message):
    text = (f"Kerakli bo'limni qayta tanlashingiz mumkin🎧,\n"
            f"Ushbu menyuga tushganingiz sabablari:🎶\n"
            f"1.Tanlangan bo'limingizda ma'lumot joylanmagan/yangilanmagan,🗑💣\n"
            f"2.Siz bo'tdan foydalanishni bilmadingiz.🧢")
    await message.answer(text, reply_markup=start_btn)

@dp.message_handler(text="Orqaga")
async def orqaga(message: Message):
    text = f"Siz bosh bo'limga qaytdingiz, bo'limlarni qayta tanlang👇"
    await message.answer(text, reply_markup=start_btn)

# birinchi bo'lim
@dp.message_handler(text="Jahon estradasi")
async def jahon(message: Message):
    text = f"Tabriklayman, siz Jahon estradasi bo'limini tanladingiz marhamat keyingi bo'limni tanalang👇"
    await message.answer(text, reply_markup=jahon_btn)

@dp.message_handler(text="O'zbek estradasi")
async def jahon(message: Message):
    text = f"Tabriklayman, siz O'zbek estradasi bo'limini tanladingiz marhamat keyingi bo'limni tanalang👇"
    await message.answer(text, reply_markup=uzbek_btn)

@dp.message_handler(text="Top Muzikalar")
async def jahon(message: Message):
    text = f"Afsuski hozirda ushbu bo'lim to'liq shakllanmagan, Bosh menyuga qaytish uchun tugmani bosing👇"
    await message.answer(text, reply_markup=top_btn)

@dp.message_handler(text="Suralar")
async def jahon(message: Message):
    text = f"Tabriklayman, siz Suralar bo'limini tanladingiz marhamat keyingi bo'limni tanalng👇"
    await message.answer(text, reply_markup=sura_btn)


#Jahon estradasi bo'limi
@dp.message_handler(text="Jahon estradasi Top3 lik")
async def jahon(message: Message):
    text = f"1.Dance Monkey-Tones and I.\n2.Believer-Imagine Dragons.\n,3.Despacito-Luis Fonsi."
    await message.answer(text, reply_markup=jahon_top3)

@dp.message_handler(text="Yevropa mamlakatlari qo'shiqlari")
async def yevopa(message: Message):
    text = f"1.All Eyes on me-DJ Belite\n2.Rain-Guilia\n3.I'm Alone-Melisa"
    await message.answer(text, reply_markup=yevropa)

@dp.message_handler(text="G'arb mamlakatlari qo'shiqlari")
async def yevopa(message: Message):
    text = f"1.Lil Boo Thang-Pol Rassel\n2.Paint the Town Red-Doja Cat\n3.Lose Control-Teddy Swims"
    await message.answer(text, reply_markup=garb)

@dp.message_handler(text="Osiyo mamlakatlari qo'shiqlari")
async def yevopa(message: Message):
    text = f"1.Asadati Wlad Taha-Ahmed El Mounsi\n2.It's you-COSMIC BOY\n3.Something-something astro"
    await message.answer(text, reply_markup=osiyo)


# O'zbek estradasi bo'limi
@dp.message_handler(text="Ozbek estradasi estradasi Top3 lik")
async def yevopa(message: Message):
    text = f"1.Kutaman-O'lmas Olloberganov\n2.Odamlar nima deydi-Consta\n3.Jonga tegdi-Consta"
    await message.answer(text, reply_markup=uzbek_top3)

@dp.message_handler(text="Yangi qo'shiqlar")
async def yevopa(message: Message):
    text = f"Keyingi bo'limni tanlang👇"
    await message.answer(text, reply_markup=yangi)

@dp.message_handler(text="Eski qo'shiqlar")
async def yevopa(message: Message):
    text = f"Keyingi bo'limni tanlang👇"
    await message.answer(text, reply_markup=eski)

@dp.message_handler(text="O'zbek repi")
async def yevopa(message: Message):
    text = f"1.O'zbegim-Shoxrux\n2.Xato-Shoxrux\n3.Kel money-Shaxriyor"
    await message.answer(text, reply_markup=uzbek_rep)


#Suralar bo'limi
@dp.message_handler(text="Al alafasi suralari")
async def yevopa(message: Message):
    await message.reply("O'zbekiston respublikasida diniy ma'lumotlar tarqatmayman🙂\n"
                        "Iltimos Bosh menyuga qayting!", reply_markup=alafasi)

@dp.message_handler(text="O'zbek domlalari suralari")
async def yevopa(message: Message):
    await message.reply("O'zbekiston respublikasida diniy ma'lumotlar tarqatmayman🙂\n"
                        "Iltimos Bosh menyuga", reply_markup=domla)

# Jahon estradasi Muzika qo'shish
@dp.callback_query_handler(text="Despacito-Luis Fonsi")
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/Despacito.mp3", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)

@dp.callback_query_handler(text='Dance Monkey-Tones and I')
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/Dance Monkey.mp3", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)

@dp.callback_query_handler(text='Believer-Imagine Dragons')
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/Believer.mp3", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)

# yevropa bo'lim
@dp.callback_query_handler(text='All Eyes on me-DJ Belite')
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/All eyes on me.m4a", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)

@dp.callback_query_handler(text="Rain-Guilia")
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/Rain.mp3", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)

@dp.callback_query_handler(text="Im Alone-Melisa")
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/I'm Alone.mp3", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)

# G'arb bo'limi
@dp.callback_query_handler(text="Lil Boo Thang-Pol Rassel")
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/Lil Boo Thang.m4a", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)

@dp.callback_query_handler(text="Paint the Town Red-Doja Cat")
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/Paint the.mp3", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)

@dp.callback_query_handler(text="Lose Control-Teddy Swims")
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/Lose Control.mp3", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)

# Osiyo bo'limi
@dp.callback_query_handler(text="Asadati Wlad Taha-Ahmed El Mounsi")
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/All eyes on me.m4a", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="It's you-COSMIC BOY")
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/Cosmic boy.m4a", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Something-something astro")
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/Something.mp3", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)

# Uzbek top3
@dp.callback_query_handler(text="Kutaman-O'lmas Olloberganov")
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/Kutaman.mp3", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Odamlar nima deydi-Consta")
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/Konsta.mp3", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Jonga tegdi-Consta")
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/Jonga teydi.mp3", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)

#Uzbek rep
@dp.callback_query_handler(text="O'zbegim-Shoxrux")
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/O'zbegim.mp3", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Xato-Shoxrux")
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/Xato.mp3", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="Kel money-Shaxriyor")
async def callback_query(call: CallbackQuery):
    await call.message.answer_audio(open("Jahon estradasi/Kel money.mp3", "rb"), reply_markup=like_dislike)
    await call.answer(cache_time=10)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
