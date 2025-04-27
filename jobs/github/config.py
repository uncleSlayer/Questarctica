from github import Github
from config.env import settings

g = Github(settings.GITHUB_PERSONAL_ACCESS_TOKEN)