"""
This file contains shared things for all other modules
"""
# ----
# env
# ----
from dotenv   import load_dotenv
from envparse import Env

load_dotenv()
env = Env()

# -----
# auth
# -----
from fastapi.security    import OAuth2PasswordBearer
from passlib.context     import CryptContext

JWT_SECRET_KEY              = env.str("JWT_SECRET_KEY")
JWT_ALGORITHM               = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme               = OAuth2PasswordBearer(tokenUrl="login")
pwd_context                 = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ---------
# Database
# ---------
from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URL = env.str("MONGODB_URL", default="mongodb://localhost:27017/")
database    = AsyncIOMotorClient(MONGODB_URL)

COL_USERS = "users"
FLUTE_DB  = "flute_db"

# ------
# Other
# ------
STATUS      = "status"
DESCRIPTION = "description"
TOKEN       = "token"
PORT        = env.int("PORT", default=8010)
