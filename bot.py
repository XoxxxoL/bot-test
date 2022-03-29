import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.types.bot_command_scope import BotCommandScopeDefault

from aiogram.contrib.fsm_storage.memory import MemoryStorage

from handlers.gun_war_shop import register_shop_gun_war_handlers
from handlers.houses import register_house_store_handler
from handlers.keys import register_private_keys_handler
from handlers.referral import register_referral_handlers
from handlers.settings import register_settings_handler
from handlers.top_users import register_top_users_handler
from handlers.workers import register_workers_handler
from handlers.works.works_main import register_works_main_handler
from misc.services import scheduler

from db.session import engine, async_sessionmaker, config
from db.base import Base

from handlers.needs import register_needs_handlers
from handlers.start import register_start_handler
from updatesworker import get_handled_updates_list

from db.models import ammo_db, user_db, animals_db, banda_db, cars_db, chat_random_db, donat_db, fish_db, \
    gas_station_db, guns_db, guns_war_db, houses_db, pizza_components_db, pizza_db, race_event_db, \
    shop_item_db, stuff_db, user_business_db, user_stuff_db, active_user_db


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Начать/Восставновить меню"),
        BotCommand(command="id", description="Узнать свой ID")
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    bot = Bot(config.bot.token, parse_mode="HTML")
    bot["db"] = async_sessionmaker
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    scheduler.start()
    
    # REGISTER ALL HANDLERES
    register_start_handler(dp)
    register_needs_handlers(dp)
    register_house_store_handler(dp)
    register_workers_handler(dp)
    register_shop_gun_war_handlers(dp)
    register_private_keys_handler(dp)
    register_referral_handlers(dp)
    register_settings_handler(dp)
    register_top_users_handler(dp)
    register_works_main_handler(dp)

    await set_bot_commands(bot)

    try:
        await dp.start_polling(allowed_updates=get_handled_updates_list(dp))
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


try:
    asyncio.run(main())
except (RuntimeError, KeyboardInterrupt, SystemExit):
    logging.error("Bot stopped!")
