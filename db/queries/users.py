from db.models.user_db import Users
from db.models.houses_db import Houses
from db.models.guns_war_db import GunsWar
from db.models.works_db import Works

from misc.user_misc import generate_name

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound
from sqlalchemy import select

async def add_user(db_session: AsyncSession, user_id: int, fullname: str, referral_id: int = None, vip: bool = False, vip_finish: int = 0):
    name = await generate_name(user_id)
    
    async with db_session() as session:
        await session.merge(Users(telegram_id=user_id, name=name, fullname=fullname, referral_id=referral_id, vip=vip, vip_finish=vip_finish))
        await session.commit()

async def get_user_profile(db_session: AsyncSession, user_id):
    
    async with db_session() as session:
        sql = select(Users, Houses).join(Houses, Houses.id == Users.house).where(Users.telegram_id == user_id)
        user = await session.execute(sql)
    try:
        return user.one()
    except NoResultFound:
        return None
    
    
async def get_main_user_info(db_session: AsyncSession, user_id: int):
    
    async with db_session() as session:
        sql = select(Users.money, Users.bottle, Users.eat,
                     Users.health, Users.luck, Users.event_id,
                     Users.lvl, Users.exp, Users.name, Users.fullname,
                     Users.keyses, Users.donat).where(Users.telegram_id == user_id)
        user = await session.execute(sql)
    return user.one()


async def update_user_balance(db_session: AsyncSession, user_id: int, money_type: str, operation: str,
                              amount: int, vip_active: bool = False, nalog: bool = False):
    
    async with db_session() as session:
        user = await session.get(Users, user_id)
        if money_type == 'money':
            if operation == '+' and vip_active:
                user.money += amount * 2
            elif operation == '+' and nalog and not vip_active:
                user.money += amount - (amount * (13 / 100))
            elif operation == '+' and not vip_active and not nalog:
                user.money += amount
            elif operation == '-':
                if user.money - amount < 0:
                    return False
                user.money -= amount
        elif money_type == 'bottle':
            if operation == '+' and vip_active:
                user.bottle += amount * 2
            elif operation == '+' and nalog and not vip_active:
                user.bottle += amount - (amount * (13 / 100))
            elif operation == '+' and not vip_active and not nalog:
                user.bottle += amount
            elif operation == '-':
                if user.bottle - amount < 0:
                    return False
                user.bottle -= amount
        elif money_type == 'donat':
            if operation == '+':
                user.donat += amount
            elif operation == '-':
                if user.donat - amount < 0:
                    return False
                user.donat -= amount
        await session.commit()
        return True
        
        
async def update_user_exp(db_session: AsyncSession, user_id: int, operation: str, amount: int, vip_active: bool = False):
    
        async with db_session() as session:
            user = await session.get(Users, user_id)
            if operation == '+':
                if vip_active:
                    user.exp += amount * 2
                else:
                    user.exp += amount
            elif operation == '-':
                user.exp -= amount
            if user.exp > (user.lvl + 1) * 50:
                user.lvl = user.exp / 50
            await session.commit()
            
            
async def update_user_keys(db_session: AsyncSession, user_id: int, operation: str, amount: int):
    
    async with db_session() as session:
        user = await session.get(Users, user_id)
        if operation == '+':
            user.keyses += amount
        elif operation == '-':
            user.keyses -= amount
        await session.commit()
                
            

async def update_needs_user(db_session, user_id: int, need_type: str,  operation: str, amount: int):
    
    async with db_session() as session:
        user = await session.get(Users, user_id)
        if operation == '+':
            setattr(user, need_type, getattr(user, need_type) + amount)
            if getattr(user, need_type) > 100:
                setattr(user, need_type, 100)
        elif operation == '-':
            setattr(user, need_type, getattr(user, need_type) - amount)
            if getattr(user, need_type) < 0:
                setattr(user, need_type, 0)
        await session.commit()
        
        
async def update_user_house(db_session, user_id: int, house_id: int):
    
    async with db_session() as session:
        user = await session.get(Users, user_id)
        user.house = house_id
        await session.commit()


async def update_workers(db_session: AsyncSession, user_id: int, operation: str, amount: int):
    
    async with db_session() as session:
        user = await session.get(Users, user_id)
        if operation == '+':
            user.bomj += amount
        elif operation == '-':
            user.bomj -= amount
        await session.commit()
        
        
async def get_user_info_and_gun_war(db_session: AsyncSession, user_id: int):
    
    async with db_session() as session:
        sql = select(Users, GunsWar).join(GunsWar, GunsWar.id == Users.gun_war).where(Users.telegram_id == user_id)
        info = await session.execute(sql)
        info = info.one()
        return info
    
    
async def update_user_gun_war(db_session: AsyncSession, user_id: int, gun_war: int):
    
    async with db_session() as session:
        user = await session.get(Users, user_id)
        user.gun_war = gun_war
        await session.commit()
        
        
async def get_referral_user(db_session: AsyncSession, user_id: int):
    
    async with db_session() as session:
        sql = select(Users.name, Users.username).where(Users.referral_id == user_id)
        users = await session.execute(sql)
        users = users.all()
        return users
    
    
async def change_user_name(db_session: AsyncSession, user_id: int, new_name: str):
    
    async with db_session() as session:
        user = await session.get(Users, user_id)
        user.name = new_name
        await session.commit()
        
        
async def get_user_close_profile(db_session: AsyncSession, user_id: int):
    
    async with db_session() as session:
        sql = select(Users.close_profile).where(Users.telegram_id == user_id)
        user = await session.execute(sql)
        user = user.one()
        user = user[0]
        return user
    
    
async def change_close_profile_user(db_session: AsyncSession, user_id: int, close: bool):
    
    async with db_session() as session:
        user = await session.get(Users, user_id)
        user.close_profile = close
        await session.commit()
        
        
async def get_top_with_category(db_session: AsyncSession, category: str):
    
    async with db_session() as session:
        sql = 'SELECT %s, name FROM users ORDER BY %s DESC LIMIT 5' % (category, category)
        users = await session.execute(sql)
        users = users.all()
        return users
    
    
async def get_works_for_user(db_session: AsyncSession, user_id: int):
    
    async with db_session() as session:
        sql = 'SELECT id, name FROM works WHERE lvl <= (SELECT lvl FROM users WHERE telegram_id=%s)' % user_id
        works = await session.execute(sql)
        return works.all()