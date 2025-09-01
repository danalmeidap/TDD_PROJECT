from typing import Annotated

from bson import ObjectId
from pydantic import ConfigDict, Field, PositiveFloat

from tdd_project.core.schemas.base import BaseSchemaMixim


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):  # noqa: PLW3201
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)


class ProductSchema(BaseSchemaMixim):
    name: Annotated[
        str,
        Field(
            description='Nome do produto',
            examples=['Iphone 14 pro max'],
            max_length=60,
        ),
    ]
    quantity: Annotated[
        int, Field(description='Quantidade do produto', examples=[15])
    ]
    price: Annotated[
        PositiveFloat, Field(description='Preço do produto', examples=[8500.0])
    ]
    status: Annotated[
        bool,
        Field(description='Situação do produto em estoque', examples=[True]),
    ]


class ProductIn(ProductSchema):
    pass


class ProductOut(ProductSchema):
    id: Annotated[
        PyObjectId, Field(alias='_id', description='ID do produto no MongoDB')
    ]  # noqa: E501

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
    )
