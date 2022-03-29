from db.queries.business import get_current_business
from misc.vriables import SMILE_MONEY_TYPE


async def generate_name(user_id: int):
    return f'User{user_id}'


async def get_user_business_profit(db_session, user):
    
    total_money = 0
    total_bottle = 0
    
    if user is not None and user.get('business', False):
        for info in user.get('business').items():
            current_busienss = await get_current_business(db_session, info[0])
            if current_busienss.money_type == 'money':
                total_money += current_busienss.profit * info[1]
            elif current_busienss.money_type == 'bottle':
                total_bottle += current_busienss.profit * info[1]
    return {'money': total_money, 'bottle': total_bottle}


async def text_user_balance(money, bottle, exp, donat, keyses):
    return f'Твой баланс: {money} {SMILE_MONEY_TYPE.get("money")} | ' \
            f'{bottle} {SMILE_MONEY_TYPE.get("bottle")} | ' \
            f'{keyses} {SMILE_MONEY_TYPE.get("keyses")} | ' \
            f'{exp} {SMILE_MONEY_TYPE.get("exp")} | ' \
            f'{donat} {SMILE_MONEY_TYPE.get("donat")}'