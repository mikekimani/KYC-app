import os

JWT_SECRET = os.getenv("JWT_SECRET", "your_super_secret_key")
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30