from rest_framework import viewsets, permissions
from rest_framework.response import Response
from api.serializers import *


class CodePromoViewSet(viewsets.ModelViewSet):
    queryset = CodePromo.objects.all()
    serializer_class = CodePromoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        h = History(code=instance, user=request.user)
        h.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return History.objects.filter(user=user)

