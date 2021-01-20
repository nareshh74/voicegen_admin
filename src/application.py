# 3rd party modules
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# application modules
from src.routes import label, collection, speech_api
from src.utils import exception_handler


# create FastAPI instance
app = FastAPI(title="VoiceGen Admin",  description="A REST API service to be used as voicegen admin backend", exception_handlers={Exception: exception_handler, HTTPException: exception_handler})

# add routes
app.include_router(label.router)
app.include_router(collection.router)
app.include_router(speech_api.router)

# add middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

# add a test route
@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Hello, I'm voicegen admin API!!"}
