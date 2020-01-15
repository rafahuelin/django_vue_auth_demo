from django.urls import path

from .views import ListReportView, DetailReportView

urlpatterns = [
    path('', ListReportView.as_view()),
    path('<uuid:id>/', DetailReportView.as_view()),
]