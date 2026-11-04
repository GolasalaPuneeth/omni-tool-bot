from enum import StrEnum
from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field
from pydantic_ai import UseEnumMemberDocstrings

class Category(UseEnumMemberDocstrings, StrEnum):
    generic = 'generic'
    """General greetings, identity questions, or casual conversation."""

    time = 'time'
    """Questions asking about the current time, date, schedule, or timezones."""

    math = 'math'
    """Arithmetic problems, numbers, equations, or calculations to perform."""

    image = 'image'
    """Requests asking to generate, see, display, create, or show an image or picture."""

class QueryEvaluation(BaseModel):
    """Evaluate query attributes using Jev primitives."""

    model_config = ConfigDict(use_attribute_docstrings=True)

    # CHOICE: Enum selection
    category: Category
    """Which primary category matches the user's intent?"""

    # NOUL: Continuous truth probability bounded from 0.0 to 1.0
    ambiguity_score: Annotated[
        float,
        Field(ge=0, le=1),
    ]
    """Is the query vague or open to multiple interpretations? (0.0 = clear, 1.0 = highly vague)"""

    