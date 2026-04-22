from sqlalchemy.ext.asyncio import AsyncSession

from core.security import Security
from crud.crud_base import CrudBase
from schemas.user import CreateUser
from models.user import User


class UserCrud(CrudBase):

    def __init__(self, model):
        self.model = model

    async def create(
            self,
            session: AsyncSession,
            obj_in: CreateUser,
    ):
        obj_in_data = obj_in.model_dump()
        password = obj_in_data.pop('password')
        password_hash = Security.hash_password(password)
        db_user = User(password_hash=password_hash, **obj_in_data,)
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user


user_crud = UserCrud(User)
