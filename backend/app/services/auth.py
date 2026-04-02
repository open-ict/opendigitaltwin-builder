from datetime import datetime, timedelta, timezone
from jose import jwt

def create_access_token(secret_key: str, subject: str, role: str = "admin", expires_minutes: int = 1440) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    payload = {"sub": subject, "role": role, "exp": expire}
    return jwt.encode(payload, secret_key, algorithm="HS256")
