from pydantic_settings import BaseSettings
from fastapi_mail import ConnectionConfig

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL:str
    SECRET_KEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_TIME:int 
    GROQ_API_KEY:str
    DEV_DB_RESET:str
    MODEL_NAME:str


    class Config:
        env_file = ".env"




conf = ConnectionConfig(
    MAIL_USERNAME="shayanumar277@gmail.com",
    MAIL_PASSWORD="ghmk eqhk nuai xban",  # use App Password for Gmail
    MAIL_FROM="shayanumar277@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)



settings = Settings()
