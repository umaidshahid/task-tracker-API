from datetime import datetime, timedelta
from typing import Optional
import jwt
from app.core.config import settings


ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
to_encode = data.copy()
if expires_delta:
expire = datetime.utcnow() + expires_delta
else:
expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
to_encode.update({"exp": expire})
encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
return encoded_jwt


def decode_access_token(token: str):
try:
payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
return payload
except jwt.PyJWTError:
return None