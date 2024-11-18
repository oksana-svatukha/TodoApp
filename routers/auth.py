from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.util import deprecated

from models import Users
from passlib.context import CryptContext


router = APIRouter()

bcrypt_contex = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Createuserrequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

@router.post("/auth/")
async def create_user(create_user_request: Createuserrequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_contex.hash(create_user_request.password),
        is_active=True
    )
    return create_user_model





    return {"user": "authenticated"}