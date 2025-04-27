from github import Github
from config.env import settings
from github import enable_console_debug_logging


class GithubIntegration:
    def __init__(self, debug=False):

        if debug:
            enable_console_debug_logging()

        self.g = Github(settings.GITHUB_PERSONAL_ACCESS_TOKEN)

    def create_github_instance(self):
        return Github(settings.GITHUB_PERSONAL_ACCESS_TOKEN)


# Pass debug=True to enable debug logging
g = GithubIntegration().create_github_instance()
