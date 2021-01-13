# 3rd party modules
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

# application modules
from src.objects import Label, Collection
from src.utils import list_to_orjson_list
from src import DTO


router = APIRouter(
    prefix="/label",
    tags=["Label"]
)


@router.get("", status_code=200)
async def get_all_labels():
    labels_list = Label.get_all()
    labels_orjson_list = list_to_orjson_list(labels_list)
    return {"labels": labels_orjson_list}

@router.post("{labelName}", status_code=201)
async def create_label(labelName: str):
    created_label = Label.create(labelName)
    return {"label": created_label.toORJSON()}

@router.post("/{labelId}/collection/{collectionId}", status_code=201)
async def add_to_collection(labelId: int, collectionId: int):
    collection = Collection(collectionId)
    label = Label(labelId)
    label.add_to_collection(collection)
    return ORJSONResponse(content={"detail": "success"}, status_code=201)

@router.get("/{labelId}/collection", status_code=200)
async def get_label_collections(labelId: int):
    label = Label(labelId)
    collections_list = label.get_collections()
    collections_orjson_list = list_to_orjson_list(collections_list)
    return {"collections": collections_orjson_list}
