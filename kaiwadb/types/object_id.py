from typing import Any, Callable
from bson import ObjectId as _ObjectId
from pydantic_core import core_schema


class ObjectId(_ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: Callable[[Any], core_schema.CoreSchema],
    ) -> core_schema.CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema(
                [
                    core_schema.is_instance_schema(_ObjectId),
                    core_schema.no_info_plain_validator_function(lambda x: cls(x)),
                ]
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: str(x), return_schema=core_schema.str_schema(), when_used="json"
            ),
        )
