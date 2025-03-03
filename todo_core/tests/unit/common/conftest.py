from typing import Type

import pytest
from rest_framework.generics import GenericAPIView
from rest_framework.serializers import BaseSerializer

from common.mixins import MultiSerializerViewSetMixin


@pytest.fixture
def multi_serializer_viewset_mixin() -> GenericAPIView:
    mixin = type("mixin_class", (MultiSerializerViewSetMixin, GenericAPIView), {})()
    mixin.serializer_action_classes = {}
    return mixin


@pytest.fixture()
def mixin_with_base_serializer(
    multi_serializer_viewset_mixin: GenericAPIView,
) -> GenericAPIView:
    multi_serializer_viewset_mixin.serializer_class = BaseSerializer
    return multi_serializer_viewset_mixin


@pytest.fixture
def serializer_classes_dictionary_with_viewset_actions() -> (
    dict[str, Type[BaseSerializer]]
):
    return {
        "list": BaseSerializer,
    }
