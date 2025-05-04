from fastapi import FastAPI
from src.crews.github_to_todoist_crew import GithubToTodoistCrew, GithubIssue
from crewai import Crew

app = FastAPI()


@app.get("/")
def read_root():

    github_to_todoist_crew = GithubToTodoistCrew()

    agent = github_to_todoist_crew.github_issues_to_todoist_tasks_creator_agent()
    task = github_to_todoist_crew.create_github_issue_to_todoist_task(github_issue=GithubIssue(
        seriel_number="942",
        title="Reduce API calls",
        body="""
            Currently, the playbook is making multiple unnecessary query API calls during its execution. These redundant calls are leading to increased network traffic, slower performance, and potential rate-limiting issues, especially when the playbook is triggered frequently or used at scale.

            Upon reviewing the code, it appears that some API queries are being repeated even though the data is already available in memory or fetched earlier in the flow. This not only adds latency but also increases the risk of inconsistent data if responses vary slightly over time.

            ### Impact:

            Unnecessary network overhead

            Slower user experience

            Higher load on backend services

            Potential API rate limit breaches

            ### Suggested Fix:

            Identify and eliminate repeated or redundant API calls.

            Ensure any necessary calls are made only once per execution flow.

            ### Steps to Reproduce:

            Open the playbook.

            Update or add a window function  or add filters in filter group

            Observe the network tab or API logs to see repeated calls to the same endpoint(s).

            ### Expected Behavior:

            Each required API call should be made only once per context.
        """,
        url="https://github.com/silzila/silzila-saas-frontend/issues/942"
    )) 

    crew = Crew(name="GithubToTodoistCrew", agents=[agent], tasks=[task], verbose=True)

    output = crew.kickoff()

    print(output)

    return {"output": output}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)