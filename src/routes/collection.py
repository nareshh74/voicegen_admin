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
    created_collection = Collection.create(payload.sampleNeededPerLabel, payload.durationInSecondsPerSample, name=payload.name)
    return CustomResponse(content={"collection": created_collection}, status_code=201)

@router.get("", response_model=DTO.GetAllCollectionsOut, status_code=200)
def get_all_collections():
    collections = Collection.get_all()
    return CustomResponse(content={"collections": collections}, status_code=200)

@router.post("{collectionId}", response_model=DTO.AddLabelsToCollectionOut, status_code=201)
def add_labels_to_collection(collectionId: int, payload: DTO.AddLabelsToCollectionIn):
    collection = Collection(collectionId)
    created_mappings = collection.add_labels(payload.labels)
    return CustomResponse(content={"mappings": created_mappings}, status_code=201)
