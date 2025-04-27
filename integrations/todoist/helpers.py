from integrations.todoist.config import todoist
from pydantic import BaseModel
import datetime


class ChildTask(BaseModel):
    content: str | None
    due_date: str | None
    due_datetime: datetime.datetime | None
    project_id: str | None
    parent_task_id: str | None


class Task(BaseModel):
    title: str
    description: str | None
    due_date: str | None
    due_datetime: datetime.datetime | None
    steps: list[ChildTask] | None
    project_id: str | None


def create_parent_task(task: Task):

    try:

        task = todoist.add_task(
            content=task.title,
            description=task.description,
            due_date=task.due_date,
            due_datetime=task.due_datetime,
            project_id=task.steps[0].project_id,
        )

    except Exception as e:
        print(f"Error: {e}")
        return None

    return task
