from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Jahon estradasi"),
            KeyboardButton("O'zbek estradasi")
        ],
        [
            KeyboardButton("Top Muzikalar"),
            KeyboardButton("Suralar")
        ]
    ],
    resize_keyboard=True
)

jahon_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Jahon estradasi Top3 lik"),
            KeyboardButton("Yevropa mamlakatlari qo'shiqlari")
        ],
        [
            KeyboardButton("G'arb mamlakatlari qo'shiqlari"),
            KeyboardButton("Osiyo mamlakatlari qo'shiqlari")
        ],
        [
            KeyboardButton("Orqaga")
        ]
    ],
    resize_keyboard=True
)

uzbek_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Ozbek estradasi estradasi Top3 lik"),
            KeyboardButton("Yangi qo'shiqlar")
        ],
        [
            KeyboardButton("Eski qo'shiqlar"),
            KeyboardButton("O'zbek repi")
        ],
        [
            KeyboardButton("Orqaga")
        ]
    ],
    resize_keyboard=True
)

top_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Bosh menyu")
        ]
    ],
    resize_keyboard=True
)

sura_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Al alafasi suralari")
        ],
        [
            KeyboardButton("O'zbek domlalari suralari")
        ],
        [
            KeyboardButton("Orqaga")
        ]
    ],
    resize_keyboard=True
)

domla = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Bosh menyu")
        ]
    ],
    resize_keyboard=True
)

alafasi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Bosh menyu")
        ]
    ],
    resize_keyboard=True
)


