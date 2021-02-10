# 3rd party modules
from fastapi import APIRouter

# application modules
from src.objects import Label, Collection
from src.responses import CustomResponse
from src import DTO


router = APIRouter(
    prefix="/label",
    tags=["Label"]
)


@router.get("", response_model=DTO.GetAllLabelsOut, status_code=200)
async def get_all_labels():
    labels_list = Label.get_all()
    return CustomResponse(content={"labels": labels_list})

@router.post("/{labelName}", response_model=DTO.CreateLabelsOut, status_code=201)
async def create_label(labelName: str):
    created_label = Label.create(labelName)
    return CustomResponse(content={"label": created_label}, status_code=201)

@router.post("/{labelId}/collection/{collectionId}", response_model=DTO.SuccessResponse, status_code=201)
async def add_to_collection(labelId: int, collectionId: int):
    collection = Collection(collectionId)
    label = Label(labelId)
    label.add_to_collection(collection)
    return CustomResponse(status_code=201)

@router.get("/{labelId}/collection", response_model=DTO.GetLabelCollectionsOut, status_code=200)
async def get_label_collections(labelId: int):
    label = Label(labelId)
    collections_list = label.get_collections()
    return CustomResponse(content={"collections": collections_list})

@router.get("/SampleDurations", response_model=DTO.GetSampleDurationsOfLabelsOut, status_code=200)
async def get_sample_duration_of_labels(payload: DTO.GetSampleDurationsOfLabelsIn):
    labels_list = []
    for id in payload.labels:
        labels_list.append(Label(id))
    return CustomResponse(content={"sampleDurations": Label.get_sample_duration_of_labels(labels_list)})
