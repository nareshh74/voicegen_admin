# standard modules
from typing import List
from datetime import datetime

# 3rd party modules
from pydantic import BaseModel


# entity models
class Label(BaseModel):
    id: int
    name: str=None
    sampleCount: int=None

class Collection(BaseModel):
    id: int
    name: str=None
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

class GetSampleDurationsOfLabelsIn(BaseModel):
    labels: List[int]

class GetSampleDurationsOfLabelsOut(BaseModel):
    sampleDurations: List[int]

# collection tagged endpoint responses
class CreateCollectionIn(BaseModel):
    sampleNeededPerLabel: int
    durationInSecondsPerSample: int
    name: str=None

class GetAllCollectionsOut(BaseModel):
    collections: List[Collection]
    
# speechAPI tagged endpoint responses
class GetAllSpeechAPIsOut(BaseModel):
    speechAPIs: List[SpeechAPI]

class GetAllSpeechAPIVersionsOut(BaseModel):
    speechAPIVersions: List[SpeechAPIVersion]

class GetLabelsOfSpeechAPIVersionOut(BaseModel):
    labels: List[Label]

class TrainSpeechAPIIn(BaseModel):
    labels: List[int]
    sampleDuration: int
    class Config:
        schema_extra = {
            "example": {
                "labels": [1, 2, 3],
                "sampleDuration": 5
            }
        }

class GetLabelsOfSpeechAPIOut(BaseModel):
    labels: List[Label]
