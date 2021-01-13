# standard modules
import traceback

# 3rd party modules
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import ORJSONResponse

# application modules
from src.routes import label, collection, speech_api
from src.utils import exception_handler


# create FastAPI instance and register routes
app = FastAPI(title="VoiceGen Admin",  description="A REST API service to be used as voicegen admin backend", include_in_schema=False, exception_handlers={Exception: exception_handler, HTTPException: exception_handler})
app.include_router(label.router)
app.include_router(collection.router)
app.include_router(speech_api.router)

# add a test route
@app.get("/")
async def root():
    return {"message": "Hello World"}
