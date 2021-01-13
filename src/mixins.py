# standard modules
import decimal
import abc

# 3rd party modules
import orjson


def orjson_encoder(obj):
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    return obj.__dict__


class ORJSONSerializableMixin(abc.ABC):
    def toORJSON(self):
        return orjson.dumps(self, default=orjson_encoder)
