from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from config import settings
from datetime import datetime, timedelta, timezone
import jwt

security = HTTPBearer()

def crear_token(user_id: int, nombre: str):
    payload = {
            "sub": str(user_id),
            "nombre": nombre,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_EXPIRE_MINUTES),
            }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

def verificar_jwt(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        return jwt.decode(
                credentials.credentials,
                settings.JWT_SECRET,
                algorithm=[settings.JWT_ALGORITHM],
                )
    except jwt.PyJWTError:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token invalido o expirado"
                )

