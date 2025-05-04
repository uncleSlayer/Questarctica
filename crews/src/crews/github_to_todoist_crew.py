from crewai import Agent, Task
from textwrap import dedent
from pydantic import BaseModel


class GithubIssue(BaseModel):
    seriel_number: str
    title: str
    body: str
    url: str


class GithubToTodoistCrew:

    def github_issues_to_todoist_tasks_creator_agent(self):

        return Agent(
            goal="You are a Github Issue to Todoist Task description writer agent.",
            role="Go through the github issue and write a todoist task description for it in markdown format.",
            backstory=dedent(
                """
            You are a Github Issue to Todoist Task description writer agent.
            You get the github issue in the following format:
            
            {
                "seriel_number": "Seriel Number of the Github Issue",
                "title": "Title of the Github Issue",
                "body": "Body of the Github Issue in Markdown format",
                "url": "Url of the Github Issue"
            }

            Your task is to write todoist task description for the Github Issue.
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

    def create_github_issue_to_todoist_task(self, github_issue: GithubIssue):

        return Task(
            description=dedent(
                f"""
                You are a Github Issue to Todoist Task description writer agent.
                Read the following github issue thoroughly, find out what is the title, body, url, issue number of the issue and write a todoist task description for it in markdown format.
                Following is the github issue details:
                
                title: {github_issue.title}
                body: {github_issue.body}
                url: {github_issue.url}
                issue number: {github_issue.seriel_number}
            """
            ),
            expected_output=dedent(
                f"""
                A todoist task description for the github issue in todoist supported markdown format.
                """
            ),
            agent=self.github_issues_to_todoist_tasks_creator_agent(),
        )
