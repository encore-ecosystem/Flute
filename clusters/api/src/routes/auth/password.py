from passlib.context import CryptContext

password_context = CryptContext(
    schemes    = 'bcrypt',
    deprecated = 'auto',
)


class HashPassword:
    @staticmethod
    def hash(password: str) -> str:
        return password_context.hash(password)

    @staticmethod
    def verify(plain_password: str, hashed_password: str) -> bool:
        return password_context.verify(plain_password, hashed_password)


__all__ = [
    'HashPassword'
]