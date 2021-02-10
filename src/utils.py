# standard modules
import traceback
import decimal, datetime

# 3rd party modules
import pyodbc
from fastapi import HTTPException, Request
from fastapi.responses import ORJSONResponse

# application modules
from src.config import config


def get_db_cursor():
    conn = pyodbc.connect(config.db_connection_string)
    return conn.cursor()

async def exception_handler(request: Request, exc: Exception):
    code = 500
    detail = str(exc)
    if isinstance(exc, HTTPException):
        code = exc.status_code
        detail = exc.detail
        print(traceback.print_exc())
    return ORJSONResponse(content={"detail":detail}, status_code=code)

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def convert(input_value):
    if isinstance(input_value, str) or isinstance(input_value, int) or isinstance(input_value, datetime.datetime) or isinstance(input_value, datetime.date):
        return input_value
    if isinstance(input_value, decimal.Decimal):
        return int(input_value)
    if isinstance(input_value, list):
        converted_input_value = []
        for n in input_value:
            converted_input_value.append(convert(n))
        return converted_input_value
    if hasattr(input_value, '__dict__'):
        input_value = input_value.__dict__
    if isinstance(input_value, dict):
        converted_input_value = {}
        for key, value in input_value.items():
            converted_input_value[to_camel_case(key)] = convert(value)
        return converted_input_value
    raise HTTPException(detail=f"Cannot convert type {type(input_value)}", status_code=500)
