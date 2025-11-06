from typing import Any

from beanie import init_beanie  # type: ignore
from motor.motor_asyncio import AsyncIOMotorClient

from config.config import settings
from domains.User.Model_adm import Adm
from domains.Turma.Model_turma import Turma


async def init_db():
    client: AsyncIOMotorClient[Any] = AsyncIOMotorClient(settings.MONGO_URI)

    await init_beanie(
        database=client[settings.MONGO_DB_NAME], #type: ignore
        document_models=[Adm,Turma], #type: ignore
    )