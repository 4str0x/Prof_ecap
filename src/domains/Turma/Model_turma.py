from typing import Any, Optional
from beanie import Document
from pydantic import BaseModel, Field

from domains.Aluno.Model_aluno import Aluno

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
    async def update_turma(turma_id: str, update_data: dict[str, Any]) -> bool:
        """Atualiza uma turma pelo ID."""
        turma = await Turma.get(turma_id)
        if not turma:
            return False
        await turma.set(update_data)
        return True

    @staticmethod
    async def vincular_aluno(turma_id: str, aluno_id: str) -> bool:
        """Vincula um aluno a uma turma (substitui turma anterior, se houver)."""
        turma = await Turma.get(turma_id)
        aluno = await Aluno.get(aluno_id)

        if not turma or not aluno:
            return False

        # Se o aluno já tem uma turma antiga, remove ele de lá
        if aluno.turma_id:
            turma_antiga = await Turma.get(aluno.turma_id)
            if turma_antiga:
                turma_antiga.alunos = [a for a in turma_antiga.alunos if a != aluno.id]
                await turma_antiga.save()

        # Atualiza o vínculo novo
        aluno.turma_id = str(turma.id)
        await aluno.save()

        # Adiciona o aluno à nova turma, se ainda não estiver nela
        if str(aluno.id) not in turma.alunos:
            turma.alunos.append(str(aluno.id))
            await turma.save()

        return True

    @staticmethod
    async def desvincular_aluno(aluno_id: str) -> bool:
        aluno = await Aluno.get(aluno_id)
        if not aluno or not aluno.turma_id:
            return False

        turma = await Turma.get(aluno.turma_id)
        if turma:
            turma.alunos = [a for a in turma.alunos if a != aluno_id]
            await turma.save()

        aluno.turma_id = None
        await aluno.save()

        return True

    @staticmethod
    async def delete_turma(turma_id: Any) -> bool:
        """Deleta uma turma pelo ID."""
        turma = await Turma.get(turma_id)
        if not turma:
            return False
        await turma.delete()
        return True