from config.env import settings
from integrations.github.config import g
from pprint import pprint
from integrations.todoist.helpers import create_parent_task, Task
try:

    work_repository_urls = [settings.COMPANY_REPO_1, settings.COMPANY_REPO_2]

    for work_repository_url in work_repository_urls:
        work_repo = g.get_repo(work_repository_url)
        issues = work_repo.get_issues(state="open", assignee="uncleSlayer")

        for issue in issues:

            task = Task(
                title=issue.title,
                description=issue.body,
                due_date=None,
                due_datetime=None,
                steps=None,
                project_id=None,
            )

            t = create_parent_task(task)

            pprint(t)

except Exception as e:
    print(f"Error: {e}")
    exit(1)
