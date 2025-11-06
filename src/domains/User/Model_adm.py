from typing import Any, Optional
from beanie import Document
from pydantic import BaseModel

class Model_LoginAdm(BaseModel):
    email: str = ""
    password: str = ""
    
class Model_RegisterAdm(BaseModel):
    name: str
    email: str
    password: str

class Adm(Document):
    name: str
    email: str
    password: str

    class Settings:
        collection = "Adm"

    # ========================
    # CRUD BÁSICO
    # ========================

 
    @staticmethod
    async def create_adm(data: dict[str, Any]) -> "Adm":
        adm = Adm(
            name=data["name"], 
            email=data["email"], 
            password=data["password"]
            )
        
        await adm.insert()
        return adm

    @staticmethod
    async def get_all() -> list["Adm"]:
        """Retorna todos os admins."""
        return await Adm.find_all().to_list()  # sem .dict()

    @staticmethod
    async def get_by_id(adm_id: int) -> Optional["Adm"]:
        """Busca admin por ID."""
        return await Adm.find_one({"ID": adm_id})

    @staticmethod
    async def get_by_email(email: str) -> Optional["Adm"]:
        """Busca admin por email."""
        return await Adm.find_one({"email": email})

    @staticmethod
    async def update_adm(adm_id: int, update_data: dict[str, Any]) -> bool:
        """Atualiza um admin pelo ID."""
        adm = await Adm.find_one({"ID": adm_id})
        if not adm:
            return False
        await adm.update({"$set": update_data})
        return True

    @staticmethod
    async def delete_adm(adm_id: int) -> bool:
        """Deleta um admin pelo ID."""
        adm = await Adm.find_one({"ID": adm_id})
        if not adm:
            return False
        await adm.delete()
        return True
