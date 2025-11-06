from fastapi import APIRouter

from controller import Controller_token as controller_token
from controller import Controller_turma as controler_turma

router = APIRouter()

router.include_router(controller_token.router)  # type: ignore
router.include_router(controler_turma.router)