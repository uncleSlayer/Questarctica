from integrations.todoist.config import todoist
from pydantic import BaseModel
from datetime import datetime
from datetime import timedelta
from itertools import chain
from todoist_api_python.models import Task as TodoistTask


def get_all_tasks_for_a_week() -> list[TodoistTask] | None:
    try:

        today = datetime.today().date()

        tasks_iterator = todoist.filter_tasks(
            query=f"{today} & due before: {today + timedelta(days=7)} & @job"
        )

        todoist_format_task = list(chain.from_iterable(tasks_iterator))

        return todoist_format_task

    except Exception as e:
        print(f"Error: {e}")
        return None
