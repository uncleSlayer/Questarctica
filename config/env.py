from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    GITHUB_PERSONAL_ACCESS_TOKEN: str = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN", "")
    COMPANY_REPO_1: str = os.getenv("COMPANY_REPO_1", "")
    COMPANY_REPO_2: str = os.getenv("COMPANY_REPO_2", "")
    TODOIST_API_TOKEN: str = os.getenv("TODOIST_API_TOKEN", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")


settings = Settings()
