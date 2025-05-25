from pydantic import BaseModel


class SupervisorRequest(BaseModel):
    """Return control to the supervisor with a reason, data request or ending of task"""
    reason: str
