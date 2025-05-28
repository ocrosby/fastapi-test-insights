from typing import List, Optional
from pydantic import BaseModel

class TestCase(BaseModel):
    name: str
    classname: str
    time: float
    status: str = "passed"
    failure_message: Optional[str] = None

class TestSuite(BaseModel):
    name: str
    time: float
    testcases: List[TestCase] = []
    children: List["TestSuite"] = []

TestSuite.update_forward_refs()
