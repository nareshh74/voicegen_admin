# 3rd party modules
from fastapi import APIRouter

# application modules
from src.objects import Collection
from src import DTO


router = APIRouter(
    prefix="/collection",
    tags=["Collection"]
)


@router.post("", status_code=201)
def create_collecion(payload: DTO.CreateCollectionIn):
    created_collection = Collection.create(payload.sampleNeededPerLabel, payload.durationInSecondsPerSample)
    return {"collection": created_collection.toORJSON()}
