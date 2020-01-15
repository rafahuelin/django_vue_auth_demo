from rest_framework import generics

from .models import Report
from .serializers import ReportSerializer


def access_level_queryset(self):
    user = self.request.user
    group_names = [group.name for group in user.groups.all()]

    if 'gold' in group_names:
        queryset = Report.objects.all()
    elif 'silver' in group_names:
        queryset = Report.objects.exclude(minimum_access_level='gold')
    elif 'bronze' in group_names:
        queryset = Report.objects.filter(minimum_access_level__in='bronze')
    else:
        queryset = None
        
    return queryset


class ListReportView(generics.ListAPIView):
    serializer_class = ReportSerializer

    def get_queryset(self):
        return access_level_queryset(self)


class DetailReportView(generics.RetrieveAPIView):
    serializer_class = ReportSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return access_level_queryset(self)