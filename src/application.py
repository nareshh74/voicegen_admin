# 3rd party modules
from fastapi import FastAPI, HTTPException

# application modules
from src.routes import label, collection, speech_api
from src.utils import exception_handler


# create FastAPI instance and register routes
app = FastAPI(title="VoiceGen Admin",  description="A REST API service to be used as voicegen admin backend", exception_handlers={Exception: exception_handler, HTTPException: exception_handler})
app.include_router(label.router)
app.include_router(collection.router)
app.include_router(speech_api.router)

# add a test route
@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Hello, I'm voicegen admin API!!"}
