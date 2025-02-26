from typing import Protocol

from rest_framework.serializers import BaseSerializer


class MultiSerializerViewSetProtocol(Protocol):

    serialzer_action_classes: dict[str, BaseSerializer]
    serializer_class: BaseSerializer

    def get_serializer_class(self) -> BaseSerializer: ...
