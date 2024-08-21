from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.api.v1.crud.crud import get_user_by_id
from app.core.security import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/signin")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    user = get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user