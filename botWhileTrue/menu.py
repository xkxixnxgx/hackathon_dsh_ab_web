from telebot import types

start = [
    types.KeyboardButton('Вклад'),
    types.KeyboardButton('Кредит'),
    types.KeyboardButton('Ипотека'),
    types.KeyboardButton('Дебетовые карты'),
    types.KeyboardButton('Заявки'),
    types.KeyboardButton('Специалист')
]

services =  {
    "Вклад": [
        types.InlineKeyboardButton('Уверенное будущее до 6,3%*', callback_data='vklad_future'),
        types.InlineKeyboardButton('Я сам?! до 5,8%*', callback_data='vklad_self'),
        types.InlineKeyboardButton('Просто преумножить до 5%*', callback_data='vklad_mnzh'),
        types.InlineKeyboardButton('Просто поймай момент до 2,95%*', callback_data='vklad_moment'),
        types.InlineKeyboardButton('Просто управлять до 4,6%*', callback_data='vklad_upr'),
        types.InlineKeyboardButton('Просто накопить до 5,1%*', callback_data='vklad_nakop')
    ],
    "Кредит": [
        types.InlineKeyboardButton('Помощь в период COVID-19', callback_data='kredit_covid19'),
        types.InlineKeyboardButton('Кредит наличными до 7 лет', callback_data='kredit_cash'),
        types.InlineKeyboardButton('Кредит до 20 лет', callback_data='kredit_zalog'),
        types.InlineKeyboardButton('Рефинансирование кредитов', callback_data='kredit_ref'),
        types.InlineKeyboardButton('Кредитная карта Emotion', callback_data='kredit_card')
    ],
    "Ипотека": [
        types.InlineKeyboardButton('Вторичное жилье', callback_data='ipoteka_vtor'),
        types.InlineKeyboardButton('Новостройки с господдержкой', callback_data='ipoteka_novogos'),
        types.InlineKeyboardButton('Новостройки', callback_data='ipoteka_novo'),
        types.InlineKeyboardButton('Рефинансирование ипотеки', callback_data='ipoteka_ref'),
        types.InlineKeyboardButton('Господдержка для семей с детьми', callback_data='ipoteka_child'),
        types.InlineKeyboardButton('Коммерческая недвижимость', callback_data='ipoteka_kom'),
        types.InlineKeyboardButton('Дом и земельный участок', callback_data='ipoteka_house')
    ],
    "Дебетовые карты": [
        types.InlineKeyboardButton('Карта Aurum', callback_data='card_aurum'),
        types.InlineKeyboardButton('Карта Evolution', callback_data='card_evolution'),
        types.InlineKeyboardButton('Карта Generation', callback_data='card_generation'),
        types.InlineKeyboardButton('Ак Барс Premium', callback_data='card_premium'),
        types.InlineKeyboardButton('Классическая карта', callback_data='card_classic'),
        types.InlineKeyboardButton('Мир Долголетия', callback_data='card_mir')
    ]
}

service_messages = [
    "Выберите необходимую вам программу:",
    "Выберите удобную вам программу:",
    "Выберите нужную вам программу"
]

