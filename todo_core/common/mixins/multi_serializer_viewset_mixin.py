from rest_framework.serializers import BaseSerializer

from common.protocols import MultiSerializerViewSetProtocol


class MultiSerializerViewSetMixin(MultiSerializerViewSetProtocol):

    def get_serializer_class(self) -> BaseSerializer:
        if self.action in self.serialzer_action_classes:
            return self.serialzer_action_classes[self.action]
        return self.serializer_class
