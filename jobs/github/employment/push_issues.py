from config.env import settings
from integrations.github.config import g
from pprint import pprint

# from integrations.todoist.helpers import (
#     create_parent_task,
#     Task,
#     get_all_tasks_by_project,
# )
from integrations.mongo.config import github_issues_collection

try:

    work_repository_urls = [settings.COMPANY_REPO_1, settings.COMPANY_REPO_2]

    for work_repository_url in work_repository_urls:
        work_repo = g.get_repo(work_repository_url)
        issues = work_repo.get_issues(state="open", assignee="uncleSlayer")

        for issue in issues:

            # check if the issue already exists in the database
            existing_issue = github_issues_collection.find_one({"id": issue.id})
            if existing_issue:
                # update the issue in the database
                github_issues_collection.update_one(
                    {"id": issue.id},
                    {
                        "$set": {
                            "title": issue.title,
                            "body": issue.body,
                            "url": issue.html_url,
                            "created_at": issue.created_at,
                            "updated_at": issue.updated_at,
                            "assignees": [assignee.name for assignee in issue.assignees],
                            "labels": [label.name for label in issue.labels],
                            "closed_at": issue.closed_at,
                        }
                    },
                )
                continue

            # create the issue in the database
            github_issues_collection.insert_one(
                {
                    "id": issue.id,
                    "title": issue.title,
                    "body": issue.body,
                    "url": issue.html_url,
                    "created_at": issue.created_at,
                    "updated_at": issue.updated_at,
                    "assignees": [assignee.name for assignee in issue.assignees],
                    "labels": [label.name for label in issue.labels],
                    "closed_at": issue.closed_at,
                }
            )

        # tasks_pages = get_all_tasks_by_project(project_id="")
        # all_tasks = []

        # for taks_list in tasks_pages:
        #     all_tasks.extend(taks_list)

        # for task in all_tasks:
        #     pprint(task)

        #     existing_task = github_issues_collection.find_one({"id": task.id})

        #     pprint("existing_task", existing_task)

        # for issue in issues:

        #     task = Task(
        #         title=issue.title,
        #         description=issue.body,
        #         due_date=None,
        #         due_datetime=None,
        #         steps=None,
        #         project_id=None,
        #     )

        #     t = create_parent_task(task)

        #     pprint(t)

except Exception as e:
    print(f"Error: {e}")
    exit(1)
