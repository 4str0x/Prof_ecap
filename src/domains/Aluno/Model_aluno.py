from typing import Any, Optional
from beanie import Document
from pydantic import BaseModel, Field

class Model_RegisterAluno(BaseModel):
    name: str
    turma: str
    chamada: list[str] = Field(default_factory=list)

class Aluno(Document):
    name: str
    turma: str
    chamada: list[str] = Field(default_factory=list)

    class Settings:
        collection = "Aluno"

    @staticmethod
    async def create_aluno(data: dict[str, Any]) -> "Aluno":
        aluno = Aluno(
            name=data.get("name", ""),
            turma=data.get("alunos", ""),
            chamada=data.get("chamada", [])
        )
        await aluno.insert()
        return aluno


    @staticmethod
    async def get_all() -> list["Aluno"]:
        """Retorna todas as turmas."""
        return await Aluno.find_all().to_list()
    

    @staticmethod
    async def get_by_id(Aluno_id: Any) -> Optional["Aluno"]:
        """Busca turma pelo ID."""
        return await Aluno.get(Aluno_id)

    @staticmethod
    async def update_aluno(Aluno_id: Any, update_data: dict[str, Any]) -> bool:
        """Atualiza uma turma pelo ID."""
        turma = await Aluno.get(Aluno_id)
        if not turma:
            return False
        await turma.set(update_data)
        return True

    @staticmethod
    async def delete_aluno(turma_id: Any) -> bool:
        """Deleta uma turma pelo ID."""
        aluno = await Aluno.get(turma_id)
        if not aluno:
            return False
        await aluno.delete()
        return True