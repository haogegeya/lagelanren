import json

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.parsers import MultiPartParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .serializers import ContentSeriaslzer, LeaveMessageSeriaslzer
from .models import Content, Key, LeaveMessage
from .filters import getContentFilter
import logging
from django.conf import settings
_logger = logging.getLogger(settings.LOGGERS_NAME)

def index(request):
    return render(request, "five_two_zero_index.html")


# Create your views here.
class ContentView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
               generics.GenericAPIView):
    serializer_class = ContentSeriaslzer
    lookup_field = "id"
    queryset = Content.objects.filter(is_deleted=False, is_activate=True).order_by("-update_time")
    parser_classes = [MultiPartParser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = getContentFilter
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        key = request.GET.get("q")
        _logger.info(f"================ {key}")
        Key.update_key_total(key)
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


def site_total(request):
    return HttpResponse(json.dumps({
        "total_data": Content.objects.count(),
        "total_view": Key.objects.aggregate(Sum('total'))
    }))


class LeaveMessageView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
               generics.GenericAPIView):
    serializer_class = LeaveMessageSeriaslzer
    lookup_field = "id"
    queryset = LeaveMessage.objects.filter(is_deleted=False).order_by("-update_time")
    parser_classes = [MultiPartParser]
    filter_backends = [DjangoFilterBackend]
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)