proposals = {
    # ВКЛАДЫ
    "vklad_future": {
        "name": "Уверенное будущее",
        "message": "Вклад с накопительным страхованием жизни",
        "link": "https://www.akbars.ru/individuals/deposits/uverennoe-budushchee/"
    },
    "vklad_self": {
        "name": "Я сам",
        "message": "Вклад с пополнением и пролонгацией",
        "link": "https://www.akbars.ru/individuals/deposits/ya-sam/"
    },
    "vklad_mnzh": {
        "name": "Просто преумножить",
        "message": "Вклад с пополнением и снятием",
        "link": "https://www.akbars.ru/individuals/deposits/prosto-preumnozhit/"
    },
    "vklad_moment": {
        "name": "Просто поймать момент",
        "message": "Вклад сроком на 31 день",
        "link": "https://www.akbars.ru/individuals/deposits/prosto-poimat-moment/"
    },
    "vklad_upr": {
        "name": "Просто управлять",
        "message": "Вклад с частичным снятием",
        "link": "https://www.akbars.ru/individuals/deposits/prosto-upravlyat/"
    },
    "vklad_nakop": {
        "name": "Просто накопить",
        "message": "Вклад с удобными процентами",
        "link": "https://www.akbars.ru/individuals/deposits/prosto-nakopit/"
    },
    # КРЕДИТЫ
    "kredit_covid19": {
        "name": "Оставайся дома",
        "message": "Наши услуги и рекомендации для вас",
        "link": "https://www.akbars.ru/individuals/stay-home/"
    },
    "kredit_cash": {
        "name": "Потребительский",
        "message": "От 7,7%*",
        "link": "https://www.akbars.ru/individuals/credits/potrebitelskiy/"
    },
    "kredit_zalog": {
        "name": "Кредит под залог недвижимости",
        "message": "Под залог недвижимости",
        "link": "https://www.akbars.ru/individuals/credits/potrebkredit-zalog-nedvizhimosti/"
    },
    "kredit_ref": {
        "name": "Рефинансирование",
        "message": "Рефинансирование потребительских кредитов",
        "link": "https://www.akbars.ru/individuals/credits/refinansirovanie-potrebkreditov/"
    },
    "kredit_card": {
        "name": "Кредитная карта Emotion",
        "message": "Льготный период, кэшбэк рублями и снятие наличных без комиссии",
        "link": "https://www.akbars.ru/individuals/credit-cards/emotion/"
    },
    # ИПОТЕКИ
    "ipoteka_vtor": {
        "name": "Мегаполис",
        "message": "Ставка от 7,75%:",
        "link": "https://www.akbars.ru/individuals/hypothec/megapolis/"
    },
    "ipoteka_novogos": {
        "name": "Субсидирование ставки",
        "message": "Ставка от 6,1%",
        "link": "https://www.akbars.ru/individuals/hypothec/subsidirovaniye-stavki/"
    },
    "ipoteka_novo": {
        "name": "Перспектива",
        "message": "Ставка от 7,75%",
        "link": "https://www.akbars.ru/individuals/hypothec/perspektiva/"
    },
    "ipoteka_ref": {
        "name": "Рефинансирование",
        "message": "Ставка от 7,99%",
        "link": "https://www.akbars.ru/individuals/hypothec/refinansirovanie-ipoteki/"
    },
    "ipoteka_child": {
        "name": "Семья с детьми",
        "message": "Ставка от 4,9%",
        "link": "https://www.akbars.ru/individuals/hypothec/gospodderzhka-semya-s-detmi/"
    },
    "ipoteka_kom": {
        "name": "Бизнес",
        "message": "Ставка от 9,99%",
        "link": "https://www.akbars.ru/individuals/hypothec/ak-bars-biznes/"
    },
    "ipoteka_house": {
        "name": "Комфорт",
        "message": "Ставка от 8,5%",
        "link": "https://www.akbars.ru/individuals/hypothec/komfort/"
    },
    # Карты
    "card_aurum": {
        "name": "Aurum",
        "message": "Кэшбэк за покупки и процент на остаток выплачиваются золотом",
        "link": "https://www.akbars.ru/individuals/cards/aurum/"
    },
    "card_evolution": {
        "name": "Evolution",
        "message": "Самая выгодная карта для полетов по России*",
        "link": "https://www.akbars.ru/individuals/cards/evolution/"
    },
    "card_generation": {
        "name": "Generation",
        "message": "Для тех, кто постоянно в движении",
        "link": "https://www.akbars.ru/individuals/cards/generation/"
    },
    "card_premium": {
        "name": "Premium",
        "message": "Пакет услуг повышенной комфортности",
        "link": "https://www.akbars.ru/individuals/cards/ak-bars-premium/"
    },
    "card_classic": {
        "name": "Classic",
        "message": "Универсальная карта для покупок",
        "link": "https://www.akbars.ru/individuals/cards/classic/"
    },
    "card_mir": {
        "name": "Карта долголетия",
        "message": "Получайте пенсию на карту",
        "link": "https://www.akbars.ru/individuals/cards/mir-karta-dolgoletiya/"
    }
}
