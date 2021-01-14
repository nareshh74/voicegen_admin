# 3rd party modules
from fastapi import APIRouter

# application modules
from src.objects import Collection
from src import DTO
from src.responses import CustomResponse


router = APIRouter(
    prefix="/collection",
    tags=["Collection"]
)


@router.post("", response_model=DTO.Collection, status_code=201)
def create_collecion(payload: DTO.CreateCollectionIn):
    created_collection = Collection.create(payload.sampleNeededPerLabel, payload.durationInSecondsPerSample)
    return CustomResponse(content={"collection": created_collection}, status_code=201)
