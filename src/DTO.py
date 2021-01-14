# standard modules
from typing import List
from datetime import datetime

# 3rd party modules
from pydantic import BaseModel


# entity models
class Label(BaseModel):
    id: int
    name: str
    sampleCount: int=None

class Collection(BaseModel):
    id: int
    sampleNeededPerLabel: int=None
    durationInSecondsPerSample: int=None

class SpeechAPI(BaseModel):
    id: int
    name: str=None
    trainingStatus: str=None
    type: str=None

class SpeechAPIVersion(BaseModel):
    id: int
    speechAPI: SpeechAPI=None
    version: str=None
    lastUpdated: datetime=None

# generic responses
class SuccessResponse(BaseModel):
    detail: str

# label tagged endpoint responses
class GetAllLabelsOut(BaseModel):
    labels: List[Label]

class CreateLabelsOut(BaseModel):
    label: Label

class GetLabelCollectionsOut(BaseModel):
    collections: List[Collection]

# collection tagged endpoint responses
class CreateCollectionIn(BaseModel):
    sampleNeededPerLabel: int
    durationInSecondsPerSample: int

# speechAPI tagged endpoint responses
class GetAllSpeechAPIsOut(BaseModel):
    speechAPIs: List[SpeechAPI]

class GetAllSpeechAPIVersionsOut(BaseModel):
    speechAPIVersions: List[SpeechAPIVersion]

class GetLabelsOfSpeechAPIVersionOut(BaseModel):
    labels: List[Label]
