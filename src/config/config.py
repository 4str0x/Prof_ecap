from pydantic_settings import BaseSettings, SettingsConfigDict

class _Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # --------------------
    # SERVER CONFIG
    # --------------------
    PORT: int = 80
    HOST: str = "0.0.0.0"

    # --------------------
    # JWT / AUTH
    # --------------------
    SECRET: str = ""
    JWT_SECRET_KEY: str = ""
    EXPIRES_IN: int = 5  # em minutes
    
    # --------------------
    # MongoDB
    # --------------------
    MONGO_URI: str = ""
    MONGO_DB_NAME: str = ""

    # --------------------
    # DEV MODE
    # --------------------
    # Quando True, sobrescreve PORT/HOST para valores de desenvolvimento (5050, localhost)
    DEV_MODE: bool = False

settings = _Settings()

# Se o .env definir DEV_MODE=true, usar porta e host de desenvolvimento
if settings.DEV_MODE:
    settings.PORT = 5050
    settings.HOST = "localhost"