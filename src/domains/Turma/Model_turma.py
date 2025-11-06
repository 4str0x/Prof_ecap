from typing import Any, Optional
from beanie import Document
from pydantic import BaseModel, Field


# ========================
# SCHEMAS (Entrada de dados)
# ========================
class Model_RegisterTurma(BaseModel):
    horario: str
    alunos: list[str] = Field(default_factory=list)
    chamada: list[str] = Field(default_factory=list)


# ========================
# DOCUMENTO PRINCIPAL (Mongo/Beanie)
# ========================
class Turma(Document):
    horario: str
    alunos: list[str] = Field(default_factory=list)
    chamada: list[str] = Field(default_factory=list)

    class Settings:
        collection = "Turma"

    # ========================
    # CRUD BÁSICO
    # ========================

    @staticmethod
    async def create_turma(data: dict[str, Any]) -> "Turma":
        turma = Turma(
            horario=data["horario"],
            alunos=data.get("alunos", []),
            chamada=data.get("chamada", [])
        )
        await turma.insert()
        return turma

    @staticmethod
    async def get_all() -> list["Turma"]:
        """Retorna todas as turmas."""
        return await Turma.find_all().to_list()

    @staticmethod
    async def get_by_id(turma_id: Any) -> Optional["Turma"]:
        """Busca turma pelo ID."""
        return await Turma.get(turma_id)

    @staticmethod
    async def update_turma(turma_id: Any, update_data: dict[str, Any]) -> bool:
        """Atualiza uma turma pelo ID."""
        turma = await Turma.get(turma_id)
        if not turma:
            return False
        await turma.set(update_data)
        return True

    @staticmethod
    async def delete_turma(turma_id: Any) -> bool:
        """Deleta uma turma pelo ID."""
        turma = await Turma.get(turma_id)
        if not turma:
            return False
        await turma.delete()
        return True