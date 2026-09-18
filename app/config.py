from pydantic_settings import BaseSettings, SettingsConfigDict
import os

print("Directorio actual:", os.getcwd())
print("Existe .env:", os.path.exists(".env"))


class Settings(BaseSettings):
    DB_URL: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )

settings = Settings()

# print("DB_URL:", settings.DB_URL)

##-----------------------
#
# Posible future configuration 
#
#------------------------

# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_PORT = os.getenv("DB_PORT")

# STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")