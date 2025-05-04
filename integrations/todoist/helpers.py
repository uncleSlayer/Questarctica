from integrations.todoist.config import todoist
from pydantic import BaseModel
# from todoist import Task as TodoistTask
from datetime import datetime
from datetime import timedelta

class ChildTask(BaseModel):
    content: str | None
    due_date: str | None
    due_datetime: datetime | None
    project_id: str | None
    parent_task_id: str | None


class Task(BaseModel):
    title: str
    description: str | None
    due_date: str | None
    due_datetime: datetime | None
    steps: list[ChildTask] | None
    project_id: str | None


def create_parent_task(task: Task):

    try:

        task = todoist.add_task(
            content=task.title,
            description=task.description,
            due_date=task.due_date if task.due_date else None,
            due_datetime=task.due_datetime if task.due_datetime else None,
            # project_id=task.steps[0].project_id if task.steps else None,
        )

    except Exception as e:
        print(f"Error: {e}")
        return None

    return task


def get_all_tasks_by_project(
    project_id: str,
) -> list[Task] | None:
    try:
        tasks = todoist.filter_tasks(query="due after: 2025-04-28")
        return tasks
    except Exception as e:
        print(f"Error: {e}")
        return None
    

def get_all_tasks_for_a_week() -> list[Task] | None:
    try:

        today = datetime.today().date()

        tasks = todoist.filter_tasks(query=f"due after: {today} & due before: {today + timedelta(days=7)}")

        for task_list in tasks:
            for task in task_list:
                print(task)

        return tasks
    except Exception as e:
        print(f"Error: {e}")
        return None
