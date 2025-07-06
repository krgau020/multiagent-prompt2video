# tools.py
from crewai_tools import SerperDevTool, BaseTool





from dotenv import load_dotenv
load_dotenv()
import os

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')


# Web search tool using Serper.dev
web_search_tool = SerperDevTool()


from crewai_tools import BaseTool
from typing import Optional

class VideoGeneratorTool(BaseTool):
    name: str = "Video Generator Tool"
    description: str = "Generates a mock video output based on script and visuals"

    def _run(self, query: str, **kwargs) -> str:
        # Simulate video output
        return f"🎬 [Mock Video Output]:\n\n{query}"