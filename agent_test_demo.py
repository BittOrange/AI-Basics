from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.llms import OpenAI
import math
import os
from dotenv import load_dotenv

# load openai api key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# initialize the llm
llm = OpenAI(temperature=0, openai_api_key=api_key)

# create a simple rool (calculating square root)
def sqrt_tool(input: str) -> str:
    number = float(input)
    return str(math.sqrt(number))

tools = [
    Tool.from_function(
        name = "Square Root Calculator",
        description = "Use this to calculate the square root of a number",
        func = sqrt_tool
    )
]

# create the agent
agent = initialize_agent(
    tools,
    llm,
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True
)

# test the agent    
agent.run("What is the square root of 198?")
