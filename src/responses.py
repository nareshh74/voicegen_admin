from fastapi.responses import ORJSONResponse
from src.utils import convert

class CustomResponse(ORJSONResponse):
    def __init__(self, content=None, status_code=200):
        if content:
            converted_content = convert(content)
        else:
            converted_content = {"detail": "success"}
        super().__init__(content=converted_content, status_code=status_code)
