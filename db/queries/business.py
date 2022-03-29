from db.models.business_db import Business

from sqlalchemy.ext.asyncio import AsyncSession


async def get_current_business(db_session: AsyncSession, business_id):
    
    async with db_session() as session:
        business = await session.get(Business, business_id)
    return business
        