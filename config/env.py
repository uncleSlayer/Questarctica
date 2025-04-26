from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()


class Settings(BaseSettings):
    GITHUB_PERSONAL_ACCESS_TOKEN: str = os.getenv(
        "GITHUB_PERSONAL_ACCESS_TOKEN", ""
    )
    COMPANY_REPO_1: str = os.getenv("COMPANY_REPO_1", "")
    COMPANY_REPO_2: str = os.getenv("COMPANY_REPO_2", "")


# Instantiate the settings
settings = Settings()