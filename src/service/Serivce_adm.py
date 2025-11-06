from typing import Any

from passlib.context import CryptContext
from domains.User.Model_adm import Adm
from service.Service_jwt import Token

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


class ServiceAdm:
    @staticmethod
    async def register(data: dict[str,Any]):
        existing = await Adm.get_by_email(data["email"])
        if existing:
            return {"status": "ERROR", "msg": "Email já cadastrado"}

        data["password"] = pwd_context.hash(data["password"])
        await Adm.create_adm(data)

        return {"status": "OK", "msg": "Administrador criado"}

    @staticmethod
    async def login(data: dict[str,Any]):
        adm = await Adm.get_by_email(data["email"])
        if not adm:
            return {"status": "ERROR", "msg": "Administrador não encontrado"}

        if not pwd_context.verify(data.get("password", ""), adm.password):
            return {"status": "ERROR", "msg": "Senha incorreta"}

        token = Token().create({"email": data["email"]})
        return {"status": "OK", "msg": "Login bem-sucedido", "token": token}

    @staticmethod
    async def get_all(): #type: ignore
        adms = await Adm.get_all()
        return {"status": "OK", "content": adms} #type: ignore