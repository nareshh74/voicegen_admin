# 3rd party modules
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

# application modules
from src.objects import SpeechAPI, SpeechAPIVersion
from src import DTO
from src.utils import list_to_orjson_list


router = APIRouter(
    prefix="/speechAPI",
    tags=["SpeechAPI"]
)


@router.get("", status_code=200)
def get_all_speech_apis():
    speech_apis_list = SpeechAPI.get_all()
    speech_apis_orjson_list = list_to_orjson_list(speech_apis_list)
    return {"speechAPIs": speech_apis_orjson_list}

@router.get("/{speechAPIId}/speechAPIVersion", status_code=200)
def get_versions(speechAPIId: int):
    speech_api = SpeechAPI(speechAPIId)
    speech_api_versions_list = speech_api.get_speech_api_versions()
    speech_api_versions_orjson_list = list_to_orjson_list(speech_api_versions_list)
    return {"speechAPIVersions": speech_api_versions_orjson_list}

@router.get("/{speechAPIId}/speechAPIVersion/{speechAPIVersionId}/labels", status_code=200)
def get_labels(speechAPIId: int, speechAPIVersionId: int):
    speech_api = SpeechAPI(speechAPIId)
    speech_api_version = SpeechAPIVersion(speechAPIVersionId, speech_api=speech_api)
    labels_list = speech_api_version.get_labels()
    labels_orjson_list = list_to_orjson_list(labels_list)
    return {"labels": labels_orjson_list}

@router.post("/{speechAPIId}/train", status_code=200)
def train_speech_api(speechAPIId: int):
    speech_api = SpeechAPI(speechAPIId)
    speech_api.train()
    return ORJSONResponse(content={"detail": "success"}, status_code=200)
