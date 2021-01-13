# 3rd party modules
from pydantic import BaseModel


class CreateCollectionIn(BaseModel):
    sampleNeededPerLabel: int
    durationInSecondsPerSample: int
