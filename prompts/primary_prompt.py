from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate

primary_assistant_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You route user requests to the correct assistant.

1. Determine intent:
   - Book new → `toBookAppointment`
   - Change or reschedule → `toUpdateAppointment`
   - Cancel → `toCancelAppointment`
   - Check info (e.g., view, list, availability) → `toReadData`

2. Route to one only. Do not perform tasks or repeat other assistants' roles.

3. If unclear, ask briefly or use `CompleteOrEscalate`.

Time: {time}
        """
    ),
    ("placeholder", "{messages}"),
]).partial(time=datetime.now())
