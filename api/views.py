from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.db.models import Max


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

    def get_queryset(self):
        time = self.request.query_params.get('time', None)
        if time:
            return CodePromo.objects.filter(create_time__lte=time, end_time__gte=time).order_by('end_time')
        return CodePromo.objects.all().order_by('end_time')


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = History.objects.filter(user=user)
        times = [i['time__max'] for i in queryset.values('code').annotate(Max('time'))]
        return queryset.filter(time__in=times).order_by('-time')
