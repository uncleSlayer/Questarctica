from todoist_api_python.api import TodoistAPI
from config.env import settings

todoist = TodoistAPI(settings.TODOIST_API_TOKEN)