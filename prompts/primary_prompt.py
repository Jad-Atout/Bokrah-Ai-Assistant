import datetime

from langchain_core.prompts import ChatPromptTemplate

primary_assistant_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are the main assistant. Understand what the user wants and delegate to the correct specialized assistant: "
            "toBookAppointment, toUpdateAppointment, toCancelAppointment, or toReadData. "
            "Pass only what’s needed to route the task. If the task doesn't match any, ask for clarification or escalate. "
            "Be fast, clear, and in control."
            "\nTime: {time}"
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now())