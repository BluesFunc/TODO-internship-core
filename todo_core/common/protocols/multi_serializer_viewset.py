from typing import Protocol

from rest_framework.serializers import BaseSerializer


class MultiSerializerViewSetProtocol(Protocol):

    serializer_action_classes: dict[str, BaseSerializer]
    serializer_class: BaseSerializer
    action: str

    def get_serializer_class(self) -> BaseSerializer: ...
