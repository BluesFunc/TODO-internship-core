from typing import Protocol, Type

from rest_framework.serializers import BaseSerializer


class MultiSerializerViewSetProtocol(Protocol):

    serializer_action_classes: dict[str, Type[BaseSerializer]]
    serializer_class: Type[BaseSerializer]
    action: str

    def get_serializer_class(self) -> Type[BaseSerializer]:
        raise NotImplementedError()
