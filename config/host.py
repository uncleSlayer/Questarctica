from env import settings

HOST = (
    "http://localhost:8000"
    if settings.ENV == "dev"
    else "https://questarctica-api.siddhantota.in"
)
