from crewai import Agent, Crew, Task, Process
from langchain_openai import ChatOpenAI
from config.env import settings
from dotenv import load_dotenv
from crewai import LLM


class IssueManagerCrew(Crew):

    def __init__(self):
        load_dotenv()
        super().__init__(
            agents=[self.github_issue_to_todoist_converter()],
            tasks=[self.github_issue_to_todoist_converter_task()],
            process=Process.sequential,
            verbose=True
        )

    def github_issue_to_todoist_converter(self) -> Agent:

        todoist_markdown_support = """
            | Element                  | Support | Notes                                                        |
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
            | Disabling Automatic URL Linking | Yes | Supported in comments only.                               |
            | HTML                      | No      |                                                             |
        """

        return Agent(
            role="Todoist task description writer",
            goal=f"""Translate GitHub issues into Todoist task descriptions

                    Below is the rules of Todoist task descriptions:
                    {todoist_markdown_support}
                """,
            backstory="""
                An experienced GitHub issue to Todoist task description writer. Who takes GitHub issues and translates them into Todoist task descriptions.
                You know the rules of Todoist task descriptions, and you know how to write them.
            """,
            verbose=True,
            # llm=LLM(
            #     model="gpt-3.5-turbo",
            #     api_key=settings.OPENAI_API_KEY
            # )
        )


    def github_issue_to_todoist_converter_task(self) -> Task:
        return Task(
            description="Translate GitHub issues into Todoist task descriptions.",
            expected_output="Todoist task description in todoist supported markdown.",
            agent=self.github_issue_to_todoist_converter()
        )

