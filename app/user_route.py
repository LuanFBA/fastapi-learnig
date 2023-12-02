from fastapi import APIRouter
from bson import ObjectId
from core.models import User
from core.schemas import list_serial
from core.database import collection

user_router = APIRouter()

@user_router.get("/")
async def get_users():
    return list_serial(collection.find({ "enable": True}))

@user_router.get("/{id}")
async def get_user_by_id(id: str):
    return list_serial(collection.find({"_id": ObjectId(id)}))
    

@user_router.post("/")
async def post_user(user: User):
    collection.insert_one(dict(user))

@user_router.put("/{id}")
async def put_user(id: str, user: User):
    collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})

@user_router.delete("/{id}")
async def delete_user(id: str):
    collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"enable": False}})
