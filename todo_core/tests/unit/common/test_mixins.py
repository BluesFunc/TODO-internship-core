from typing import Type

import pytest
from rest_framework.generics import GenericAPIView
from rest_framework.serializers import BaseSerializer


@pytest.mark.parametrize(
    "action,expected", [("list", BaseSerializer), ("zxc123", BaseSerializer)]
)
def test_multiserializer_viewset_mixin(
    mixin_with_base_serializer: GenericAPIView,
    serializer_classes_dictionary_with_viewset_actions: dict[str, Type[BaseSerializer]],
    expected: Type[BaseSerializer],
    action: str,
) -> None:
    mixin_with_base_serializer.action = action
    result = mixin_with_base_serializer.get_serializer_class()
    assert result == expected
