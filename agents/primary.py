from prompts.primary_prompt import supervisor_agent_prompt
from tools import assign_to_create, assign_to_update, assign_to_cancel, assign_to_reader
from utils import llm
from langgraph.prebuilt import create_react_agent
supervisor_agent = create_react_agent(
    model=llm,
    tools=[assign_to_create, assign_to_update, assign_to_cancel, assign_to_reader],
    prompt=supervisor_agent_prompt,
    name="supervisor",
)