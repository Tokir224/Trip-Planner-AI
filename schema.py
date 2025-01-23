from pydantic import BaseModel, Field
from typing import List


class Travel(BaseModel):
    title: str = Field(description="Generate a unique and engaging travel itinerary title and do not display number of day and location name in title.")
    morning: str = Field(description="Generate detailed description where to go at morning, suggest family friendly activities and local food options also.")
    afternoon: str = Field(description="Generate detailed description where to go at afternoon, suggest family friendly activities and local food options also.")
    night: str = Field(description="Generate detailed description where to go at night, suggest family friendly activities and local food options also.Give bedtime options also.")
    day: int = Field(description="Day of travel")


class Response(BaseModel):
    itinerary: List[Travel]
