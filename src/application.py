# 3rd party modules
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

# application modules
from src.routes import label, collection, speech_api
from src.utils import exception_handler


# create FastAPI instance
app = FastAPI(title="VoiceGen Admin",  description="A REST API service to be used as voicegen admin backend", exception_handlers={Exception: exception_handler, HTTPException: exception_handler}, docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")

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

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css"
    )

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )
