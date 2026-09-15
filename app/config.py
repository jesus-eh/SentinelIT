from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )

settings = Settings()


##-----------------------
#
# Posible configuracion de un futuro
#
#------------------------

# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_PORT = os.getenv("DB_PORT")

# STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")