# standard modules
import traceback

# 3rd party modules
import pyodbc
from fastapi import HTTPException, Request
from fastapi.responses import ORJSONResponse

# application modules
from src.config import config
from src.mixins import ORJSONSerializableMixin


def get_db_cursor():
    conn = pyodbc.connect(config.db_connection_string)
    return conn.cursor()

def list_to_orjson_list(entities_list):
    if len(entities_list) == 0:
        return []
    if not isinstance(entities_list[0], ORJSONSerializableMixin):
        raise HTTPException(detail="List can't be serialized to ORJSON", status_code=500)
    entities_orjson_list = []
    for entity in entities_list:
        entities_orjson_list.append(entity.toORJSON())
    return entities_orjson_list

async def exception_handler(request: Request, exc: HTTPException):
    print(str(exc))
    print(traceback.print_exc())
    code = exc.status_code or 500
    detail = exc.detail or "Server Error"
    return ORJSONResponse(content={"detail":detail}, status_code=code)
