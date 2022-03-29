def get_needs_text(need_type: str):
    if need_type == 'health':
        return """
💉 Поликлиника {business_name}

💰 Цена на один приём доктора: {total_price_health}
💊 Всего медикаментов в поликлинике: {business_count_product} ед.
❤️ Ты здоров на {user_health} %
💰 Твой баланс: {user_money} р."""
    elif need_type == 'eat':
        return """
🍴 Столовая {business_name}

💰 Цена один приём пищи: {total_price_health}
🥮 Всего медикаментов в поликлинике: {business_count_product} ед.
🍗 Ты сыт на {user_health} %
💰 Твой баланс: {user_money} р."""
    elif need_type == 'luck':
        return """
🍓 Бар {business_name}

💰 Цена один поход в бар: {total_price_health}
🍷 Всего медикаментов в поликлинике: {business_count_product} ед.
😄 Ты счастлив на {user_health} %
💰 Твой баланс: {user_money} р."""


ACCEPT_BUY_BUSINESS = """
Ты успешно приобрёл новый бизнес. Теперь процент дохода с бизнеса будет поступать тебе на счёт
Но не забывай следить за товарами, если они закончатся, государство отберёт твой бизнес."""

NEED_DOES_NOT_REGEN = """
Потребность не нуждается в восстановлении"""

NEEDS_REGEN = """
Потребность восстановлена"""

NOT_MONEY_TO_BUY_BUSINESS = """
😞Недостаточно средств для покупки бизнеса
💰 Цена: 20.00М руб. Твой баланс: {user_money} руб."""

MAIN_NEEDS_SETTINGS = """Выбери, что хочешь изменить в своём бизнесе"""

GET_NEW_NAME_NEED = """
Пришли мне новое название бизнеса или 0 для отмены"""

NEW_NAME_NEED = """
Название бизнеса изменено на {new_name}"""

NEED_NOT_OWNER = """
Не знаю, как ты сюда попал, но делать тебе тут нечего!"""

NEW_ORDER_PRODUCT = """
На данный момент на складе {count_product} шт.
Для заполения склада тебе необходимо {total_need_product} шт. ~ {total_price_product} руб. 💰
Твой баланс: {user_money} руб. 💰"""


def get_text_new_order_product(user_money: bool = False):
    if not user_money:
        return NEW_ORDER_PRODUCT + '\n\nУ тебя недостаточно средств для заказа продуктов'
    return NEW_ORDER_PRODUCT
