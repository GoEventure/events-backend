from pydantic import BaseModel
from pydantic import Field

DESC_EXAMPLE = 'Come get your inner rock on while singing some of the best tunes around at music karoke.'  # noqa: E501


class EventSchema(BaseModel):

    name: str = Field(example='Cool Karoke Event')
    description: str = Field(example=DESC_EXAMPLE)
