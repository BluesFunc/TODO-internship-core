from typing import Type

from rest_framework.serializers import BaseSerializer

from common.protocols import MultiSerializerViewSetProtocol


class MultiSerializerViewSetMixin(MultiSerializerViewSetProtocol):

    def get_serializer_class(self) -> Type[BaseSerializer]:
        if self.action in self.serializer_action_classes:
            return self.serializer_action_classes[self.action]
        return self.serializer_class
