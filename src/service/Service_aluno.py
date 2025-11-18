from typing import Any

from domains.Aluno.Model_aluno import Aluno

class ServiceAluno:
    @staticmethod
    async def create(data: dict[str, Any]): #type: ignore
        aluno = await Aluno.create_aluno(data)
        return {"status": "OK", "msg": "aluno criada com sucesso", "content": aluno} #type: ignore

    @staticmethod
    async def get_all(): #type: ignore
        alunos = await Aluno.get_all()
        return {"status": "OK", "content": alunos} #type: ignore

    @staticmethod
    async def get_by_id(turma_id: str): #type: ignore
        aluno = await Aluno.get_by_id(turma_id)
        if not aluno:
            return {"status": "ERROR", "msg": "aluno não encontrada"}
        return {"status": "OK", "content": aluno} #type: ignore

    @staticmethod
    async def update(turma_id: str, data: dict[str, Any]):
        updated = await Aluno.update_aluno(turma_id, data)
        if not updated:
            return {"status": "ERROR", "msg": "Turma não encontrada"}
        return {"status": "OK", "msg": "Turma atualizada com sucesso"}

    @staticmethod
    async def delete(turma_id: str):
        deleted = await Aluno.delete_aluno(turma_id)
        if not deleted:
            return {"status": "ERROR", "msg": "Turma não encontrada"}
        return {"status": "OK", "msg": "Turma deletada com sucesso"}
