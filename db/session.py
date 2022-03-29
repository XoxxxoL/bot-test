from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# from db.models import ammo_db, user_db, animals_db, banda_db, cars_db, chat_random_db, donat_db, fish_db, \
#     gas_station_db, guns_db, guns_war_db, houses_db, pizza_components_db, pizza_db, race_event_db, \
#     shop_item_db, stuff_db, user_business_db, user_stuff_db, api_user_db, active_user_db

from config_loader import Config, load_config

config: Config = load_config('.env')


engine = create_async_engine(
    f"postgresql+asyncpg://{config.db.user}:{config.db.password}@{config.db.host}:5432/{config.db.db_name}",
    future=True
)

async_sessionmaker = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)