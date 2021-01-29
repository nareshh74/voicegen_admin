# 3rd party modules
from os import name
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

# application modules
from src.objects import SpeechAPI, SpeechAPIVersion, Label
from src import DTO
from src.responses import CustomResponse


router = APIRouter(
    prefix="/speechAPI",
    tags=["SpeechAPI"]
)


@router.post("/{SpeechAPIName}", response_model=DTO.CreateSpeechAPIOut, status_code=201)
def create_speech_api(speechAPIName: str, payload: DTO.CreateSpeechAPIIn):
    labels_id_csv = ""
    for label_id in payload.labels:
        labels_id_csv += str(label_id)
    speech_apis = SpeechAPI.create(speechAPIName, description=payload.description, labels=labels_id_csv)
    speech_api = SpeechAPI(speech_apis[0].id, name=speechAPIName)
    speech_api.train(labels_id_csv, payload.sampleDuration)
    return CustomResponse()

@router.get("", response_model=DTO.GetAllSpeechAPIsOut, status_code=200)
def get_all_speech_apis():
    speech_apis_list = SpeechAPI.get_all()
    return CustomResponse(content={"speechAPIs": speech_apis_list})

@router.get("/{speechAPIId}/speechAPIVersion", response_model=DTO.GetAllSpeechAPIVersionsOut, status_code=200)
def get_all_speech_api_versions(speechAPIId: int):
    speech_api = SpeechAPI(speechAPIId)
    speech_api_versions_list = speech_api.get_speech_api_versions()
    return CustomResponse(content={"speechAPIVersions": speech_api_versions_list})

@router.get("/{speechAPIId}/speechAPIVersion/{speechAPIVersionId}/labels", response_model=DTO.GetLabelsOfSpeechAPIVersionOut, status_code=200)
def get_labels_of_speech_api_version(speechAPIId: int, speechAPIVersionId: int):
    speech_api = SpeechAPI(speechAPIId)
    speech_api_version = SpeechAPIVersion(speechAPIVersionId, speech_api=speech_api)
    labels_list = speech_api_version.get_labels_of_speech_api_version()
    return CustomResponse(content={"labels": labels_list})

@router.get("/{speechPAIId}/labels", response_model=DTO.GetLabelsOfSpeechAPIOut, status_code=200)
def get_labels_of_speech_api(speechAPIId: int):
    speech_api = SpeechAPI(speechAPIId)
    labels_list = speech_api.get_labels_of_speech_api()
    return CustomResponse(content={"labels": labels_list}, status_code=200)

@router.post("/{speechAPIId}/train", response_model=DTO.SuccessResponse, status_code=200)
def train_speech_api(speechAPIId: int, payload: DTO.TrainSpeechAPIIn):
    speech_api = SpeechAPI(speechAPIId)
    labels_id_csv = ""
    for label_id in payload.labels:
        labels_id_csv += str(label_id)
    labels_id_csv = labels_id_csv[:-1]
    speech_api.train(labels_id_csv, payload.sampleDuration)
    return CustomResponse()
