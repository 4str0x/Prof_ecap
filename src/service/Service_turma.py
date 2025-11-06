from typing import Any

from domains.Turma.Model_turma import Turma

class ServiceTurma:
    @staticmethod
    async def create(data: dict[str, Any]): #type: ignore
        turma = await Turma.create_turma(data)
        return {"status": "OK", "msg": "Turma criada com sucesso", "content": turma} #type: ignore

    @staticmethod
    async def get_all(): #type: ignore
        turmas = await Turma.get_all()
        return {"status": "OK", "content": turmas} #type: ignore

    @staticmethod
    async def get_by_id(turma_id: str): #type: ignore
        turma = await Turma.get_by_id(turma_id)
        if not turma:
            return {"status": "ERROR", "msg": "Turma não encontrada"}
        return {"status": "OK", "content": turma} #type: ignore

    @staticmethod
    async def update(turma_id: str, data: dict[str, Any]):
        updated = await Turma.update_turma(turma_id, data)
        if not updated:
            return {"status": "ERROR", "msg": "Turma não encontrada"}
        return {"status": "OK", "msg": "Turma atualizada com sucesso"}

    @staticmethod
    async def delete(turma_id: str):
        deleted = await Turma.delete_turma(turma_id)
        if not deleted:
            return {"status": "ERROR", "msg": "Turma não encontrada"}
        return {"status": "OK", "msg": "Turma deletada com sucesso"}
