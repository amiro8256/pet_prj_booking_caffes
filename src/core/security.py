from passlib.context import CryptContext


class Security:
    """Класс обработки и проверки пароля."""

    _pwd_context = CryptContext(schemes=['bcrypt-sha256'])

    @classmethod
    def hash_password(cls, password: str) -> str:
        """Хэширует пароль xthtp bcrypt с предварительным SHA-256 прехэшем."""
        hash_pwd = cls._pwd_context.hash(password)
        return hash_pwd

    def verify_password(self, plain_password: str, hash_password: str) -> bool:
        """Проверяет пароль, сравнивая его хэш с сохранённым bcrypt-хэшем."""
        return self._pwd_context.verify(plain_password, hash_password)


security = Security()
