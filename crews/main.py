from fastapi import FastAPI
from src.crews.github_to_todoist_crew import GithubToTodoistCrew, GithubIssue
from crewai import Crew
from pprint import pprint

app = FastAPI()


@app.post("/job/task/create")
def read_root(github_issues: list[GithubIssue]):

    pprint(github_issues)

    for github_issue in github_issues:
        github_to_todoist_crew = GithubToTodoistCrew(github_issue=github_issue)
        github_to_todoist_crew.kick_off()

    return {"output": "succeed"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
