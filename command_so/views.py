from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.parsers import MultiPartParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import Content, Label, SiteConfig
from .serializers import ContentSeriaslzer, LabelSeriaslzer, SiteConfigSeriaslzer
from .filters import getContentFilter

def index(request):
    return render(request, "index.html")

class ContentView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
               generics.GenericAPIView):
    serializer_class = ContentSeriaslzer
    lookup_field = "id"
    queryset = Content.objects.filter(is_deleted=False)
    parser_classes = [MultiPartParser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = getContentFilter
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        SiteConfig.update_query(is_null=len(queryset)==0)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class LabelView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
               generics.GenericAPIView):
    serializer_class = LabelSeriaslzer
    lookup_field = "id"
    queryset = Label.objects.filter(is_deleted=False)
    parser_classes = [MultiPartParser]
    filter_backends = [DjangoFilterBackend]
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)



class SiteConfigView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
               generics.GenericAPIView):
    serializer_class = SiteConfigSeriaslzer
    lookup_field = "id"
    queryset = SiteConfig.objects.all()
    parser_classes = [MultiPartParser]
    filter_backends = [DjangoFilterBackend]
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)