from uuid import UUID

import pytest
from pydantic import ValidationError

from tdd_project.core.schemas.product import ProductIn


def test_schemas_return_success():
    data = {"name": 'Iphone 14 pro max',
            'quantity': 10,
            "price": 8500,
            "status": True
    }

    product = ProductIn.model_validate(data)  # type: ignore # noqa: E501, F821

    assert product.name == 'Iphone 14 pro max'
    assert isinstance(product.id, UUID)


def test_schemas_return_raise():
    data = {"name": 'Iphone 14 pro max',
            'quantity': 10,
            "price": 8500,
    }

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)
    assert len(err.value.errors()) == 1
    error = err.value.errors()[0]
    assert error['loc'] == ('status',)
    assert error['msg'] == 'Field required'
    assert error['type'] == 'missing'
