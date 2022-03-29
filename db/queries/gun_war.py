from db.models.guns_war_db import GunsWar


async def get_current_gun_war(db_session, gun_id: int):
    
    async with db_session() as session:
        gun = await session.get(GunsWar, gun_id)
        return gun