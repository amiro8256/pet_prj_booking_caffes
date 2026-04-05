from sqlalchemy.ext.asyncio import AsyncSession

from core.security import Security
from schemas.user import CreateUser
from models import User


class UserCrud:

    def __init__(self, model):
        self.model = model

    async def create(self, session: AsyncSession, obj_in: CreateUser):
        obj_in_data = obj_in.model_dump()
        password = obj_in_data.pop('password')
        password_hash = Security.hash_password(password)
        db_user = User(**obj_in_data, password_hash=password_hash)
        # проверить как сессия передаётся генератором сессий
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user


user_crud = UserCrud(User)
