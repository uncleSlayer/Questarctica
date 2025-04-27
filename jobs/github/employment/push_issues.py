from config.env import settings
from github import enable_console_debug_logging
from jobs.github.config import g
import pprint
# enable_console_debug_logging()

try:

    work_repository_urls = [settings.COMPANY_REPO_1, settings.COMPANY_REPO_2]

    for work_repository_url in work_repository_urls:
        work_repo = g.get_repo(work_repository_url)
        issues = work_repo.get_issues(state="open", assignee="uncleSlayer")

        for issue in issues:
            pprint.pprint({
                "issue_number": issue.number,
                "issue_title": issue.title,
                "issue_description": issue.body
            })

except Exception as e:
    print(f"Error: {e}")
    exit(1)
