from pydantic import BaseModel, Field, conint
from typing import Optional

DESC_EXAMPLE = "Come get your inner rock on while singing some of the best tunes around at music karoke."


class EventSchema(BaseModel):

    name: str = Field(example="Cool Karoke Event")
    description: str = Field(example=DESC_EXAMPLE)
