
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from service.Serivce_adm import ServiceAdm
from domains.User.Model_adm import Model_LoginAdm, Model_RegisterAdm
from config.security.Security_jwt import JWTBearer

router = APIRouter(prefix="/v1/adm", tags=["Administrador"])


@router.post("/register")
async def register_adm(payload: Model_RegisterAdm): #type: ignore
    result = await ServiceAdm.register(payload.model_dump()) #type: ignore
    status_code = 201 if result["status"] == "OK" else 400
    
    return JSONResponse(status_code=status_code, content=jsonable_encoder(result))


@router.post("/login")
async def login_adm(payload: Model_LoginAdm): #type: ignore
    result = await ServiceAdm.login(payload.model_dump()) #type: ignore
    status_code = 200 if result["status"] == "OK" else 401
    
    return JSONResponse(status_code=status_code, content=jsonable_encoder(result))


@router.get("/get/all", dependencies=[Depends(JWTBearer())])
async def get_all_adms():
    result = await ServiceAdm.get_all() #type: ignore
    
    return JSONResponse(status_code=200, content=jsonable_encoder(result))