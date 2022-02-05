import json
from uuid import UUID
from abc import ABCMeta, abstractmethod
from datetime import date, datetime
from bson import ObjectId


class JSONSerializable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def toJson(self):
        pass


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, (datetime, date)):
            return o.isoformat()
        if isinstance(o, JSONSerializable):
            return o.toJson()
        if isinstance(o, UUID):
            return o.hex
        return json.JSONEncoder.default(self, o)


def clean_message(body):
    if body:
        return {k: v for k, v in json.loads(body).items() if v not in (None, '')}
