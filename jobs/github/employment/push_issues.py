from github import Github
from config.env import settings
from github import enable_console_debug_logging

# enable_console_debug_logging()

try:

    g = Github(settings.GITHUB_PERSONAL_ACCESS_TOKEN)

    work_repository_urls = [settings.COMPANY_REPO_1, settings.COMPANY_REPO_2]

    for work_repository_url in work_repository_urls:
        print(f"Working on {work_repository_url}")
        work_repo = g.get_repo(work_repository_url)
        issues = work_repo.get_issues(state="open", assignee="uncleSlayer")

        print(f"Issues for {work_repository_url}:")
        for issue in issues:
            print(issue)

except Exception as e:
    print(f"Error: {e}")
    exit(1)
