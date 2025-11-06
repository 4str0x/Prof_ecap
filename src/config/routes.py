from fastapi import APIRouter

from controller import Controller_token as controller_token
from controller import Controller_turma as controler_turma
from controller import Controller_aluno as controller_aluno

router = APIRouter()

router.include_router(controller_token.router)  # type: ignore
router.include_router(controler_turma.router)
router.include_router(controller_aluno.router)