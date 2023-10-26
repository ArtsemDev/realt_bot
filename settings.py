from aiogram import Bot, Dispatcher
from pydantic import SecretStr
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    TOKEN: SecretStr


settings = Settings()
bot = Bot(
    token=settings.TOKEN.get_secret_value(),
    parse_mode="HTML"
)
dp = Dispatcher()
