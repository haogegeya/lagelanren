
# Create your views here.
from rest_framework import mixins, generics
from rest_framework.parsers import MultiPartParser
from django_filters.rest_framework import DjangoFilterBackend

from .models import Image
from storage.serializers import ImageSeriaslzer


class ImageView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
               generics.GenericAPIView):
    serializer_class = ImageSeriaslzer
    lookup_field = "id"
    queryset = Image.objects.filter(is_deleted=False)
    parser_classes = [MultiPartParser]
    filter_backends = [DjangoFilterBackend]
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)