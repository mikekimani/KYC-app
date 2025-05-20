from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from backend.database import Base, engine
from backend.auth import models, routes as auth_routes, auth_utils
from backend.kyc import routes as kyc_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_routes.router)
app.include_router(kyc_routes.router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@app.get("/me")
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = auth_utils.decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return {"username": payload.get("sub")}
