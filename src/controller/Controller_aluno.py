from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from service.Service_aluno import ServiceAluno
from domains.Aluno.Model_aluno import Aluno, Model_RegisterAluno
from config.security.Security_jwt import JWTBearer

router = APIRouter(prefix="/v1/aluno", tags=["Alunos"])


@router.post("/create", dependencies=[Depends(JWTBearer())])
async def create_turma(payload: Model_RegisterAluno):
    result = await ServiceAluno.create(payload.model_dump()) #type: ignore
    status_code = 201 if result["status"] == "OK" else 400
    return JSONResponse(status_code=status_code, content=jsonable_encoder(result))


@router.get("/get/all", dependencies=[Depends(JWTBearer())])
async def get_all_alunos():
    result = await ServiceAluno.get_all() #type: ignore
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@router.get("/get/{aluno_id}", dependencies=[Depends(JWTBearer())])
async def get_aluno_by_id(aluno_id: str):
    result = await ServiceAluno.get_by_id(aluno_id) #type: ignore
    status_code = 200 if result["status"] == "OK" else 404
    return JSONResponse(status_code=status_code, content=jsonable_encoder(result))


@router.put("/update/{aluno_id}", dependencies=[Depends(JWTBearer())])
async def update_aluno(aluno_id: str, payload: Model_RegisterAluno):
    result = await ServiceAluno.update(aluno_id, payload.model_dump())
    status_code = 200 if result["status"] == "OK" else 404
    return JSONResponse(status_code=status_code, content=jsonable_encoder(result))


@router.delete("/delete/{aluno_id}", dependencies=[Depends(JWTBearer())])
async def delete_aluno(aluno_id: str):
    result = await ServiceAluno.delete(aluno_id)
    status_code = 200 if result["status"] == "OK" else 404
    return JSONResponse(status_code=status_code, content=jsonable_encoder(result))

