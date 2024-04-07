from fastapi import APIRouter

from src.common.schemas.ext import Msg
from src.router.schemas import ListResponse

router = APIRouter()


@router.get("/", response_model=Msg)
def index():
    return {"msg": "Столповких Данил Юрьевич"}


@router.get("/users", response_model=ListResponse)
def get_users():
    return {"items": ["tg: @strannik1105", "you don't need my phone number"]}


@router.get("/tools", response_model=ListResponse)
def get_tools():
    return {"items": ["C/C++", "Python", "FastApi", "PostgreSQL", "Clickhouse", "Redis", "RabbitMQ"]}
