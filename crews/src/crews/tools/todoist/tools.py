from crewai.tools import tool
from integrations.todoist.helpers import get_all_tasks_for_a_week
from pydantic import BaseModel
from integrations.todoist.config import todoist
from datetime import datetime
from todoist_api_python.models import Task as TodoistTask

class OneWeekUnAvailableTime(BaseModel):
    dates_unavailable_to_create_task: list[str]


class due_datetime(BaseModel):
    due_date: str
    due_time: str

class NewTodoistTask(BaseModel):

    """
        This tool creates a todoist task on the given due date.
        The arguments are:
        content: The content of the task.
        description: The description of the task.
        due_datetime: The due date and time of the task.
    """

    content: str
    description: str
    due_datetime: datetime


class CreateTodoistTaskOnSchedule(BaseModel):

    """
        This tool creates a todoist task on the given due date. 
    """

    task: NewTodoistTask


@tool("get_one_week_todoist_schedule_tool")
def get_one_week_todoist_schedule() -> OneWeekUnAvailableTime:
    """
    This tool returns the one week schedule for todoist.
    The time which this tool returns are the time when I'm already working on a taks and can't take a new taks on these time of the week.
    Most of the time, there will be a time, but sometimes, there will be no time but just a date.

    For example:

    {
        "dates_unavailable_to_create_task": ['2025-05-05 15:45:00', '2025-05-06 15:45:00', '2025-05-07 15:45:00', '2025-05-05', '2025-05-06', '2025-05-07']
    }

    """

    due_tasks = get_all_tasks_for_a_week()

    master_unavailable_times = []

    for task in due_tasks:
        master_unavailable_times.append(task.due.string)

    print("master_unavailable_times: ", master_unavailable_times)

    return OneWeekUnAvailableTime(dates_unavailable_to_create_task=master_unavailable_times).model_dump()


@tool("create_todoist_task_on_schedule_tool")
def create_todoist_task_on_schedule(
    title: str, description: str, due_datetime: datetime
) -> TodoistTask | None:
    """
    This tool creates a todoist task on the given due date.

    For example:

    { 
        "task": {
            "title": "This is a new task",
            "description": "This is a new task description",
            "due_datetime": "2025-05-05 15:45:00"
        }
    }  

    If the task is created successfully, it returns the created task, otherwise, it returns None.

    """

    try:

        created_task = todoist.add_task(
            content=title,
            description=description,
            due_datetime=due_datetime,
            labels=["job"]
        )

        return created_task

    except Exception as e:
        print(f"Error: {e}")
        return None
