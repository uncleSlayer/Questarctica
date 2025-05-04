from crewai import Agent, Task, Crew
from textwrap import dedent
from pydantic import BaseModel


class GithubIssue(BaseModel):
    seriel_number: str
    title: str
    body: str
    url: str


class GithubToTodoistTaskDescriptionOutput(BaseModel):
    task_description: str


class GithubToTodoistCrew:

    def __init__(self, github_issue: GithubIssue):
        self.github_issue = github_issue

    def github_issues_to_todoist_tasks_description_writer_agent(self):

        return Agent(
            role="You are a Github Issue to Todoist Task description writer agent.",
            goal="Go through the github issue and write a todoist task description for it in markdown format.",
            backstory=dedent(
                """

                EXTREMELY IMPORTANT: DO NOT AT ALL USE ESCAPE SEQUENCES IN YOUR OUTPUT. THINK THAT YOU ARE WRITING THIS OUTPUT DIRECTLY IN TODOIST DESCRIPTION FIELD.

                You are a Github Issue to Todoist Task description writer agent. 
                You get the github issue in the following format:
                
                {
                    "seriel_number": "Seriel Number of the Github Issue",
                    "title": "Title of the Github Issue",
                    "body": "Body of the Github Issue in Markdown format",
                    "url": "Url of the Github Issue"
                }

                Your task is to write todoist task description for the Github Issue. 

                Please generate the markdown content for: [your specific request]

                Todoist description should be written in markdown format.

                Todoist does not support markdown in full so you have to keep in mind the following rules:

                | Element                   | Support | Notes                                                        |
                |---------------------------|---------|-------------------------------------------------------------|
                | Headings                  | Yes     | Supported in comments only.                                 |
                | Paragraphs                | Yes     |                                                             |
                | Line Breaks               | Yes     | Supported in comments only. You can press Return once.      |
                | Bold                      | Yes     |                                                             |
                | Italic                    | Yes     |                                                             |
                | Blockquotes               | Yes     | Supported in comments only.                                 |
                | Ordered Lists             | Yes     | Supported in comments only.                                 |
                | Unordered Lists           | Yes     | Supported in comments only.                                 |
                | Code                      | Yes     |                                                             |
                | Horizontal Rules          | Yes     |                                                             |
                | Links                     | Yes     |                                                             |
                | Images                    | No      |                                                             |
                | Tables                    | No      | No longer supported in the latest version.                  |
                | Fenced Code Blocks        | Yes     |                                                             |
                | Syntax Highlighting       | No      |                                                             |
                | Footnotes                 | No      |                                                             |
                | Heading IDs               | No      |                                                             |
                | Definition Lists          | No      |                                                             |
                | Strikethrough             | Yes     |                                                             |
                | Task Lists                | Yes     | Supported in comments only.                                 |
                | Emoji (copy and paste)    | Yes     |                                                             |
                | Emoji (shortcodes)        | No      |                                                             |
                | Highlight                 | No      |                                                             |
                | Subscript                 | No      |                                                             |
                | Superscript               | No      |                                                             |
                | Automatic URL Linking     | Yes     |                                                             |
                | HTML                      | No      |                                                             | 
            """
            ),
        )

    def create_github_issue_to_todoist_description_task(self):

        return Task(
            description=dedent(
                f"""
                You are a Github Issue to Todoist Task description writer agent.
                Read the following github issue thoroughly, find out what is the title, body, url, issue number of the issue and write a todoist task description for it in markdown format.
                Following is the github issue details:
                
                title: {self.github_issue.title}
                body: {self.github_issue.body}
                url: {self.github_issue.url}
                issue number: {self.github_issue.seriel_number}
            """
            ),
            expected_output=dedent(
                f"""
                A todoist task description for the github issue in todoist supported markdown format. 
                """
            ),
            agent=self.github_issues_to_todoist_tasks_description_writer_agent(),
            output_pydantic=GithubToTodoistTaskDescriptionOutput,
        )

    def schedule_fixer_agent(self):
        return Agent(
            goal="Create a task in my todoist account to fix the github issue.",
            backstory=dedent(
                """
                You are a Github Issue to Todoist Task description writer agent and you manage my todoist account.
                
                Based on my daily routine, and my availability, you have to create a task in my todoist account to fix the github issue.

                Following is some pointers regarding my daily routine:
                - I am a software engineer and I work on a lot of github issues.
                - I have a todoist account and I use it to manage my daily tasks.
                - I wake up at around 6:00 am and get my morning routine done by 15 minutes before 8 am.
                - I work go through my todoist account tasks and think about the whole day for 15 minutes.
                - I start working on the githug issues assigned to me from 9 am to 11 am.
                - On Tuesday, Thursday and Saturday, I attend my daily standup meeting at 11 am, which lasts for about 30 minutes to an hour.
                - Again from 11 am to 1 pm, I work on my github issues.
                - I go for a quick bath and have my lunch from 1 pm to 2:30 pm.
                - I take a break from 2:30 pm to 3 pm.
                - I again start working on my github issues from 3 pm to 5 pm and then call it a day.
                - On Saturdays and Sundays, I don't work on my github issues.
            """
            ),
            role="You are a Todoist task creator agent.",
            tools=[],
            verbose=True,
        )

    def kick_off(self):
        crew = Crew(
            name="GithubToTodoistCrew",
            agents=[self.github_issues_to_todoist_tasks_description_writer_agent()],
            tasks=[self.create_github_issue_to_todoist_description_task()],
            verbose=True,
        )
        output = crew.kickoff()

        output_parsed = output.to_dict().get("task_description").encode('utf-8').decode('unicode_escape')

        return output_parsed
